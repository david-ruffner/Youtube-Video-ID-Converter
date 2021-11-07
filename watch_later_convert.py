import csv
import requests
import json
import pandas as pd
import openpyxl

class Video:
    def __init__(self, title, channel):
        self.title = title
        self.channel = channel

def GetVideoInfo(videoId):
    response = requests.get("https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={0}&key=[Your Google API Key Here]"
    .format(videoId))

    if response.status_code == 200:
        responseObj = json.loads(response.text)
        try:
            title = responseObj["items"][0]["snippet"]["title"]
            channel = responseObj["items"][0]["snippet"]["channelTitle"]
            return Video(title, channel)
        except:
            return Video(videoId, "Invalid")
    else:
        return None

def GetVideoIds(fileName):
    videoIds = []
    with open(fileName, 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        
        for row in csvReader:
            videoIds.append(row[0])

    return videoIds

videoIds = GetVideoIds("./watch_later_csv.csv")
totalVideos = len(videoIds)
currentVideo = 0
titles = []
channels = []

for id in videoIds:
    currentVideo = currentVideo + 1
    finishedPercentage = currentVideo / totalVideos

    print("Processing Video {0} of {1} - {2:.2f}% Finished\n".format(currentVideo, totalVideos, (finishedPercentage * 100)))
    vid = GetVideoInfo(id)
    if vid != None:
        titles.append(vid.title)
        channels.append(vid.channel)
    else:
        print("Sorry, something went wrong with video: {0}\n".format(id))

df = pd.DataFrame({'Title':titles, 'Channel':channels})
df.to_excel("./watch_later.xlsx")