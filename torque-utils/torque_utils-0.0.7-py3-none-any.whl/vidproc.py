''' Video processing routines - vidproc
        developed by Victor Cossich (victor.cossich@gmail.com) and Conrado Torres (conradotl@gmail.com)
	for muscle architecture muasurement. Email us if you want. ;)

	you need numpy,pandas,matplotlib,scipy,cv2,moviepy and to run this module.
'''


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import moviepy.editor
import cv2
import torque_utils.sigproc as sigproc
from scipy import signal as sig
from scipy.io import wavfile

def calibrate(video_file,orientation='vertical',known_dist=10):
    '''
    Zoom in the region of the calibration object, press any button and click in the extremities of the calibration onject.
    video_file = cv2.video object or video image for calibration
    orientation(optional) = orientation of the calibration object ('vertical' ou 'horizontal'), default is 'vertical'
    known_dist(optional) = size of the calibration object in the desired unit, default is 10
    return: correction factor for convert pixel in known_dist units
    '''
    # if the video_file is a string, hold video in the a cv2.VideoCapture object 
    if type(video_file) == str:
        cap = cv2.VideoCapture(video_file)
    # if video_file is not string, assume to be a cv2.VideoCapture object
    else:
        cap = video_file
    # select the first frame and print it
    cap.set(1,0)
    ret, frame = cap.read()
    plt.imshow(frame)
    plt.title('zoom in, press any button and click on the boundaries of the calibrarion object')
    # Wait for a button press to enable ginput
    zoom_ready=False
    while not zoom_ready:
        zoom_ready=plt.waitforbuttonpress()
    # hold the points for calibration and close the image
    p0,p1 = plt.ginput(2,timeout=0)
    plt.close()
    # calculate the point distance in the passed orientation    
    if orientation == 'vertical':
        # distance of the vertical(y) coordinates
        dist_p=abs(p0[1]-p1[1])
    elif orientation == 'horizontal':
        # distance of the horizontal(x) coordinates
        dist_p=abs(p0[0]-p1[0])
   # calculate the correction factor 
    correction_factor=known_dist/dist_p
    
    return correction_factor

############################################################################### 
    
def MT(video_file,correction_factor,skip=5,explicit=False):
    '''
    calculate the muscle thickness (MT) by the average distance between aponeurosis. in each frame, zoom in the muscle area 
    , press any button and the click in the superficial and deep aponeurosis, respectively, three times
    video_file = cv2.video object or video image for muscle thickness measurement
    correction_factor = correction factor for convert pixel in a given size unit
    skip(optional) = frames skipped between analyzed images, default is 5
    explicit(optional) = shows the previous clicks, default is False
    return: list with muscle thickness (MT)
    '''
    # if the video_file is a string, hold video in the a cv2.VideoCapture object 
    if type(video_file) == str:
        cap = cv2.VideoCapture(video_file)
    # if video_file is not string, assume to be a cv2.VideoCapture object
    else:
        cap = video_file
    # obtains the frame number
    n_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # make a list to add the MT values
    mt=[]
    # iterate ver the frames
    for i in range(0,n_frames,skip):
        # set the frame
        cap.set(1,i)
        ret, frame = cap.read()
        # plot the frame
        plt.imshow(frame)
        plt.draw()        
        # creates the text for title
        mensage='image ' + str( int(i/skip)+1 ) + ' of ' + str( int(n_frames/skip+1))
        plt.title(mensage)
        # Wait for a button press to enable ginput
        zoom_ready=False
        while not zoom_ready:
            zoom_ready=plt.waitforbuttonpress()
        # hold the pairs of points
        a1,a2,b1,b2,c1,c2 = plt.ginput(6,timeout=0)
        # make a list to add the distances in each frame
        mt_frame=[]
        # calculate the distance of each pair of points for each frame and convert to desired unit
        for i in [(a1[1],a2[1]),(b1[1],b2[1]),(c1[1],c2[1])]:
            mt_temp=abs(i[0]-i[1])*correction_factor
            mt_frame.append(mt_temp)
        # add the mean of distances in the MT list
        mt.append(np.mean(mt_temp))
        # plot the actual clicks
        if explicit:
            for i in (a1,a2,b1,b2,c1,c2):
                plt.plot(i[0],i[1],'r.',alpha=.2)
    # close the image at the end of iteration
    plt.close()
    
    return mt

###############################################################################

