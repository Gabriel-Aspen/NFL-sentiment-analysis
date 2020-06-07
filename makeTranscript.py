import speech_recognition as spr
import numpy as np

def makeTranscript(audio_file = False, steps=900, window_size=10, overlap= 0):
    '''
    Convert a .WAV file to a text transcript using Google web API

    Attributes
        audio_file: The location of the audio file (.WAV)
        steps: The number of windows to listen to
        window_size: The length of time in seconds each window will be
        overlap: The percentage (decimal) each window overlaps with the next

    Output
        A list of strings representing the transcribed text,
        each element of the list is one window
    '''
    #HERE
        #and HERE
    if audio_file == False:
        return 'no input'
    else:
        transcript = []
        for step in range(steps):
          r = spr.Recognizer()
          with spr.AudioFile(audio_file) as source:
              offset_multiplier = window_size * (1-overlap)
              audio = r.record(source, duration=window_size , offset=step * offset_multiplier)
          try:
              text = r.recognize_google(audio) #google web API recognizer- however there are many other options
              transcript.append([text])
          except spr.UnknownValueError:
              text = 'error'
          except spr.RequestError as e:
              False
        return np.array(transcript)
