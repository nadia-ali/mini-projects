import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='MASKED FOR GITHUB')
from_ = "St james's park"
pubs = gmaps.places("pubs near {}".format(from_))
nearest_pubs = []

for pub in pubs["results"]:
    if "name" in pub.keys():
        name = pub["name"]
    else:
        name = "NOT AVAILABLE"
    if "formatted_address" in pub.keys():
        place = pub["formatted_address"]
    else:
        place = "NOT AVAILABLE"
    if "rating" in pub.keys():
        rating = pub["rating"]
    else:
        rating = "NOT AVAILABLE"
    
    nearest_pubs.append([name,place,rating])

for index, pub in enumerate(nearest_pubs):
    address = pub[1]
    d_api = gmaps.distance_matrix(origins=from_, destinations=address)
    distance_tmp = d_api["rows"][0]["elements"][0]["distance"]["text"]
    if "km" in distance_tmp :
        distance = float(distance_tmp.split(" km")[0])
    elif "m" in distance_tmp:
        distance = float(distance_tmp.split(" m")[0])
        
    duration = d_api["rows"][0]["elements"][0]["duration"]["text"]
    
    nearest_pubs[index].append(distance)
    nearest_pubs[index].append(duration)


data = pd.DataFrame(nearest_pubs,columns=["name","address","rating","distance","duration"])
sorted_data = data.sort(["distance"])
final_result = sorted_data.ix[0]
print("You can get to {} on {} which has rating of {} which is {}km far and it would take {} to go. ".format(final_result["name"], final_result["address"] , final_result["rating"] , final_result["distance"], final_result["duration"]))
