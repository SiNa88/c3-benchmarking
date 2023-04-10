import ffmpeg
import subprocess as commands
import sys

input_file = sys.argv[1]
data = commands.getstatusoutput("ffprobe -show_entries stream=r_frame_rate,nb_read_frames -select_streams v -count_frames -of compact=p=0:nk=1 -v 0 "+str(input_file))
y = list(data)
spl = y[1].split("|")
#print(spl[0], " ", spl[1])
spl0 = spl[0].split("/")
print(int(spl[1])/(int(spl0[0])/int(spl0[1])))
