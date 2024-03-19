import cv2
face_cascade=cv2.CascadeClassifier('opencv/face_detection/lbpcascade_frontalface_improved.xml')
#opencv\face_detection\haarcascade_profileface.xml
#opencv\face_detection\lbpcascade_frontalface_improved.xml

def print_hello():
    print('hello')

def face_detect(img):
    '''ths function detects faces in an image'''
    #convert image to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #detect faces
    faces=face_cascade.detectMultiScale(gray,1.1,2)   #image, scale factor, min neighbors

    #put rectangle around the faces
    count=0
    for (x,y,w,h) in faces:
        count+=1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)     #image, start point, end point, color(BGR), thickness
    return img,count

def callibarate(img):
    '''this function will calibrate the image'''
    #convert image to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    a=1.1
    b=1
    #iterate over 6 times for better scale factor and min neighbors
    for j in range(1,6):
        a=1.1
        for i in range(1,6):
            
            faces=face_cascade.detectMultiScale(gray,a,b)   #image, scale factor, min neighbors

            #put rectangle around the faces
            
            count=0
            for (x,y,w,h) in faces:
                count+=1
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)     #image, start point, end point, color(BGR), thickness
            #print to file.txt
            
            print('Number of faces detected: ',count,'scale factor: ',a,'min neighbors: ',b)
            a+=.1
        b+=1
    
def main():
    img=cv2.imread('opencv/face_detection/jupitar.jpg')
    #show image by 500/500 pixels
    img=cv2.resize(img,(500,500))
    # callibarate(img)
    res_img,count=face_detect(img)
    cv2.imshow('image',res_img)
    #wait for key press
    cv2.waitKey(0)

    print('Number of faces detected: ',count)

# main()
