# Music Hack
A collection of scripts for toying around with music files. The scripts rely on beat detection and audio editing libraries.

### Requirements
[Ffmpeg](https://www.ffmpeg.org) library with sdl-2. On a Mac with HomeBrew:

    brew install ffmpeg --with-sdl2

Following python libraries:

    pip3 install numpy madmom pydup librosa ipython

## Beatremove

Beatremove was inspired by "Every other beat is missing" -experiments, such as [this one](https://youtu.be/jws73OMT6a8). It removes beats in sequences. Usage examples:

Remove every other beat from a song (default behavior):

    python3 beatremove.py song.mp3

Remove every fifth beat from a song:

    python3 beatremove.py -s 5 -i 4 song.mp3

Leave only every fifth beat to the song:

    python3 beatremove.py -s 5 -i 1,2,3,4 song.mp3

## Notes
- As Madmom has [some issues](https://github.com/CPJKU/madmom/issues/373) with Python 3.7, all testing has been done using Python 3.66
- The scripts currently only support mp3 files for input and output