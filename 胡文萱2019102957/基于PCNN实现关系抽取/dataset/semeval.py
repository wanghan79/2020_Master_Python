# -*- coding: utf-8 -*-

from torch.utils.data import Dataset
import os
import numpy as np
import string

# 保证所有数据能够显示，而不是用省略号表示，np.inf表示一个足够大的数
np.set_printoptions(threshold=np.inf)
# z:
np.set_printoptions(suppress=True)

class SEMData(Dataset):

    def __init__(self, root_path, train=True):
        if train:
            path = os.path.join(root_path, 'train/npy/')
            print('loading train data')
        else:
            path = os.path.join(root_path, 'test/npy/')
            print('loading test data')

        # print("加载 word,lexical-feature,right_pf,left_pf")
        self.word_feautre = np.load(path + 'word_feautre.npy')
        self.lexical_feature = np.load(path + 'lexical_feature.npy')
        self.right_pf = np.load(path + 'right_pf.npy')
        self.left_pf = np.load(path + 'left_pf.npy')
        self.labels = np.load(path + 'labels.npy')
        # x 为 5 + 98 * 3 + 3
        self.x = list(zip(self.lexical_feature, self.word_feautre, self.left_pf, self.right_pf, self.labels))
        # print(self.x)
        print('loading finish')

    def __getitem__(self, idx):
        assert idx < len(self.x)
        return self.x[idx]

    def __len__(self):
        return len(self.x)


class SEMLoad(object):
    '''
    load and preprocess data
    '''
    def __init__(self, root_path, train=True, max_len=98, limit=50):

        self.stoplists = set(string.punctuation)

        self.max_len = max_len
        self.limit = limit
        self.root_path = root_path
        self.train = train
        if self.train:
            print('train data:')
        else:
            print('test data:')

        self.rel_path = os.path.join(root_path, 'relation2id.txt')
        self.w2v_path = os.path.join(root_path, 'vector_50.txt')
        self.train_path = os.path.join(root_path, 'train.txt')
        self.vocab_path = os.path.join(root_path, 'vocab.txt')
        self.test_path = os.path.join(root_path, 'test.txt')

        print('loading start....')
        # 关系字典，关系： id
        self.rel2id, self.id2rel = self.load_rel()
        #单词字典 ， 单词： id
        self.w2v, self.word2id, self.id2word = self.load_w2v()

        # print("word2id['<PAD>'] is ",self.word2id['<PAD>'])
        """
        w2v 是单词的向量， word2id ’i‘,0. '(', 2, id2word
        """

        if train:
            """
            lexical_feature，lexical_feature 表示两个实体，及其左右单词的向量id
            sen_feature, 句子的embeding，position1 embedding ,postion2 embedding 98 * 3
            label 每个句子对应的关系
            """
            self.lexical_feature, sen_feature, self.labels = self.parse_sen(self.train_path)
            print("sen_feature",sen_feature)
        else:
            self.lexical_feature, sen_feature, self.labels = self.parse_sen(self.test_path)

        self.word_feautre, self.left_pf, self.right_pf = sen_feature
        print('loading finish')

    def save(self):
        if self.train:
            prefix = 'train'
        else:
            prefix = 'test'
        np.save(os.path.join(self.root_path, prefix, 'npy/word_feautre.npy'), self.word_feautre)
        np.save(os.path.join(self.root_path, prefix, 'npy/left_pf.npy'), self.left_pf)
        np.save(os.path.join(self.root_path, prefix, 'npy/right_pf.npy'), self.right_pf)
        np.save(os.path.join(self.root_path, prefix, 'npy/lexical_feature.npy'), self.lexical_feature)
        np.save(os.path.join(self.root_path, prefix, 'npy/labels.npy'), self.labels)
        np.save(os.path.join(self.root_path, prefix, 'npy/w2v.npy'), self.w2v)
        print('save finish!')

    def load_rel(self):
        '''
        load relations  获取关系r对应的id 字典
        # 读取dataset的每行，删除'\n'，然后以空格分隔
        [['0 Cause-Effect(e1,e2)], ......]
        [['0', 'Cause-Effect(e1,e2)']......]
        '''
        rels = [i.strip('\n').split() for i in open(self.rel_path)]

        # print(rels)# [['0', 'Cause-Effect(e1,e2)']......]
        rel2id = {j: int(i) for i, j in rels}
        id2rel = {int(i): j for i, j in rels}

        return rel2id, id2rel

    def load_w2v(self):
        '''
        reading from vec.bin
        add two extra tokens:
            : UNK for unkown tokens
            : BLANK for the max len sentence
            获取词向量表示形式，和单词与id之间的字典
        '''
        wordlist = []
        vecs = []

        w2v = open(self.w2v_path)
        for line in w2v:
            line = line.strip('\n').split()
            word = line[0]
            vec = list(map(float, line[1:]))
            wordlist.append(word)
            vecs.append(np.array(vec))

        # wordlist.append('UNK')
        # wordlist.append('BLANK')
        # vecs.append(np.random.normal(size=dim, loc=0, scale=0.05))
        # vecs.append(np.random.normal(size=dim, loc=0, scale=0.05))
        # vecs.append(np.zeros(dim))
        # vecs.append(np.zeros(dim))
        word2id = {j: i for i, j in enumerate(wordlist)}
        id2word = {i: j for i, j in enumerate(wordlist)}

        return np.array(vecs, dtype=np.float32), word2id, id2word

    def parse_sen(self, path):
        '''
        parse the records in data
        将句子与关系向量表示
        '''
        all_sens =[]
        all_labels =[]
        for line in open(path, 'r'):
            line = line.strip('\n').split(' ')
            sens = line[5:]

