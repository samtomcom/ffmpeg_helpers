# FFMPEG Helpers

This repository contains scripts that help with the execution of ffmpeg commands and related video file management.

## Requirements

* ffmpeg
* Python 3
* bash

## Installation

1. Clone the repository
2. Add the repository directory to your `PATH` so that the commands can be run from anywhere from a bash prompt.

You may have to `chmod +x` the files to make them executable if they are not already.

## Scripts

### ffmpeg_chapters.py

A script to make adding chapters to video files more human readable (01:23:45 timestamps instead of milliseconds).

### find264

Find a list of the files in the current directory that are encoded with H.264 encoding.

### findaudio

Find a list of the files in the current directory that have 5.1 audio channels.

### reencode

Take a video file and reencode it to a new audio and video encoding, then replace the original file.
Can also take a list of files from STDIN or a file and reencode them all.
