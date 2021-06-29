import cv2
import time
def record(camSerial=0,showVedio=True,width = 640,height = 480, maxDuration=5,fourcc_code= 'XVID'):
    '''
    record(camSerial=0,showVedio=True,width = 640,height = 480,maxDuration=5,fourcc_code= 'XVID')
        camSerial=0
        showVedio=True
        width = 640,height = 480
        fourcc_code= 'XVID'
        maxDuration=5 ==> force stop opened clip after 5 minute recording....
    '''
    fourcc = cv2.VideoWriter_fourcc(*fourcc_code)    
    cap = cv2.VideoCapture(camSerial)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    ret, frame = cap.read()
    state =0
    if showVedio: cv2.startWindowThread()
    stime = 0
    while(cap.isOpened()):
        if cv2.waitKey(10) == 27: break
        if cv2.waitKey(1) & 0xFF == ord('q'): break
        ret, frame = cap.read()# 讀取一幅影格
        if ret == False:break # 若讀取至影片結尾，則跳出
        if state == 0:
            filename = time.strftime("%Y%m%d%H%M%S.mp4")
            out = cv2.VideoWriter(filename, fourcc, 20.0, (width,  height))
            print(filename,'opened..')
            stime=time.time()
            state = 1
        elif state == 1:
            if (time.time()-stime)/60>maxDuration: state=2
            out.write(frame)
        elif state == 2:
            out.release();state = 0;print(filename,'closed..')
    
        if showVedio:
            frame=cv2.imshow('Record while there is different,esc to exit...', frame)
    
    print('End of recording process')
    out.release()
    cap.release()
    cv2.destroyAllWindows()

def recordMove(camSerial=0,showVedio=True,width = 640,height = 480, maxDuration=5,fourcc_code= 'XVID' ,TH = 15000,showPower=False):
    '''
    recordMove(camSerial=0,showVedio=True,width = 640,height = 480,maxDuration=5,fourcc_code= 'XVID' ,TH = 15000,showPower=False)
        camSerial=0
        showVedio=True
        width = 640,height = 480
        fourcc_code= 'XVID'
        maxDuration=5 ==> force stop opened clip after 5 minute recording....
        TH = 15000 ==> record while different power bigger than 15000 and stop recording while different power smaller than 15000/2
        showPower=False
    '''
    fourcc = cv2.VideoWriter_fourcc(*fourcc_code)    
    #COUNT = 1
    # 開啟網路攝影機
    cap = cv2.VideoCapture(camSerial)
    # 設定擷取影像的尺寸大小
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    # 初始化平均影像
    ret, frame = cap.read()
    avg = cv2.blur(frame, (4, 4))
    avg_float = np.float32(avg)
    state =0
    if showVedio: cv2.startWindowThread()
    stime = 0
    while(cap.isOpened()):
        if cv2.waitKey(10) == 27: break
        if cv2.waitKey(1) & 0xFF == ord('q'): break
        ret, frame = cap.read()# 讀取一幅影格
        if ret == False:break # 若讀取至影片結尾，則跳出
        blur = cv2.blur(frame, (4, 4))# 模糊處理
        diff = cv2.absdiff(avg, blur)# 計算目前影格與平均影像的差異值
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)# 將圖片轉為灰階
        # 篩選出變動程度大於門檻值的區域
        ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
        kernel = np.ones((5, 5), np.uint8)# 使用型態轉換函數去除雜訊
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
        # 更新平均影像
        cv2.accumulateWeighted(blur, avg_float, 0.01)
        avg = cv2.convertScaleAbs(avg_float)
        power=sum(sum(thresh))
        if showPower: print(state,power)
        if state == 0:
            if power>TH:
                filename = time.strftime("%Y%m%d%H%M%S.mp4")
                out = cv2.VideoWriter(filename, fourcc, 20.0, (width,  height))
                print(filename,'opened..')
                stime=time.time()
                state = 1
        elif state == 1:
            if (time.time()-stime)/60>maxDuration or power < TH/2: state=2
            out.write(frame)
        elif state == 2:
            out.release();state = 0;print(filename,'closed..')
            
        if showVedio:
            frame=cv2.imshow('Record while there is different,esc to exit...', frame)
        
    print('End of recording process')
    cap.release()
    out.release()
    cv2.destroyAllWindows()

#record(maxDuration=0.1)
