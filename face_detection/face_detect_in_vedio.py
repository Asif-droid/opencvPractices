import cv2 as cv
import face_detection 
# im=cv.imread('images/image05.jpg')
# cv.imshow('book',im)
# cv.waitKey(0)

#reading videos
# face_detection.print_hello()

def rescale(frame,scale):  #resizing frame
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)

    return cv.resize(frame,dim, interpolation=cv.INTER_AREA)



capture=cv.VideoCapture(0)

count=0
while True:
    isTrue, frame = capture.read()
    farme_res=rescale(frame,.75)
    farme_res=cv.rotate(farme_res,cv.cv2.ROTATE_180)
    detc_farme,count=face_detection.face_detect(frame)
    cv.imshow('cam',detc_farme)
    cv.imshow('cam2',farme_res)
    if cv.waitKey(2)== ord('x'):   #wait for 2ms and if x is pressed then break
        break

print('Number of faces detected: ',count)
capture.release()
cv.destroyAllWindows()



