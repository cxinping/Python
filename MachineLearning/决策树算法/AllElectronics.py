from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

# Read in the csv file and put features into list of dict and list of class label
# 载入样本数据
allElectronicsData = open(r'./AllElectronics.csv', 'r')
# 第一行表头
reader = csv.reader(allElectronicsData)
# #headers = reader.next
for row in reader:
    headers = row
    break

print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)

print(featureList)

# Vetorize features
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList) .toarray()

print("dummyX: " + str(dummyX))
print(vec.get_feature_names())

print("labelList: " + str(labelList))

# vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: " + str(dummyY))

# Using decision tree for classification
# clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf: " + str(clf))


# Visualize model
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

#3 dot -Tpdf allElectronicInformationGainOri.dot -o tree.pdf

# oneRowX = dummyX[0, :]
# print("oneRowX: " + str(oneRowX))
#
# newRowX = oneRowX
# newRowX[0] = 1
# newRowX[2] = 0
# print("newRowX: " + str(newRowX))
#
# predictedY = clf.predict([newRowX])
# print("predictedY: " + str(predictedY))


