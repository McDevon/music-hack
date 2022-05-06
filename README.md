# Music Hack

A collection of scripts for toying around with music files. The scripts rely on beat detection and audio editing libraries.

## Usage

A convenience `Dockerfile` is provided to get the correct versions of Python and all the dependencies.

Build the docker image:

    docker build . -t music

Run the docker container and mount your directory containing music files (change `/absolute/path/to/music/directory` to your actual path containing `.mp3` files):

    docker run -itv /absolute/path/to/music/directory:/music-hack/files music

You have entered the docker container and your music files are available in the directory called `files`. You are now ready to start using the scripts. If used from the current path, they will add the output files to the same directory where the input files are.

You can exit the docker container with `Ctrl+D`.

### Requirements for running without Docker

[Ffmpeg](https://www.ffmpeg.org) suite with sdl2. On a Mac with HomeBrew:

    brew install ffmpeg

Following python libraries:

    pip install Cython
    pip install numpy
    pip install pydub madmom librosa

Note that there are issues with some version combinations of these libraries and using Docker is recommended to get the dependencies right.

## Beatremove

Beatremove is inspired by "Every other beat is missing" -experiments, such as [this one](https://youtu.be/jws73OMT6a8). It removes beats in sequences. Usage examples:

Remove every other beat from a song (default behavior):

    python beatremove.py files/song.mp3

Remove every fifth beat from a song (in every five beat sequence, remove the beat at index 4):

    python beatremove.py -s 5 -i 4 files/song.mp3

Leave only every fifth beat to a song (in every five beat sequence, remove beats at indices 1-4):

    python beatremove.py -s 5 -i 1,2,3,4 files/song.mp3

## Beatreverse

Beatreverse works similarly to beatremove, except that it reverses the selected beats instead of removing them. Usage examples:

Reverse every other beat in a song (default behavior):

    python beatreverse.py files/song.mp3

Reverse every beat in a song:

    python beatreverse.py -s 1 -i 0 files/song.mp3

## Swing

Swing is inspired by [swinger.py](https://github.com/echonest/remix/blob/master/tutorial/swinger/swinger.py) script, which relies on libraries that seem to no longer work. It attempts to convert 4/4 songs into swingy 6/8 format. Currently the script expects a stereo track.

Usage:

    python swing.py files/song.mp3

## Insert

Insert works similarly to beatremove, except that it replaces the selected beats instead of removing them. The replace clip is cropped to fit the beat. Usage examples:

Replace every tenth beat of a song by insert.mp3:

    python insert.py -s 10 -i 9 files/song.mp3 files/insert.mp3

## Speedup

Speedup speeds the song up beat by beat, starting at normal speed and ending up going at double speed by the end of the song. Currently the script expects a stereo track.

Usage:

    python speedup.py files/song.mp3

## Trucker

Trucker adds half step modulations to a song. Currently the script expects a stereo track. Usage examples:

Add a half-step modulation in the middle of a song (default behavior):

    python trucker.py files/song.mp3

Add half-step modulations at beat indices 80, 160, and 240 to a song:

    python trucker.py -i 80,160,240 files/song.mp3

## Notes

- There have been issues with Python versions 3.7 and 3.10, docker usage is recommended
- The scripts currently only support mp3 files for input and output
- There are no proper input checks or error messages
