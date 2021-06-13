#!/usr/bin/env python3

import sys
import subprocess
import os

from datetime import datetime
from datetime import timedelta

# get input
_, VIDEO, CHAPTERS, OUTPUT = sys.argv
TMPFILE = '_tmp_ffmpeg_chapters'
times = []

# process chapters file
with open(CHAPTERS, 'r') as f:
    for line in f:
        time, title = line.split(" ", 1)
        
        if len(time) == 2: # ss
            time = datetime.strptime(time, "%S")
        elif len(time) == 5: # mm:ss
            time = datetime.strptime(time, "%M:%S")
        elif len(time) == 8: # hh:mm:ss
            time = datetime.strptime(time, "%H:%M:%S")
        else:
            raise Exception("Date time format is not correct.")

        time = int((time - datetime(1900, 1, 1)).total_seconds()) * 1_000_000_000 # s to ns
        times.append([time,title])

# FFMETADATA file for timestamps
timestamps = [';FFMETADATA1\n']

# last time is video length
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

# cleanup
os.remove(TMPFILE)