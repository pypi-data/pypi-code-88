import tkinter as tk
import vlc
import os 
import sys
import platform
import PIL 
import cv2
import mediapipe as mp
from PIL import Image
from PIL import ImageTk
if sys.version_info[0] < 3:
    import Tkinter as Tk
    from Tkinter import *
    from Tkinter.filedialog import askopenfilename
else:
    import tkinter as Tk
    from tkinter import *
    from tkinter.filedialog import askopenfilename
    from tkinter.messagebox import showinfo
from PIL import Image 
from PIL import ImageTk
from os.path import basename, expanduser, isfile, join as joined
from pathlib import Path
import time
from tkinter import messagebox
import tkinter.font as font 

class App1:
    def __init__(self,parent,media,window_title,video_source=0):
        self.window = Toplevel(parent)
        self.window.title(window_title)
        self.video_source = video_source
        self.media = media
        self.vid = MyVideoCapture(self.media,video_source)
        self.canvas = tk.Canvas(self.window, width = self.vid.WIDTH, height = self.vid.HEIGHT)
        self.canvas.pack()
        self.delay = 15
        self.update()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def on_closing(self):
        self.window.destroy()
        del self.vid
        cv2.destroyAllWindows()

        #uncomment these 4 lines for a message window
        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #     self.window.destroy()
        #     del self.vid
        #     cv2.destroyAllWindows()

    def update(self):
     # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
 
        self.window.after(self.delay, self.update)


class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 9, (0, 255, 255), cv2.FILLED)

        return lmList

