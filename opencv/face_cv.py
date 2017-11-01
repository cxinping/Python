import cv2
#读取图片
img = cv2.imread('cv1.jpg')
#转化为灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#特征级联表
face_cascade = cv2.CascadeClassifier(r'G:\java_tool\cv_data\haarcascades\haarcascade_frontalface_default.xml')
# print(type(face_cascade))    #<class 'cv2.CascadeClassifier'>
#多尺寸检测，返回列表  # print(face)     #[[1947 2275  374  374]....
face = face_cascade.detectMultiScale(
    gray,1.3,5
)
print('发现{0}个脸'.format(len(face)))
for (x,y,w,h) in face:
    #(图像对象，圆心，半径，颜色，封闭？)
    #cv2.circle(img,((x+x+w)//2,(y+y+h)//2),w//2,(0,255,0),-1)
    cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)
    
#保存图像
cv2.imwrite('14Peoele.jpg',img)
#显示图像
cv2.imshow('gray',img)
#防止闪屏
cv2.waitKey(0)