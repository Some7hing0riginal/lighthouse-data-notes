# import packages we need (remember what packages we used yesterday during the API session)
# IMPORT HERE
import os
import requests
import pprint
import json
import html
import urllib

def makeRequest(url):
    # don't forget package os
    app_id = os.environ["app_id"]
    app_key = os.environ["app_key"]
    url_append = f'?app_id={app_id}&app_key={app_key}' 


    # We send the request to the API
    # NOTE: if you don't have your APP_KEY, run this without the url_append
    res = requests.get(url)

    # We can check if the request was successful
    if res.status_code != 200 and res.status_code != 300:
        print(f"Unsuccessful request. Error code {res.status_code}")
        return res.status_code
    else:
        return res

res = makeRequest("https://api.tfl.gov.uk/AirQuality")

# We can export the information that was returned using method .json()
json_response = res.json()

futureForecast = json_response["currentForecast"][1]

#print(pprint.pprint(futureForecast))


forecastText = html.unescape(futureForecast["forecastText"])
formattedForecastText = forecastText.replace(r'<br/>', '\n')
print(formattedForecastText)


#task
#res = makeRequest("https://api.tfl.gov.uk/Line/Meta/Modes")
res = makeRequest("https://api.tfl.gov.uk/Journey/Meta/Modes")

json_response = res.json()

#print(json.dumps(json_response))
tflModesList = [mode["modeName"] for mode in json_response if mode["isTflService"]]

print(tflModesList)
print(f"The number of different modes of transport is {len(tflModesList)}")

#task
res = makeRequest("https://api.tfl.gov.uk/BikePoint")
json_response = res.json()

with open('responseBikePoints.json', 'w') as outfile:
    json.dump(json_response, outfile)

sumOfWorkingDocks = 0
sumOfTotalDocks = 0
for bikepoint in json_response:
    nbBikes = int(bikepoint["additionalProperties"][6]["value"])
    nbEmptyDocks = int(bikepoint["additionalProperties"][7]["value"])
    sumOfWorkingDocks += nbBikes + nbEmptyDocks
    sumOfTotalDocks += int(bikepoint["additionalProperties"][8]["value"])

print()
print(f"There are a total of {len(json_response)} BikePoints")
print(f"There are a total of {sumOfWorkingDocks} working docks")
print(f"There are a total of {sumOfTotalDocks} all docks")


#task
res = makeRequest("https://api.tfl.gov.uk/Line/Mode/tube")
json_response = res.json()
tubelines = json_response


res = makeRequest("https://api.tfl.gov.uk/Line/Mode/bus")
json_response = res.json()
buslines = json_response

print()
print(f"Total of {len(tubelines)} tube lines and {len(buslines)} bus lines")
print([line["name"] for line in tubelines])
print()

res = makeRequest("https://api.tfl.gov.uk/Line/Victoria/StopPoints")
json_response = res.json()
print(f"Victoria line has {len(json_response)} stations")
print()



#task
res = makeRequest("https://api.tfl.gov.uk/Journey/JourneyResults/Heathrow%20Airport/to/Tower%20Bridge?mode=bus")
json_response = res.json()

toLocation = json_response["toLocationDisambiguation"]["disambiguationOptions"][0]["parameterValue"]
fromLocation = json_response["fromLocationDisambiguation"]["disambiguationOptions"][0]["parameterValue"]

res = makeRequest(f"https://api.tfl.gov.uk/Journey/JourneyResults/{fromLocation}/to/{toLocation}?mode=bus")
json_response = res.json()

busJourney = json_response["journeys"][0]
print(f"Duration of {busJourney['duration']} minutes on the bus")

res = makeRequest(f"https://api.tfl.gov.uk/Journey/JourneyResults/{fromLocation}/to/{toLocation}?mode=tube")
json_response = res.json()
tubeJourney = json_response["journeys"][0]
print(f"Duration of {tubeJourney['duration']} minutes on the tube")

#with open('responseJourneyBus.json', 'w') as outfile:
#    json.dump(json_response, outfile)