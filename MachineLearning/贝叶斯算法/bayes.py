import numpy as np


def loadDataSet():
    docs = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
            ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
            ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
            ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
            ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
            ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classes = [0,1,0,1,0,1]    # 1为辱骂, 0为否
    return docs, classes

#创建一个带有所有单词的列表
def create_all_words(docs):
    all_words = set([])
    for doc in docs:
        all_words = all_words | set(doc)
    return list(all_words)

# 将句子根据其中的单词转成向量
def create_all_words_counter(all_words, doc):
    all_words_counter = [0] * len(all_words)
    for word in doc:
        if word in all_words:
            all_words_counter[all_words.index(word)] = 1   # 置1，伯努利模型
            #all_words_counter[all_words.index(word)] += 1 # 加1，多项式模型
        else:
            print('word ',word ,'not in dict')
    return all_words_counter


# 计算P(i)和P(w[i]|C[1])和P(w[i]|C[0])，这里有两个技巧
# 一个是开始的分子分母没有全部初始化为0是为了防止其中一个的概率为0导致整体为0，
# 另一个是后面乘用对数防止因为精度问题结果为0
def trainNB0(all_words_counters, classes):
    num_docs = len(all_words_counters)
    num_all_words = len(all_words_counters[0])
    pAbusive = np.sum(classes) / num_docs # 辱骂的先验概率

    pNum = np.ones((2, num_all_words))  # 置1，没有置0，这是一个技巧
    pDenom = np.array([2.0, 2.0])

    for i in range(num_docs):
        pNum[classes[i]] += all_words_counters[i]
        pDenom[classes[i]] += np.sum(all_words_counters[i])

    p0Vec = np.log(pNum[0]) - np.log(pDenom[0])  # 处于精度的考虑，这里使用对数减法！！
    p1Vec = np.log(pNum[1]) - np.log(pDenom[1])
    return p0Vec, p1Vec, pAbusive
   
def classifyNB(all_words_counter, p0Vec, p1Vec, pAbusive):
    p1 = np.sum(all_words_counter * p1Vec) + np.log(pAbusive)    # 乘以辱骂先验概率。与前对应，这里用了对数加！！
    p0 = np.sum(all_words_counter * p0Vec) + np.log(1.0 - pAbusive)
    if p1 > p0:
        return 1 # 分类1：辱骂
    else:
        return 0 # 分类2：否
       

   
if __name__ == '__main__':
    docs, classes = loadDataSet()
    all_words = create_all_words(docs)
    all_words_counters = []
    for doc in docs:
        all_words_counters.append(create_all_words_counter(all_words, doc))
    p0Vec, p1Vec, pAb = trainNB0(np.array(all_words_counters), np.array(classes))
    
    testDoc = ['love', 'my', 'dalmation']
    all_words_counter = np.array(create_all_words_counter(all_words, testDoc))
    print(testDoc, 'classified as: ', classifyNB(all_words_counter, p0Vec, p1Vec, pAb))
    
    testDoc = ['stupid', 'garbage']
    all_words_counter = np.array(create_all_words_counter(all_words, testDoc))
    print(testDoc, 'classified as: ', classifyNB(all_words_counter, p0Vec, p1Vec, pAb))
    