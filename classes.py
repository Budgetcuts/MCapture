import cv2, time, pandas

class Cam:

    def __init__(self,curr,conn,id,port):
        self.curr = False 
        self.conn = False 

    def connect(self):
        self.conn = False 

    def isConnected(self):
        return self.conn

    def setId(self, num):
        self.id = num 

    def setPort(self, port):
        self.port = port

    def setDetect(self):

        static_back = None
        
        motion_list = [ None, None ]
        
        time = []
        
        
        df = pandas.DataFrame(columns = ["Start", "End"])
        

        video = cv2.VideoCapture(0)
        check, frame = video.read()
    
        motion = 0

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
       
        if static_back is None:
            static_back = gray
            continue
    
        diff_frame = cv2.absdiff(static_back, gray)
    
       
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    
        cnts,_ = cv2.findContours(thresh_frame.copy(), 
                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            motion = 1
    
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
        motion_list.append(motion)
    
        motion_list = motion_list[-2:]