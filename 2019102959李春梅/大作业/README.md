# Python实现英文词性标注
<br>学号：2019102959
<br>姓名：李春梅
<br>专业：软件工程
## 一、任务概述
主  题：词性标注；<br>
数据集：traindata.txt，每一行是一个单词，“/”后面是它的词性；<br>
目  标：给出一个新的句子，对其中的每个词进行词性标注；<br>
方  法：语言模型和Viterbi算法。<br>
## 二、相关概念介绍
### 1、词性标注
词性标注（Part-Of-Speech tagging, POS tagging）也被称为语法标注（grammatical tagging）或词类消疑（word-category disambiguation），是语料库语言学（corpus linguistics）中将语料库内单词的词性按其含义和上下文内容进行标记的文本数据处理技术。
词性标注主要被应用于文本挖掘（text mining）和NLP领域，是各类基于文本的机器学习任务，例如语义分析（semantic analysis）和指代消解（coreference resolution）的预处理步骤。
近年来，在情感分析任务中也有应用。
### 2、语言模型
语言模型是根据语言客观事实而进行的语言抽象数学建模，是一种对应关系。语言模型本质上是通过计算一个句子的概率大小，整句的概率就是各个词出现概率的乘积，以此来判断出现的语句是否合理，概率高的语句比概率低的语句更为合理。经典的统计语言模型就是N-gram语言模型。
### 3、Viterbi算法
维特比算法是一种动态规划算法，用于寻找最有可能产生观测事件序列的-维特比路径-隐含状态序列，提供了一种有效的计算方法来分析隐马尔科夫模型的观察序列，并捕获最可能的隐藏状态序列。它利用递归减少计算量，并使用整个序列的上下文来做判断，从而对包含“噪音”的序列也能进行良好的分析。例如在统计句法分析中动态规划算法可以被用于发现最可能的上下文无关的派生(解析)的字符串，有时被称为“维特比分析”。 
在使用时，维特比算法对于网格中的每一个单元(cell)都计算一个局部概率，同时包括一个反向指针用来指示最可能的到达该单元的路径。当完成整个计算过程后，首先在终止时刻找到最可能的状态，然后通过反向指针回溯到t=1时刻，这样回溯路径上的状态序列就是最可能的隐藏状态序列了。
## 三、代码相关说明
### 1、使用如下公式实现对句子中的词进行最合适的词性标注：
代码中的参数：<br>
A：是一个N行M列的矩阵，N代表词性的数量，M代表词库里词的数量；<br>
pi：是一个向量，长度为N，每个词性出现在句子中第一个位置的概率；<br>
B：是一个N行N列的状态转移矩阵。<br>
### 2、首先需要对数据集进行划分，将“.”作为句子划分的标志，代码使用每个单词及其词性的位置id，所以要进行映射。<br>
```
tag2id, id2tag = {}, {}
word2id, id2word = {}, {}

for line in open('traindata.txt'):
    items = line.split('/')
word, tag = items[0], items[1].rstrip()#抽取每一行里的单词和词性

    if word not in word2id:
        word2id[word] = len(word2id)
        id2word[len(id2word)] = word
    if tag not in tag2id:
        tag2id[tag] = len(tag2id)
        id2tag[len(id2tag)] = tag

M = len(word2id)  # M: 词典的大小，num of words in dictionary
N = len(tag2id)   # N: 词性的种类个数，num of tags in tag set
```
### 3、构建 pi, A, B
```
pi = np.zeros(N)  # 每个词性出现在句子中第一个位置的概率,pi[i]: tag i出现在句子中第一个位置的概率<br>
A = np.zeros((N, M)) # A[i][j]: 给定tag i, 出现单词j的概率<br>
B = np.zeros((N,N))  # B[i][j]: 之前的状态是i, 之后转换成转态j的概率<br>
```
### 4、计算模型参数
```
prev_tag = ""
for line in open('traindata.txt'):
    items = line.split('/')
    wordId, tagId = word2id[items[0]], tag2id[items[1].rstrip()]
    if prev_tag == "":  # 这意味着是句子的开始
        pi[tagId] += 1
        A[tagId][wordId] += 1
    else:  # 如果不是句子的开头
        A[tagId][wordId] += 1
        B[tag2id[prev_tag]][tagId] += 1
    
    if items[0] == ".":
        prev_tag = ""
    else:
        prev_tag = items[1].rstrip()

# normalize
pi = pi/sum(pi)
for i in range(N):
    A[i] /= sum(A[i])
B[i] /= sum(B[i])
```
### 5、使用Viterbi算法
```
def viterbi(x, pi, A, B):
    """
    x: user input string/sentence: x: "I like playing soccer"
    pi: initial probability of tags
    A: 给定tag, 每个单词出现的概率
    B: tag之间的转移概率
    """
    x = [word2id[word] for word in x.split(" ")]  # x: [4521, 412, 542 ..]
    T = len(x)
    
    dp = np.zeros((T,N))  # dp[i][j]: w1...wi, 假设wi的tag是第j个tag
    ptr = np.array([[0 for x in range(N)] for y in range(T)] ) # T*N
    # TODO: ptr = np.zeros((T,N), dtype=int)
    
    for j in range(N): # basecase for DP算法
        dp[0][j] = log(pi[j]) + log(A[j][x[0]])
    
    for i in range(1,T): # 每个单词
        for j in range(N):  # 每个词性
            # TODO: 以下几行代码可以写成一行（vectorize的操作， 会使得效率变高）
            dp[i][j] = -9999999
            for k in range(N): # 从每一个k可以到达j
                score = dp[i-1][k] + log(B[k][j]) + log(A[j][x[i]])
                if score > dp[i][j]:
                    dp[i][j] = score
                    ptr[i][j] = k
    
    # decoding: 把最好的tag sequence 打印出来
    best_seq = [0]*T  # best_seq = [1,5,2,23,4,...]  
    # step1: 找出对应于最后一个单词的词性
    best_seq[T-1] = np.argmax(dp[T-1])
    
    # step2: 通过从后到前的循环来依次求出每个单词的词性
    for i in range(T-2, -1, -1): # T-2, T-1,... 1, 0
        best_seq[i] = ptr[i+1][best_seq[i+1]]
        
    # 到目前为止, best_seq存放了对应于x的词性序列
    for i in range(len(best_seq)):
        print(id2tag[best_seq[i]])
```
## 四、实验结果
### 1、先给出数据集里的一个句子，验证词性标注是否准确：
```
x = "Social Security number , passport number and details about the services provided for the payment"
```
结果：<br>
NNP<br>
NNP<br>
NN<br>
,<br>
NN<br>
NN<br>
CC<br>
NNS<br>
IN<br>
DT<br>
NNS<br>
VBN<br>
IN<br>
DT<br>
NN<br>
对照之后发现是正确的。<br>
### 2、给出一个非数据集里的句子进行词性标注：
```
x = "The class is very interesting"
```
结果：<br>
DT<br>
NN<br>
VBZ<br>
RB<br>
JJ<br>
结果显示也是正确的。
## 五、课程心得
由于疫情的出现，这学期的Python与数据挖掘课程是在家线上进行，虽然隔着屏幕，但是依然能够感受到老师讲课的热情和专业。
我自知基础薄弱，  代码能力不强，所以在老师讲解的时候尽力去听，有时候跟着老师敲代码，当然很多时候听不大懂，但也不是一无所获。我的研究方向代码的实现需要用到python，
虽然课程马上结束了，但是对python的学习不能停止。在此非常感谢王老师每节课的耐心讲解，让我对python的认知不再仅停留在语法规则上。
希望自己可以更努力些，提高编程能力。
