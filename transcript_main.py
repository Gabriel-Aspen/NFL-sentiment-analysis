from generateSentiment import generateSentiment
from plotSentiment import plotSentiment, rollingMean, get_sec
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = 'transcripts/sbL.csv'

def main(filepath):
    df = pd.read_csv(filepath)
    df = df.head(100)
    #check Columns
    df['sent_scores'] = generateSentiment(df['transcript'])
    df['rolling_mean'] = rollingMean(df.sent_scores)
    df['minutes'] = df.time.apply(get_sec)/60
    plotSentiment(df)
main(filepath)
