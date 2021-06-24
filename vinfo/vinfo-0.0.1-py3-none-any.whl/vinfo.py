import cv2
import sys

if len(sys.argv)==1:
 print('enter image filaname')
 sys.exit(0)
def main():
 d=cv2.VideoCapture(sys.argv[1])
 frames=d.get(cv2.CAP_PROP_FRAME_COUNT)
 fps=d.get(cv2.CAP_PROP_FPS)
 width=d.get(cv2.CAP_PROP_FRAME_WIDTH)
 height=d.get(cv2.CAP_PROP_FRAME_HEIGHT)
 print("frames=",frames,"fps=",fps,"width=",width,"height=",height)
 sys.exit(0)
main()
