import youtube_dl, requests
from bgeditor.common.utils import get_dir, download_file,normal_audio
from bgeditor.dao.FFmpeg import create_loop_audio_times
import uuid,json, shutil,os
from moviepy.editor import *
import urllib
def download_audio(url,ext='mp3'):
    file_name = str(uuid.uuid4()) + "." + ext
    rs = get_dir('download') + file_name
    ydl_opts = {
        'outtmpl': rs,
        'format': 'bestaudio/m4a',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return rs
def create_compilation_songs(data, job_id, mf_server):
    #[{"type":3,"url":"","repeat":1}]
    #3: youtube_video
    #7: deezer
    #8: link direct
    arr_songs=data
    file_merg_path = get_dir('coolbg_ffmpeg') + str(uuid.uuid4())
    file_merg = open(file_merg_path, "a")
    final_clip_path = get_dir('coolbg_ffmpeg') + str(uuid.uuid4()) + '-final.mp3'
    cnt_song=0
    try:
        for song in arr_songs:
            try:
                arr_tmp=song['uri'].split(":")
                song['local']=''
                if arr_tmp[0] == "youtube":#youtube
                    song['local']=download_audio(arr_tmp[2])
                if arr_tmp[0] == "direct":#direct
                    tmp=song['uri'].replace("direct:track:","")
                    song['local'] = download_file(tmp)
                if arr_tmp[0] == "deezer":#deezer
                    song_info=requests.get("http://source.automusic.win/deezer/track/get/"+arr_tmp[2], timeout=180).json()
                    song['local']=download_file(song_info['url_128'])
                if arr_tmp[0] == "spotify":  # spotify
                    arr_song_info = requests.get("http://source.automusic.win/spotify/track/get/" + arr_tmp[2], timeout= 180).json()
                    if len(arr_song_info)>0:
                        song_info=arr_song_info[0]
                        song['local'] = download_file(song_info['url_128'])
                if arr_tmp[0] == "automusic" and arr_tmp[1] == "source":
                    arr_song_info = requests.get("http://source.automusic.win/config/f-retrieve/"+arr_tmp[2] +
                                                 f"?jobid={job_id}&mfs={urllib.parse.quote_plus(mf_server)}", timeout= 600).json()
                    for song_info in arr_song_info:
                        arr_songs.append({"uri":"direct:track:"+song_info['url_128'], "repeat":1})

                #after download song, re-check song
                try:
                    audio_test=AudioFileClip(song['local'])
                    audioduration=audio_test.duration
                    audio_test.close()
                    if audioduration < 1:
                        continue
                except:
                    continue
                    pass

                song['local']=normal_audio(song['local'])
                if song['repeat'] > 1:
                    song['local']= create_loop_audio_times(song['local'], song['repeat'])

                if not "coolbg_ffmpeg" in song['local']:
                    tmp_clip_path = get_dir('coolbg_ffmpeg') + str(uuid.uuid4()) + '-' + os.path.basename(song['local'])
                    shutil.copyfile(song['local'], tmp_clip_path)
                    os.remove(song['local'])
                    song['local']=tmp_clip_path

                file_merg.write("file '%s'\n" % os.path.basename(song['local']))
                cnt_song+=1
            except:
                pass
        file_merg.close()
        if cnt_song>1:
            cmd = "ffmpeg -y -f concat -safe 0 -i \"%s\" -codec copy \"%s\"" % (file_merg_path, final_clip_path)
            os.system(cmd)
            os.remove(file_merg_path)
            for song in arr_songs:
                try:
                    os.remove(song['local'])
                except:
                    pass
        else:
            if cnt_song ==1:
                return arr_songs[0]['local']
    except:
        pass
    if cnt_song == 0:
        return None
    try:
        audio_moviepy = AudioFileClip(final_clip_path)
        if audio_moviepy.duration < 1:
            final_clip_path=None
        audio_moviepy.close()
    except:
        pass
    return final_clip_path




