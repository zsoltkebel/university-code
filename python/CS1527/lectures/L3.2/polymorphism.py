# Author: Zsolt Kébel
# Date: 10/02/2021

class AudioFile:

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Invalid file format')
        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'

    def play(self):
        print('playing as mp3')


class WavFile(AudioFile):
    ext = 'wav'

    def play(self):
        print('playing as wav')


mp3 = MP3File('myfile.mp3')
mp3.play()

wav = WavFile('myfile.wav')
wav.play()

no_file = MP3File('thisfile.abc')
