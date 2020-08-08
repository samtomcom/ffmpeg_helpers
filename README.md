# FFMPEG Chapters

Add chapters easily to a file, with ffmpeg.

Created because I really don't want to type out all those times, and convert timestamps into nanoseconds just to correctly tag recordings of concerts.

## Requirements

* ffmpeg
* Python 3

## Installation

    $ git clone https://github.com/samtomcom/ffmpeg_chapters.git
    $ cd ffmpeg_chapters/
    $ sudo chmod +x ffmpeg_chapters.py

## Usage

Create a file with timestamps and (optional) chapter names for the chapters, separated by a space.  
The time should be formated as HH:MM:SS
The final line should be the approximate length of the video

chapters.txt

    00:00:00 Intro
    00:01:00 Chapter 1
    00:01:30 Unnamed Chapter
    00:02:00 Final Chapter
    00:03:00 x

If chapter names are not provided they will be named 'Unnamed Chapter'

    00:01:30

is the same as

    00:01:30 Unnamed Chapter

Run the program with:

    $ ffmpeg_chapters.py video.mp4 chapters.txt out.mp4

Where out.mp4 is the output file.