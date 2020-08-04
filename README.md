# FFMPEG Chapters

Add chapters easily to a file, with ffmpeg.

## Requirements

* ffmpeg
* Python 3

## Usage

Create a file with timestamps and (optional) chapter names for the chapters, separated by a space.  
The time should be formated as HH:MM:SS:ms, if any are ommited the last values will be assumed to be 0, e.g. 00:12:30 will give the ms collumn 00
If chapter names are not provided they will be automatically created (by number)  

chapters.txt

    00 Intro
    00:01 Chapter 1
    00:01:30 
    00:02 End

is the same as

    00:00:00:00 Intro
    00:01:00:00 Chapter 1
    00:01:30:00 Chapter 2
    00:02:00:00 End

Run the program with:

    $ python ffmpeg_chapters.py video.mp4 chapters.txt out.mp4

Where out.mp4 is the output file.