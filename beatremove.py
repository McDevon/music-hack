from optparse import OptionParser
from pydub import AudioSegment
import librosa
import madmom
import numpy as np
import sys
import os
import random
import string

def convert(inputFile, outputFile, options):

    wavFileName = 'temp_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + '.wav'

    track = AudioSegment.from_mp3(inputFile)
    track.export(wavFileName, format='wav')

    proc = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)
    act = madmom.features.beats.RNNBeatProcessor()(wavFileName)

    os.remove(wavFileName)

    beat_times = proc(act)

    timelist = np.insert(beat_times, 0, 0)
    combined = AudioSegment.empty()

    sequenceLength = int(options.sequence)
    indices = list(map(lambda x: int(x), options.index.split(',')))

    for i in range(0, len(timelist)-1):
        if i % sequenceLength in indices:
            continue
        
        start = int(timelist[i] * 1000)
        end = int(timelist[i+1] * 1000)

        combined += track[start:end]

    combined.export(outputFile, format='mp3')

def main():
    parser = OptionParser(usage='usage: %s [options] <mp3_file>' % sys.argv[0])
    parser.add_option('-s', '--sequence', default=2, help='beat sequence length, default = 2')
    parser.add_option('-i', '--index', default="0", help='beat indices to remove from sequence, default = 0')

    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        return -1

    fileName = args[0]
    outputFile = ''.join(fileName.split('.')[:-1]) + '_beatremove.mp3'

    convert(fileName, outputFile, options)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print (e)
