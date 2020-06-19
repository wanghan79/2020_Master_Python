# -*- coding: utf-8 -*-

from .BasicModule import BasicModule
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
torch.set_printoptions(profile="full")


class PCNN(BasicModule):
    '''
    the basic model
    Zeng 2014 "Relation Classification via Convolutional Deep Neural Network"
    '''

    def __init__(self, opt):
        super(PCNN, self).__init__()
        # print("初始化对象")
        self.opt = opt

        self.model_name = 'PCNN'

        self.word_embs = nn.Embedding(self.opt.vocab_size, self.opt.word_dim)  # 22315, 50
        self.pos1_embs = nn.Embedding(self.opt.pos_size + 1, self.opt.pos_dim) # 102 + 1, 5
        self.pos2_embs = nn.Embedding(self.opt.pos_size + 1, self.opt.pos_dim) # 102 + 1, 5

        feature_dim = self.opt.word_dim + self.opt.pos_dim * 2  # 60

        # encoding sentence level feature via cnn
        #(in_channel=1, out_channel=230, (k=3, 60), stride=1, padding=1, dilation=0)
        self.convs = nn.ModuleList([nn.Conv2d(1, self.opt.filters_num, (k, feature_dim), padding=(int(k / 2), 0)) for k in self.opt.filters])
        # all_filter_num = 230 * 1 len(opt.filter)=1
        all_filter_num = self.opt.filters_num * len(self.opt.filters)
        # Linear(230, 230)  (size of input example, size of output example)
        self.cnn_linear = nn.Linear(all_filter_num, self.opt.sen_feature_dim)

        # self.cnn_linear = nn.Linear(all_filter_num, self.opt.rel_num)

        # concat the lexical feature in the out architecture
        # 分类层 230 + 50 * 6 , 19
        self.out_linear = nn.Linear(all_filter_num + self.opt.word_dim * 6, self.opt.rel_num)
        # print("out_linear: ", self.out_linear)
        self.dropout = nn.Dropout(self.opt.drop_out)
        # 初始化
        self.init_word_emb()
        self.init_model_weight()

        print("model初始化完成")

    def init_model_weight(self):
        # print("使用init_model_weight")
        '''
        use xavier to init
        '''
        nn.init.xavier_normal_(self.cnn_linear.weight)
        nn.init.constant_(self.cnn_linear.bias, 0.)
        nn.init.xavier_normal_(self.out_linear.weight)
        nn.init.constant_(self.out_linear.bias, 0.)
        for conv in self.convs:
            print(conv)
            nn.init.xavier_normal_(conv.weight)
            nn.init.constant_(conv.bias, 0)
        # print("over")

    def init_word_emb(self):
        # print("使用了init_word_emb")

        w2v = torch.from_numpy(np.load(self.opt.w2v_path))

        # w2v = torch.div(w2v, w2v.norm(2, 1).unsqueeze(1))
        # w2v[w2v != w2v] = 0.0

        if self.opt.use_gpu:
            self.word_embs.weight.data.copy_(w2v.cuda())
        else:
            self.word_embs.weight.data.copy_(w2v)
        # print("over")

    def forward(self, x):
        # print("使用了forward")

        lexical_feature, word_feautre, left_pf, right_pf = x
        # print(
        #     "lexical_feature", lexical_feature,
        #     "\nword_feature", word_feautre,
        #     "\nleft_pf", left_pf,
        #     "\nright_pf", right_pf
        #       )


        # No USE: lexical word embedding,
        batch_size = lexical_feature.size(0) # 128
        # print("lexical_feature size", lexical_feature.size())
        """将lexcial_feature 嵌入到50维向量中，[x , x, x, x, x, x ] -> [50x]
        lexical_level_emb 128 * 6 * 50
        """
        lexical_level_emb = self.word_embs(lexical_feature)  # (batch_size, 6, word_dim
        # 将 lexical_level_emb 转换为 128 * 300 的二维
        lexical_level_emb = lexical_level_emb.view(batch_size, -1)
        # print("lexical_level_emb size", lexical_level_emb.size())


        # sentence level feature
        word_emb = self.word_embs(word_feautre)  # (batch_size, max_len, word_dim) 128 * 98 * 50
        left_emb = self.pos1_embs(left_pf)  # (batch_size, max_len, pos_dim) 128 * 98 * 5
        right_emb = self.pos2_embs(right_pf)  # (batch_size, max_len, pos_dim)


        # 128 * 98 * 60 延第三维度拼接[128, 98, 50] [128, 98, 5] [128, 98, 5] --> [128, 98, 60]
        sentence_feature = torch.cat([word_emb, left_emb, right_emb], 2)  # (batch_size, max_len, word_dim + pos_dim *2)

        # conv part 在 1 位置添加一个维度 [128, 1, 98, 60]，因为
        x = sentence_feature.unsqueeze(1)
        # [128, 1, 98, 60]
        x = self.dropout(x)
        x = [F.relu(conv(x)).squeeze(3) for conv in self.convs] # (128, 230, 98)
        x = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x]
        x = torch.cat(x, 1) # 128, 230
        #  sen_level_emb = self.cnn_linear(x)
        #  sen_level_emb = self.tanh(sen_level_emb)
        sen_level_emb = x

        # combine lexical and sentence level emb
        x = torch.cat([lexical_level_emb, sen_level_emb], 1)
        x = self.dropout(x)
        x = self.out_linear(x)
        print("over")
        return x
