from generateSentiment import generateSentiment
from makeTranscript import makeTranscript
from plotSentiment import plotSentiment, rollingMean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = 'audiofiles/highlights.wav'
name = 'XLVII highlights'

# making the transcript
window_size=10 #10 second samples
steps=900 #900 samples - stops automatically at the end of recording
overlap= 0 #no overlap

#smoothing the data
rolling_mean_window_size = 2

def main(filepath):
    transcript = makeTranscript(filepath, steps=steps, window_size=window_size,
                                overlap=overlap)
    sentiment = generateSentiment(transcript)
    df = pd.DataFrame(sentiment, columns= ['sent_scores'])
    df['rolling_mean'] = rollingMean(df.sent_scores, window_size=rolling_mean_window_size)
    df['minutes'] = ((df.index +1) *window_size)/60
    plotSentiment(df, title = name)
    #do this for transcript too
main(filepath)
