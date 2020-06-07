import numpy as np
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def generateSentiment(transcript, element= 'compound'):
    '''
    Generates a sentiment score for every string in a list of strings

    Attributes:
        transcript: A list of strings
        element: String of a selected sentiment metric from vaderSentiment
                Can be positive, negative, neutral or compound
    Output
        A list of sentiment scores corresponding to the list of strings
        in the transcript
    '''
    analyzer_obj = SentimentIntensityAnalyzer()
    sent_dict = []
    for i in range(int(transcript.size)):
        score_set = analyzer_obj.polarity_scores(str(transcript[i]))
        sent_dict.append(score_set)
    chosen_element = [] # can be positive, negative, neutral or compound
    for i in range(len(sent_dict)):
        chosen_element.append(sent_dict[i][element])
    return chosen_element
