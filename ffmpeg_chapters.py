import sys
import subprocess
import datetime
import os

# get input
TMPFILE = '_tmp_ffmpeg_chapters.txt'
_, VIDEO, CHAPTERS, OUTPUT = sys.argv
times = []

# process chapters file
with open(CHAPTERS, 'r') as f:
    for line in f:
        time, title = line.split(" ", 1)
        h,m,s = [int(x) for x in time.split(":")]
        time = int(datetime.timedelta(
                hours=h, minutes=m, seconds=s
            ).total_seconds()) * 1_000_000_000 # converted to ns

        times.append([time,title])

# creating the formatted timestamps file

timestamps = [';FFMETADATA1\n']

# loop over all but last one
for i, (time, title) in enumerate(times[:-1]):
    end = times[i+1][0]
    timestamps += ['[CHAPTER]\n',
        'START=' + str(time) + '\n',
        'END=' + str(end) + '\n',
        'title=' + str(title) + '\n'
    ]

with open(TMPFILE, 'w') as f:
    f.writelines(timestamps)


# run add the formatted chapters to the video
subprocess.run(["ffmpeg", 
    "-i", TMPFILE,
    "-i", VIDEO,
    "-y",
    "-codec", "copy",
    OUTPUT
    ]
)

# # cleanup
os.remove(TMPFILE)