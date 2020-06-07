# NFL-sentiment-analysis
In this project I visualize how the announcer's opinion changes throughout an NFL game using VADER sentiment analysis. This is compatible with both .wav files as well as .csv files of YouTube-generate transcripts.

## Data
### Audio
For brevity the audio in this project is taken from a YouTube clip of Superbowl XLVII found [here](https://www.youtube.com/watch?v=N-byJvHAXQA), however longer clips of an entire game can be used:
> ![](sbLII.png)

> YouTube clip of the entire Eagles vs Patriots Superbowl LII game found [here](https://www.youtube.com/watch?v=0FF_DbJ3G68)
### Transcript
A YouTube-generated transcript can be used as well. Copy and paste the timestamps and transcripts into a spreadsheet with columns 'time' and 'transcript' respectively

## Transcribing the audio
Audio is transcribed using the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library. This allows us to pass the .wav file through Google's web speech API, or any other API in the library you may have access to. Other examples of the APIs compatible with this library are:

1. CMU Sphinx 
2. Google Cloud Speech API
3. Microsoft Bing Voice Recognition
4. Houndify API
5. IBM Speech to Text

I have decided to break the audio into **10 second windows**, for a typical 2.5 hour clip of a superbowl game this is roughly 900 data points. The audio windows can be adjusted to any length, and can be overlapped to allow SpeechRecognition to capture more context.

## Sentiment analysis
Once the audio file has been transcribed we determine the sentiment score of each window using [vaderSentiment](https://pypi.org/project/vaderSentiment/). The metric I've chosen is compound because it's aggregation of positive, negative and neutral sentiment. Check out this [Medium Article](https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f) to learn more about using vaderSentiment 

## Data smoothing
To make visualization a little cleaner I use a rolling mean across sentiment scores. This helps to capture the general sentiment and smooth over tiny fluctuations VADER might pick up in the announcers attitude. The trade off is that the new sentiment score no longer corresponds with the actual sentiment - a data point might be pulled in the positive or negative direction depending on the scores of it's neighbors. It's important to note that 0 is no longer considered neutral.

# How to use
Clone this repo and pip install the dependencies:
* pandas
* numpy
* matplotlib
* vaderSentiment
* SpeechRecognition
## For audio files
1. Save your audio file as a .wav in the 'audiofiles' folder
2. Open audio_main.py and specify the path of the file. Add a title
3. Adjust the window_size, steps, and overlap (decimal). I've found that a 10 second window works well, the number of steps will depend on how long your audio file is. Overlap (decimal) is the percent of the tail end that one window will overlap with the next
4. Adjust rolling_mean_window_size. You can play around with this to see what looks best visually, I've found that this value should be somewhere around 5% of the total windows (900 windows = 45 rolling_mean_window_size)
5. Run audio_main.py
6. Your plot will be saved in the 'images' folder!
## For transcript files
1. Copy and paste the YouTube timestamps and transcripts into a spreadsheet with columns 'time' and 'transcript' respectively. Save this transcript file as a .csv in the 'transcripts' folder. 
2. Open transcript_main.py and specify the path of the file. Add a title
3. Adjust rolling_mean_window_size
4. Run transcript_main.py
5. Your plot will be saved in the 'images' folder!
