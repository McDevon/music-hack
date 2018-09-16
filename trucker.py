from optparse import OptionParser
from pydub import AudioSegment
from pydub.effects import speedup
import librosa
import madmom
import numpy as np
import sys
import os
import random
import string

def stereo_time_stretch(sample, multiplier):
    left = librosa.effects.time_stretch(sample[0], multiplier)
    right = librosa.effects.time_stretch(sample[1], multiplier)
    return np.array([left,right])

def stereo_pitch_shift(sample, rate, steps):
    left = librosa.effects.pitch_shift(sample[0], rate, n_steps=steps)
    right = librosa.effects.pitch_shift(sample[1], rate, n_steps=steps)
    return np.array([left,right])

def audiosegment_to_ndarray(audiosegment):
    samples = audiosegment.get_array_of_samples()
    samples_float = librosa.util.buf_to_float(samples, n_bytes = 2, dtype = np.float32)
    if audiosegment.channels == 2:
        sample_left= np.copy(samples_float[::2])
        sample_right= np.copy(samples_float[1::2])
        sample_all = np.array([sample_left,sample_right])        
    else:
        sample_all = samples_float
    
    return [sample_all, audiosegment.frame_rate]

def convert(inputFile, outputFile, options):

    wavFileName = 'temp_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + '.wav'

    track = AudioSegment.from_mp3(inputFile)
    track.export(wavFileName, format="wav")

    proc = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)
    act = madmom.features.beats.RNNBeatProcessor()(wavFileName)

    os.remove(wavFileName)

    beat_times = proc(act)

    timelist = np.insert(beat_times, 0, 0)
    allParts = []

    indices = [int(len(timelist) / 2)] if len(options.index) == 0 else list(map(lambda x: int(x), options.index.split(',')))
    shifts = 0

    for i in range(0, len(timelist)-1):
        
        start = int(timelist[i] * 1000)
        end = int(timelist[i+1] * 1000)
            
        split = track[start:end]

        if i in indices:
            shifts = shifts + 1

        seg = audiosegment_to_ndarray(split)[0]
        
        if shifts == 0:
            allParts.append(seg)
        else:
            allParts.append(stereo_pitch_shift(seg, split.frame_rate, shifts))
    
    fullSong = np.concatenate(allParts, 1)

    # TODO ndarray_to_audiosegment
    librosa.output.write_wav(wavFileName, fullSong, track.frame_rate)

    track = AudioSegment.from_wav(wavFileName)
    track.export(outputFile, format="mp3")

    os.remove(wavFileName)


def main():
    usage = "usage: %s [options] <mp3_file>" % sys.argv[0]
    parser = OptionParser(usage=usage)
    parser.add_option('-i', '--index', default="", help='beat indices at which to modulate half a step upwards, default = one shift at the middle of the track')

    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        return -1

    fileName = args[0]
    outputFile = ''.join(fileName.split('.')[:-1]) + '_eurovision.mp3'

    convert(fileName, outputFile, options)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print (e)