# """['a', 'few', 'days', 'before', 'the', 'service', ',', 'tom', 'burris', 'had', 'thrown', 'into', 'karen', "'", 's', 'casket',
# 'his', 'wedding', 'ring']"""

            # print(sens)
            rel = int(line[0])  # 第一个是关系

            ent1 = (int(line[1]), int(line[2]))  # 实体1
            ent2 = (int(line[3]), int(line[4]))  # 实体2

            all_labels.append(rel)
            sens = list(map(lambda x: self.word2id.get(x, self.word2id['<PAD>']), sens))
            # [539, 7805, 5501, 2295, 20093, 17916, 4, 20375, 3140, 9235, 20235, 10646, 11050, 1, 17335, 3502, 9673,
            #  21803, 17072]
            all_sens.append((ent1, ent2, sens))
            # ((15, 15), (18, 18),
            #  [539, 7805, 5501, 2295, 20093, 17916, 4, 20375, 3140, 9235, 20235, 10646, 11050, 1, 17335, 3502, 9673,
            #   21803, 17072])

        # lexical_feature 表示两个实体，及其左右单词的向量id [3502, 17335, 9673, 17072, 21803, 22314]]
        lexical_feature = self.get_lexical_feature(all_sens)
        # sen_feature 包含 position embedding
        sen_feature = self.get_sentence_feature(all_sens)

        return lexical_feature, sen_feature, all_labels

    def get_lexical_feature(self, sens):
        '''
        : noun1
        : noun2
        : left and right tokens of noun1
        : left and right tokens of noun2
        : # WordNet hypernyms
        '''

        lexical_feature = []
        for idx, sen in enumerate(sens):
            # 输出all_sen 每个元素
            pos_e1, pos_e2, sen = sen
            # pos_e1 (15, 15)
            # pos_e2 (18, 18)
            # sen [539, 7805, 5501, 2295, 20093, 17916, 4, 20375, 3140, 9235, 20235, 10646, 11050, 1, 17335, 3502, 9673, 21803, 17072
            left_e1 = self.get_left_word(pos_e1, sen)
             # 1实体左侧 17335 's'
            left_e2 = self.get_left_word(pos_e2, sen)
            # 2实体左侧 21803 'wedding'
            right_e1 = self.get_right_word(pos_e1, sen)
            # 1实体 右侧 9673 'his'
            right_e2 = self.get_right_word(pos_e2, sen)
            # 2实体右侧 22314 pad 00000
            lexical_feature.append([sen[pos_e1[0]], left_e1, right_e1, sen[pos_e2[0]], left_e2, right_e2])
            # [3502, 17335, 9673, 17072, 21803, 22314]] casket s his ring  wedding x00000

        return lexical_feature

    def get_sentence_feature(self, sens):
        '''
        : word embedding
        : postion embedding
        return:
        sen list
        pos_left
        pos_right
        '''
        update_sens = []

        for sen in sens:
            pos_e1, pos_e2, sen = sen # pos_e1 (15, 15) pos_e2 (18, 18) sen [539, 7805, 5501, 2295, 20093, 17916, 4, 20375, 3140, 9235, 20235, 10646, 11050, 1, 17335, 3502, 9673, 21803, 17072
            pos_left = []
            pos_right = []
            ori_len = len(sen)
            # print("开始\n")
            for idx in range(ori_len):
                p1 = self.get_pos_feature(idx - pos_e1[0])  # idx - 15 36~54
                p2 = self.get_pos_feature(idx - pos_e2[0])  # idx - 18 33~51

                pos_left.append(p1)
                # print(pos_left)
                pos_right.append(p2)
                # print(pos_right)

            if ori_len > self.max_len:  # max_len = 98
                sen = sen[: self.max_len]
                pos_left = pos_left[: self.max_len]
                pos_right = pos_right[: self.max_len]
            elif ori_len < self.max_len:

                sen.extend([self.word2id['<PAD>']] * (self.max_len - ori_len)) #  * (98 - 19) sen 长为 98 将后面全部置为22314
                # print(sen)
                pos_left.extend([self.limit * 2 + 2] * (self.max_len - ori_len)) # 将98 之后的 置为102
                pos_right.extend([self.limit * 2 + 2] * (self.max_len - ori_len))

            update_sens.append([sen, pos_left, pos_right]) # [[sen], [pos_left], [pos_right]] 98 * 3

            # print(update_sens)

        return zip(*update_sens) # 将update解压，变成[sen], [pos_left], [pos_right]

    def get_left_word(self, pos, sen):
        '''
        get the left word id of the token of position
        '''
        pos = pos[0]   #  # ((15, 15), (18, 18),
            #  [539, 7805, 5501, 2295, 20093, 17916, 4, 20375, 3140, 9235, 20235, 10646, 11050, 1, 17335, 3502, 9673,
            #   21803, 17072])  pos = 15
        if pos > 0:
            return sen[pos - 1]   # sen[14] 17335
        else:
            # return sen[pos]
            return self.word2id['<PAD>']

    def get_right_word(self, pos, sen):
        '''
        get the right word id of the token of position
        '''
        pos = pos[1]
        if pos < len(sen) - 1:
            return sen[pos + 1]
        else:
            # return sen[pos]
            return self.word2id['<PAD>']

    def get_pos_feature(self, x):
        '''
        clip the postion range:
        : -limit ~ limit => 0 ~ limit * 2+2
        : -51 => 0
        : -50 => 1
        : 50 => 101
        : >50: 102
        '''
        # 0 - 15 , 0 - 18
        if x < -self.limit:
            return 0
        if -self.limit <= x <= self.limit:
            return x + self.limit + 1  # -15 + 50 +1 = 36
        if x > self.limit:
            return self.limit * 2 + 1


if __name__ == "__main__":
    # 在当前目录生成数据
    # data = SEMLoad('./SemEval/', train=True)
    # print(len(data.word2id))
    # data.save()
    # data = SEMLoad('./SemEval/', train=False)
    print(np.load('./SemEval/train/npy/lexical_feature.npy'))
    print(len(np.load('./SemEval/train/npy/lexical_feature.npy')))
    # data.save()
