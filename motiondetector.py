import cv2

video=cv2.VideoCapture(0)
#now we will capture two frames
ret,frame1=video.read()
ret,frame2=video.read()

while video.isOpened():
    #calculate the difference of image
    diff=cv2.absdiff(frame1,frame2)
    #will convert to gray scale image
    grey=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    #for more accuracy we will convert to gaussian blur image
    blur=cv2.GaussianBlur(grey,(5,5),0) 
    #will apply the thershold method
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #we will dilate this image 
    dilated=cv2.dilate(thresh,(5,5),iterations=3)
    #contours
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #using the for loop and boundingrect method we will get x,y,w,h
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        #now we will construct a rectangle
        if cv2.contourArea(contour)<700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Status:{}".format('movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    cv2.imshow("win",frame1)
    frame1=frame2
    ret,frame2=video.read()
    if cv2.waitKey(40)==27:
        break

cv2.destroyAllWindows()
video.release()

