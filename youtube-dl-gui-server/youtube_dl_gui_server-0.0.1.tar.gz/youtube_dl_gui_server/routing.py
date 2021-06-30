#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import request, render_template, url_for, make_response, flash, send_file, redirect, Response
import tempfile, string, random, os, json, time
from http import HTTPStatus
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import youtube_dl

tmp_dir=tempfile.TemporaryDirectory()
root=os.path.dirname(os.path.abspath(__file__))+"/"

FILE_CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase
VIDEO_FORMATS={
    "default": "",
	"webm": "webm",
    "webm [240p]": "webm[height=240]+bestaudio",
    "webm [360p]": "webm[height=360]+bestaudio",
    "webm [480p]": "webm[height=480]+bestaudio",
    "webm [720p]": "webm[height=720]+bestaudio",
    "webm [1080p]": "webm[height=1080]+bestaudio",
    "webm [1440p]": "webm[height=1440]+bestaudio",
    "webm [2160p]": "webm[height=2160]+bestaudio",
    "mp4": "mp4",
    "mp4 [144p]": "mp4[height=144]+bestaudio[ext=m4a]",
	"mp4 [240p]": "mp4[height=240]+bestaudio[ext=m4a]",
    "mp4 [360p]": "mp4[height=360]+bestaudio[ext=m4a]",
    "mp4 [480p]": "mp4[height=480]+bestaudio[ext=m4a]",
    "mp4 [720p]": "mp4[height=720]+bestaudio[ext=m4a]",
    "mp4 [720p]": "mp4[height=1080]+bestaudio[ext=m4a]",
    "mp4 [1440p]": "mp4[height=1440]+bestaudio[ext=m4a]",
    "mp4 [2160p]": "mp4[height=2160]+bestaudio[ext=m4a]",
}
AUDIO_FORMATS = ["mp3","wav","aac","m4a","vorbis","opus","flac",]

executor=ThreadPoolExecutor(max_workers=2, thread_name_prefix="th")
proc=[]

def gen_hook(id):
    def dl_hook(d):
        if d["status"]=="downloading":
            proc[id]["queue"].put({"status": "downloading","progress": d['_percent_str'][:-1][1:],"total": d['_total_bytes_str'],"speed": d['_speed_str']})
        if d["status"]=="finished":
            proc[id]["queue"].put({"status": "finished", "total": d['_total_bytes_str'], "filename": os.path.basename(d['filename'])})
    return dl_hook

class DLLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

def download_yt(id,queue,url,format):
    ydl_opts = {
        'logger': DLLogger(),
        'progress_hooks': [gen_hook(id)],
        'outtmpl': root+"static/files/%(title)s_%(id)s-%(format)s.%(ext)s"
    }
    if format=="default":
        pass
    elif format in AUDIO_FORMATS:
        ydl_opts.update({'format': "bestaudio", 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': format}]})
    elif format in VIDEO_FORMATS:
        ydl_opts.update({'format': VIDEO_FORMATS[format]})
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    

def event_stream(queue,id):
    while True:
        sse_event = 'progress-item'
        data=queue.get(True)
        if data["status"] == "finished":
            sse_event = 'last-item'
            time.sleep(3)
        yield "event:{event}\ndata:{data}\n\n".format(event=sse_event, data=json.dumps(data))

def prepare_response(response):
	di=dir(response)
	if 'set_cookie' not in di:
		response=make_response(response)
	response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
	response.headers['X-Content-Type-Options'] = 'nosniff'
	response.headers['X-Frame-Options'] = 'SAMEORIGIN'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	return response



def show_home():
    files=os.listdir(root+"static/files/")
    results=[]
    for file in files:
        if os.path.splitext(file)[1]:
            results.append(file)
    return render_template("home.html",title="メインページ",video_fmt=list(VIDEO_FORMATS.keys()),audio_fmt=AUDIO_FORMATS,files=results)

def do_add_download():
    urls=request.form.get("url")
    urls=list(filter(lambda a: a!='',urls.split("\n")))
    format=request.form.get("format")
    q=Queue()
    id=len(proc)
    if id<5:
        proc.append({"thread": executor.submit(download_yt,id=id,queue=q,url=urls,format=format),"queue": q})
        return str(id)
    return "False"

def return_stream(id):
    if id<len(proc):
        return Response(event_stream(proc[id]['queue'],id), mimetype='text/event-stream')

def do_del_cache(file):
	files=os.listdir(os.path.join(root,"static/files"))
	if file in files:
		os.remove(os.path.join(root,"static/files",file))
	return redirect(url_for('index'))


def after_request(response):
	return  prepare_response(response)
