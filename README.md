# Music Hack
A collection of scripts for toying around with music files. The scripts rely on beat detection and audio editing libraries.

### Requirements
[Ffmpeg](https://www.ffmpeg.org) suite with sdl2. On a Mac with HomeBrew:

    brew install ffmpeg --with-sdl2

Following python libraries:

    pip3 install numpy madmom pydup librosa

## Beatremove

Beatremove was inspired by "Every other beat is missing" -experiments, such as [this one](https://youtu.be/jws73OMT6a8). It removes beats in sequences. Usage examples:

Remove every other beat from a song (default behavior):

    python3 beatremove.py song.mp3

Remove every fifth beat from a song:

    python3 beatremove.py -s 5 -i 4 song.mp3

Leave only every fifth beat to the song:

    python3 beatremove.py -s 5 -i 1,2,3,4 song.mp3

## Beatreverse

Beatreverse works similarly to beatremove, except it reverses the selected beats instead of removing them. Usage examples:

Reverse every other beat in a song (default behavior):

    python3 beatreverse.py song.mp3

Reverse every beat in a song:

    python3 beatreverse.py -s 1 -i 0 song.mp3

## Swing

Swing is inspired by [swinger.py](https://github.com/echonest/remix/blob/master/tutorial/swinger/swinger.py) script, which relies on libraries that seem to no longer work. It attempts to convert 4/4 songs into swingy 6/8 format. Currently the scripts expects a stereo track.

Usage:

    python3 swing.py song.mp3

## Notes
- As Madmom has [some issues](https://github.com/CPJKU/madmom/issues/373) with Python 3.7, all testing has been done using Python 3.66
- The scripts currently only support mp3 files for input and output
- There are no proper input checks or errors