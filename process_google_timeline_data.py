def search_location_timeline(year, cutoff_distance):
    """
    open timeline data and write the timestamps and destinations of all activities exceeding the cutoff
    travel distance to a results.csv
    PREREQUESITE This file inside the Google 'Semantic Location History' folder
    ENHANCE sort by date
    the first level is a single key named "timelineObjects" it's value is a list of all items
    the second level consists of either "activitySegment" or "placeVisit" keys that have new dictionaries as values
    """
    import os
    import json
    import csv
    from timeit import default_timer as timer

    start_time = timer()

    relevant_entries = [['Distance (m)', 'DTG', 'Departure', 'Destination']] # set Header
    for json_filename in os.listdir(year):
        json_path = year + '/' + json_filename
        with open(json_path, 'r') as file:
            dict = json.load(file)
        for i in range(len(dict["timelineObjects"])):
            if 'activitySegment' in dict["timelineObjects"][i]:
                if 'distance' in dict["timelineObjects"][i]["activitySegment"]:
                    distance = dict["timelineObjects"][i]["activitySegment"]['distance']
                    if distance > cutoff_distance:
                        destination_counter = i + 1
                        while "placeVisit" not in dict["timelineObjects"][destination_counter]:
                            destination_counter += 1
                        if destination_counter >= len(dict["timelineObjects"]): #prevent destination_counter from exceeding list 
                            destination_counter = len(dict["timelineObjects"]) - 1
                        departure_counter = i - 1
                        while "placeVisit" not in dict["timelineObjects"][destination_counter]:
                            departure_counter -= 1
                        if departure_counter < 0: # prevent departure_counter from going negative
                            departure_counter = 0
                        # Compose entries
                        try:
                            startTime = dict["timelineObjects"][i]["activitySegment"]["duration"]["startTimestamp"]
                        except:
                            startTime = 'no Time'
                        try:
                            Departure = dict["timelineObjects"][departure_counter]["placeVisit"]["location"]["address"]
                        except:
                            Departure = 'no DEP'
                        try:
                            Destination = dict["timelineObjects"][destination_counter]["placeVisit"]["location"]["address"]
                        except:
                            Destination = 'no DEST'
                        relevant_entries.append([distance, startTime, Departure, Destination])

    with open('results.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerows(relevant_entries)

    print('Done in', timer() - start_time, 's.')
search_location_timeline('2022', 100000)
