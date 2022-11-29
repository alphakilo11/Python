import json
"""
open timeline data and show the timestamps of all activities exceeding the cutoff travel distance
PREREQUESITE Google Semantic Location History
ENHANCE add automatic folder processing
"""
cutoff_distance = 100000

with open('2022_JUNE.json', 'r') as file:
    dict = json.load(file)
for i in range(len(dict["timelineObjects"])):
    if 'activitySegment' in dict["timelineObjects"][i]:
        if 'distance' in dict["timelineObjects"][i]["activitySegment"]:
            distance = dict["timelineObjects"][i]["activitySegment"]['distance']
            if distance > cutoff_distance:
                print(distance, dict["timelineObjects"][i]["activitySegment"]["duration"]["startTimestamp"])