def FA(video_file,skip=5,correction_factor=0.2,explicit=False):
    '''    
    calculate the fascicle angle (FA) by the average angle between a fascicle and the aponeurosis. in each frame, zoom in the muscle area 
    , press any button and the click in the midle of the fascicle, in the attachment site and then in the aponeurosis in the region bellow 
    the middle of the fascicle. This procedure will be repeated three times per frame.
    video_file = cv2.video object or video image for fascicle angle measurement
    skip(optional) = frames skipped between analyzed images, default is 5
    explicit(optional) = shows the previous clicks, default is False
    return: list with fascicle angles (FA)
    '''
    # if the video_file is a string, hold video in the a cv2.VideoCapture object 
    if type(video_file) == str:
        cap = cv2.VideoCapture(video_file)
    # if video_file is not string, assume to be a cv2.VideoCapture object
    else:
        cap = video_file
    #obtains the frame number
    n_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # make a list to add the FA values
    fa=[]
    # iterate ver the frames
    for i in range(0,n_frames,skip):
        # set the frame
        cap.set(1,i)
        ret, frame = cap.read()
        # plot the frame
        plt.imshow(frame)
        plt.draw()
        # creates the text for title
        mensage='imagem ' + str( int(i/skip)+1 ) + ' de ' + str( int(n_frames/skip+1))
        plt.title(mensage)
        # make a list to add the values in each frame
        fa_frame=[]
        # repeat the measurement 3 times
        for i in range(3):
            # Wait for a button press to enable ginput
            zoom_ready=False
            while not zoom_ready:
                zoom_ready=plt.waitforbuttonpress()
            # hold the points
            a,b,c = plt.ginput(3,timeout=0)
            # cast the tuples into np.array
            a,b,c = np.array(a),np.array(b),np.array(c)
            # create vectors with origins in the attachment site
            fas = a - b
            apo = c - b
            # calculate cosine of the angle between vectors
            cosine_angle = np.dot(fas, apo) / (np.linalg.norm(fas) * np.linalg.norm(apo))
            # obtains the angle based on the cosine
            angle = np.degrees(np.arccos(cosine_angle))
            fa_frame.append(angle)
            # plot the actual clicks
            if explicit:
                for i in (a,b,c):
                    plt.plot(i[0],i[1],'r.',alpha=.2)
        # add the mean of FA in the list
        fa.append(np.mean(fa_frame))
    # close the image at the end of iteration
    plt.close()
    
    return fa

###############################################################################
    
def FL (MT,FA):
    '''
    Calculates fascicle lenght (FL) as the muscle thickness (MT) divided by the sine of fascicle angle (FA)
    MT = pd.series or list with muscle thickness values
    FA = pd.series or list with fascicle angle values
    return: pd.series with the fascicle lenght (FL) values
    '''
    # cast the input into a pd.series
    MT = pd.series(MT)
    FA = pd.series(FA)
    #calculate FL
    FL = MT /np.sin(FA*np.pi/180)
    
    return FL

###############################################################################
def video_sync(video_file_patch,save=False):
    '''
    trimms the video clip based on a spike in the audio signal and save at the same dic with the "_autrim" tag. See torque_signal.onset() help
    video_file_patch = patch of the video file 
    return: time of audio spike onset in s
    '''
    # hold the video in a moviepy.VideoFileClip object
    vid=moviepy.editor.VideoFileClip(video_file_patch)
    # hold the audio in a moviepy.audioFileClip object
    audio=vid.audio
    # create a temporary audio file
    audio.write_audiofile('_temp_.wav')
    # close moviepy objects
    vid.close()
    audio.close()
    # obtain sample_rate and the audio signal as a np.array
    sample_rate, wav_signal = wavfile.read('_temp_.wav')
    # remove the temporary file
    os.remove('_temp_.wav')
    # convert np.array in pd.DataFrame and calculate the mean of the audio channels
    wav_signal=pd.DataFrame(wav_signal)
    wav_signal['signal']=abs((wav_signal[0]+wav_signal[1])/2)
    # set the filters parameters
    b,a = sig.butter(N = 2, Wn = 50/(sample_rate/2), btype = 'lowpass', output = 'ba')
    # apply the filter
    wav_signal['signal'] = sig.filtfilt(b,a,wav_signal['signal'])
    # defines audio spike onset and close the image 
    onset=sigproc.onset(torque_signal=wav_signal['signal'], sf=sample_rate, 
                   method='baseline_noise', trigger=3, passive_correction=False,plot=False)
    plt.close()
    #calculate the time of audio onset
    t_onset=onset/sample_rate
    # save the file if indicated    
    if save:
        # hold the video file in a cv2.VideoCapture object
        cap = cv2.VideoCapture(video_file_patch)
        # defines the uotput patch
        output=video_file_patch[:-4]+'_audtrim.avi'
        # build a cv2.VideoWriter object
        writer=cv2.VideoWriter(output,cv2.VideoWriter_fourcc('I','4','2','0'),cap.get(cv2.CAP_PROP_FPS),
                   (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) )
        # obtain the original frame count
        n_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # iterate over the frames from audio onset to the end of original video writing in the output
        for i in range(int(t_onset*cap.get(cv2.CAP_PROP_FPS)),n_frames):
            cap.set(1,i)
            ret, frame = cap.read()
            writer.write(frame)

    return t_onset      
    
###############################################################################
    
    
    
    
    
    
    
    
    
    
    