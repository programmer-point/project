import cv2
#import  castcadeclassifier which ha inbuild function of detecting a face
face_cascade=cv2.CascadeClassifier("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
#it had converted my image in the form of num array
img = cv2.imread("C:\\Users\\Lenovo\\Pictures\\Camera Roll\\image.jpg",1)
#convert the image into gray
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# method to search face coordinate
shapes=face_cascade.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors=5)
#display the rectangle in the image
for x,y,w,h in shapes:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#resized image
resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#it opens the window of image
cv2.imshow("grey", resized)
#how much time we have to open that window if 0then whenevr we click any button widow will disappear
cv2.waitKey(0)

cv2.destroyAllWindows()
