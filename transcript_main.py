from generateSentiment import generateSentiment
from plotSentiment import plotSentiment, rollingMean, get_sec
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = 'transcripts/sbL.csv'
title = 'sbL from transcript'

#smoothing the data
rolling_mean_window_size = 50

def main(filepath, title):
    df = pd.read_csv(filepath)
    df['sent_scores'] = generateSentiment(df['transcript'])
    df['rolling_mean'] = rollingMean(df.sent_scores, window_size=rolling_mean_window_size)
    df['minutes'] = df.time.apply(get_sec)/60
    plotSentiment(df, title = title)
main(filepath, title)
