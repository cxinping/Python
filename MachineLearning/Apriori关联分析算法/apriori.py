def  loadDataSet():  
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]  
  
def createC1(dataSet):                  #构建所有候选项集的集合  
    C1 = []  
    for transaction in dataSet:  
        for item in transaction:  
            if not [item] in C1:  
                C1.append([item])       #C1添加的是列表，对于每一项进行添加，{1},{3},{4},{2},{5}  
    C1.sort()  
    return map(frozenset, C1)           #使用frozenset，被“冰冻”的集合，为后续建立字典key-value使用。  
  
def scanD(D,Ck,minSupport):             #由候选项集生成符合最小支持度的项集L。参数分别为数据集、候选项集列表，最小支持度  
    ssCnt = {}  
    for tid in D:                       #对于数据集里的每一条记录  
        for can in Ck:                  #每个候选项集can  
            if can.issubset(tid):       #若是候选集can是作为记录的子集，那么其值+1,对其计数  
                if not ssCnt.has_key(can):#ssCnt[can] = ssCnt.get(can,0)+1一句可破，没有的时候为0,加上1,有的时候用get取出，加1  
                    ssCnt[can] = 1  
                else:  
                    ssCnt[can] +=1  
    numItems = float(len(D))    
    retList  = []  
    supportData = {}  
    for key in ssCnt:  
        support = ssCnt[key]/numItems   #除以总的记录条数，即为其支持度  
        if support >= minSupport:  
            retList.insert(0,key)       #超过最小支持度的项集，将其记录下来。  
        supportData[key] = support  
    return retList, supportData  