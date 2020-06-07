from generateSentiment import generateSentiment
from makeTranscript import makeTranscript
from plotSentiment import plotSentiment, rollingMean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = 'audiofiles/highlights.wav'
window_size=10 #10 second samples
steps=900 #900 samples
overlap= 0 #no overlap

def main(filepath):
    transcript = makeTranscript(filepath, steps=steps, window_size=window_size,
                                overlap=overlap)
    sentiment = generateSentiment(transcript)
    df = pd.DataFrame(sentiment, columns= ['sent_scores'])
    df['rolling_mean'] = rollingMean(df.sent_scores)
    df['minutes'] = ((df.index +1) *window_size)/60
    plotSentiment(df)
main(filepath)
