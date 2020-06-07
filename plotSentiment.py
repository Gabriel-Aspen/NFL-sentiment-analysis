import pandas as pd
import matplotlib.pyplot as plt

def rollingMean(scores, window_size = 50):
    '''
    Attributes:
        scores: A list of sentiment scores
        window_size: The size of the rolling window to average across
    Output:
        A DataFrame of the averaged scores. This will exclude all nth instances
        where n < window_size
        Columns:
            scores: pd dataframe of sentiment scores
            rolling_mean: the new rolling mean scores
            minutes: the timestamp of the score in minutes

    to do: try setting df.rolling(center=True)
    '''
    return scores.rolling(window=window_size).mean() # window size of 50 points

def get_sec(time_str):
    '''
    Converts timestamp to seconds

    Attributes:
        time_str: a string of time in the format 'mm:ss'
    Output:
        integer of time in seconds
    '''
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)

def plotSentiment(df):
    '''
    Attributes:
        df: DataFrame with columns 'scores', 'rolling_mean' and 'minutes'
    Output:
        Plot of mean sentiment scores vs time in minutes
    '''
    plt.plot(df.minutes, df.rolling_mean)
    plt.xlabel('minutes')
    plt.ylabel('Relative Sentiment')
