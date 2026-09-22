import cv2 as cv

cap = cv.VideoCapture(0)
tracker = cv.legacy.TrackerMOSSE_create()
tracking = False 

cv.namedWindow("Tracking",cv.WINDOW_NORMAL)
cv.resizeWindow("Tracking",1000,700)

def draw(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]), int(bbox[2]),int (bbox[3])
    cv.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv.putText(frame,"Tracking", (75,50),cv.FONT_HERSHEY_PLAIN,0.9,(0,255,0),2)

    
while True:
    ret , frame = cap.read()
    
    if tracking ==True:
        success , bbox = tracker.update (frame)
         
        if success:
            draw(frame, bbox)
        else:
            cv.putText(frame,"Lost", (75,75),cv.FONT_HERSHEY_PLAIN,0.9,(255,255,0),2)

    cv.imshow("Tracking",frame)

    k = cv.waitKey(1) & 0xff

    if  k ==ord('q') or k == ord('Q'):
        break
    elif k ==ord('s') or k == ord ('S'):
        tracking = True
        bbox = cv.selectROI('select', frame , False)
        tracker.init(frame,bbox)
        cv.destroyWindow('select')
         

cap.release()
cv.destroyAllWindows()