class MyVideoCapture:
    def __init__(self,media,video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        self.media = media
        if not self.vid.isOpened():
            raise ValueError("unable to open video source",video_source)

        self.WIDTH = 640
        self.HEIGHT = 480
        self.max_vol=150
        self.min_vol=0
        self.tipids = [4,8,12,16,20]
        self.detector = handDetector(detectionCon=0.7)
        self.previoustime = time.time()
        self.vid.set(3,self.WIDTH)
        self.vid.set(4,self.HEIGHT)
        # self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)


    def get_frame(self):
        if self.vid.isOpened():
            ret,frame = self.vid.read()
            if ret:
                cv2.rectangle(frame,(5,5),(270,270),color=(255,22,0),thickness=2)
                cv2.putText(frame,"Perform the gesture inside the blue box",(70,430),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2,cv2.LINE_AA)
                detection_region = frame[5:270,5:270]
                detection_region = self.detector.findHands(detection_region)
                points_list = self.detector.findPosition(detection_region,draw=False)
                if len(points_list)!=0:
                    fingers = []
                    #for thumb
                    if points_list[self.tipids[0]][1] > points_list[self.tipids[0]-1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                    for id in range(1,5):
                        if points_list[self.tipids[id]][2] < points_list[self.tipids[id]-2][2]:
                            fingers.append(1)
                        else:
                            fingers.append(0)
                    # print(fingers)
                    total_fingers = fingers.count(1)
                    # print(total_fingers)
                    # print(points_list)

                    #seek forward
                    if total_fingers == 2 and points_list[8][2] < points_list[6][2] and points_list[12][2] < points_list[10][2]:
                        # print('forward')
                        video_position = vlc.libvlc_media_player_get_position(self.media)
                        if video_position == 1:
                            vlc.libvlc_media_player_set_position(self.media,video_position-0.01)
                        if video_position != -1:
                            vlc.libvlc_media_player_set_position(self.media,video_position+0.001)

                    #seek back
                    elif total_fingers == 3 and points_list[8][2] < points_list[6][2] and points_list[12][2] < points_list[10][2] and points_list[16][2] < points_list[14][2]:
                        # print('backward')
                        video_position = vlc.libvlc_media_player_get_position(self.media)
                        if video_position == 0:
                            vlc.libvlc_media_player_set_position(self.media,video_position+0.01)
                        if video_position != -1:
                            vlc.libvlc_media_player_set_position(self.media,video_position-0.001)

                    #play-pause
                    elif total_fingers == 5 and  points_list[8][2] < points_list[6][2] and points_list[12][2] < points_list[10][2] and points_list[16][2] < points_list[14][2] and points_list[20][2] < points_list[18][2]:
                        currenttime = time.time()
                        # if currenttime-self.previoustime>3:
                        #     print('play/pause')
                        if currenttime-self.previoustime>3:
                            if vlc.libvlc_media_player_is_playing(self.media) == 1:
                                self.media.pause()
                            elif vlc.libvlc_media_player_is_playing(self.media) == 0:
                                self.media.play()
                        self.previoustime = currenttime

                    elif total_fingers == 2 and points_list[10][2] < points_list[12][2] and points_list[14][2] < points_list[16][2] and points_list[18][2] < points_list[20][2]:
                        cv2.line(frame, (points_list[8][1],points_list[8][2]),(points_list[4][1],points_list[4][2]),(0,255,255),10)
                        cv2.circle(frame,(points_list[8][1],points_list[8][2]),radius=8,color=(0,255,255),thickness=-1)
                        cv2.circle(frame,(points_list[4][1],points_list[4][2]),radius=8,color=(0,255,255),thickness=-1)
                        distance = math.sqrt((points_list[8][1]-points_list[4][1])**2+(points_list[8][2]-points_list[4][2])**2)
                        vol = int(np.interp(distance,[12,175],[self.min_vol,self.max_vol]))
                        # print(vol)
                        self.media.audio_set_volume(vol)

                    elif total_fingers == 0 and points_list[6][2] < points_list[8][2] and points_list[10][2] < points_list[12][2] and points_list[14][2] < points_list[16][2] and points_list[4][1] < points_list[3][1]:
                        currenttime = time.time()
                        # if currenttime-self.previoustime>3:
                        #     print('mute')
                        if currenttime-self.previoustime>3:
                            if vlc.libvlc_audio_get_mute(self.media):
                                vlc.libvlc_audio_set_mute(self.media,False)
                            else:
                                vlc.libvlc_audio_set_mute(self.media,True)
                        self.previoustime = currenttime
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret,None)
        else:
            return (ret,None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


class MenuBar(Menu,tk.Button,tk.Scale):
    def __init__(self,root):
        tk.Menu.__init__(self,root)
        self.parent = root
        file = Menu(self,tearoff = False)
        file.add_command(label="Open",command=self.OnOpen)
        if platform.system() == 'Linux':
            file.add_command(label="Stop",command=self.stop_file)
        file.add_command(label="Exit",command=self.close)

        self.add_cascade(label="File",menu=file)

        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.frame = tk.Frame(self.parent,width=self.width,height=self.height,bg='black')
        self.frame.pack()
        self.button_font = font.Font(family='Helvetica', size=10, weight='bold')
        #buttons 
        #play_button
        self.play_button = tk.Button(self.parent,text='Play',font=self.button_font,bg='white',command=self.play_video)
        self.play_button.place(relx=0.335,rely=0.9,relwidth=0.08,relheight=0.09)
        #pause button
        self.pause_button = tk.Button(self.parent,text='Pause',font=self.button_font,bg='white',command=self.pause_video)
        self.pause_button.place(relx=0.63,rely=0.9,relwidth=0.1,relheight=0.09)
        #forward button
        self.forward_button = tk.Button(self.parent,text='Forward',font=self.button_font,bg='white',command=self.go_forward)
        self.forward_button.place(relx=0.525,rely=0.9,relwidth=0.1,relheight=0.09)
        #backward_button
        self.backward_button = tk.Button(self.parent,text='Rewind',font=self.button_font,bg='white',command=self.go_back)
        self.backward_button.place(relx=0.42,rely=0.9,relwidth=0.1,relheight=0.09)
        #gesture_button
        self.gesture_button =  tk.Button(self.parent,text='Gesture Mode',font=self.button_font,bg='white',command=self.gesture_recognise)
        self.gesture_button.place(relx=0.2,rely=0.9,relwidth=0.13,relheight=0.09)

        self.volume_scale = tk.Scale(self.parent,from_=0,to=150,orient=tk.HORIZONTAL,width=24,length=150,command=self.set_volume)
        self.volume_scale.place(relx=0.735,rely=0.9)

    def OnOpen(self):
        video = askopenfilename(initialdir = Path(expanduser("~")),
            title = "Choose a video file",
            filetypes = (("all files","*.*"),
                ("mp4 files", "*.mp4"),
                ("mov files", "*.mov")))

        self.Play(video)

    def stop_file(self):
        if vlc.libvlc_media_player_is_playing(self.media):
            self.media.stop()

    def Play(self,video):
        self.media = vlc.MediaPlayer(video)
        # if platform.system() == 'Linux':
        #     self.media.set_xwindow(self.parent.winfo_id())
        # if platform.system() == 'Windows':
        self.media.set_hwnd(self.frame.winfo_id())
        self.media.play()
        self.volume_scale.set(vlc.libvlc_audio_get_volume(self.media))
        
            
    def pause_video(self):
        if vlc.libvlc_media_player_is_playing(self.media):
            self.media.pause()

    def play_video(self):
        if vlc.libvlc_media_player_is_playing(self.media)==False:
            self.media.play()

    def go_back(self):
        video_position = vlc.libvlc_media_player_get_position(self.media)
        if video_position == 0:
            vlc.libvlc_media_player_set_position(self.media,video_position+0.01)
        if video_position!=-1:
            vlc.libvlc_media_player_set_position(self.media,video_position-0.001)

    def go_forward(self):
        video_position = vlc.libvlc_media_player_get_position(self.media)
        if video_position == 1:
            vlc.libvlc_media_player_set_position(self.media,video_position-0.01)
        if video_position!=-1:
            vlc.libvlc_media_player_set_position(self.media,video_position+0.001)

    # def newwindow(self):
    #     newwin = Toplevel(self.parent)
    #     newwin.title("new")
    #     newwin.geometry("200x200")

    def gesture_recognise(self):
        '''
        start gesture recognition, turn button color to green
        if button is pressed again stop gesture recognition window, turn button color to red
        '''

        # wt.detect_gestures(self.media)
        # if self.gesture_button.cget('bg') == 'red':
        #     self.gesture_button.configure(bg ='green')
        # elif self.gesture_button.cget('bg') =='green':
        #     self.gesture_button.configure(bg = 'red')

        #testing

        App1(self.parent,self.media,"Gesture Window")
        

    def close(self):
        self.exit()

    def set_volume(self,_=None):
        self.media.audio_set_volume(self.volume_scale.get())

    def exit(self):
        exit()

class FrameBox(tk.Frame):
    def __init__(self,root):
        super().__init__(root)

        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.frame = tk.Frame(root,width=self.width,height=self.height,bg='black')
        self.frame.pack()

class App(tk.Tk):
    def __init__(self):
        super().__init__()


        #configure root window
        self.title('Video Player')
        self.minsize(800,600)
        self.maxsize(800,600)
        self.resizable(False,False)
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    def set_icon(self,path):
        player_icon = PhotoImage(file=path)
        self.iconphoto(False,player_icon)


def main():
    '''
    calls the App class and creates an object 
    object has control over the video
    select the video, automatically starts playing
    click the gesture mode to go into gesture based control mode
    '''
    app = App()
    # app.set_icon('icon_images/icon.png')
    # frame = FrameBox(app)
    file_menu = MenuBar(app)
    app.config(menu=file_menu)
    # app.on_closing()
    app.mainloop()

if __name__ == '__main__':
    main()