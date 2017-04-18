import requests


from_ = "LHR"
destination = "CJB"
outbound = "2017-06-25"
inbound = "2017-06-17"

api_key = "su999063616257631624190979680802"
url_template = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/GB/GBP/EN-US/{}/{}/{}/{}?apiKey={}"
url = url_template.format(from_, destination, inbound, outbound, api_key)

response = requests.get(url)

r = response.json()

min_price = 100000
min_index = -1

# finding the index of dictionary with cheapest price
for index,dictionary in enumerate(r["Quotes"]):
    price = dictionary["MinPrice"]
    date = dictionary["OutboundLeg"]["DepartureDate"]
    if price < min_price:
        min_price = price 
        min_index = index
    else:
        pass


# min_index - > index of cheapest price
final = r["Quotes"][min_index]

price = final["MinPrice"]
outbound_flights = final["OutboundLeg"]["CarrierIds"]
departure_date = final["OutboundLeg"]["DepartureDate"]
inbound_flights = final["InboundLeg"]["CarrierIds"]
return_date = final["InboundLeg"]["DepartureDate"]

outbound_flights_str = []
inbound_flights_str = []

carriers = {}

for value in r["Carriers"]:
    key = value["CarrierId"]
    d_value = value["Name"]
    carriers[key] = d_value 

for id in outbound_flights:
    outbound_flights_str.append(carriers[id])
    
for id in inbound_flights:
    inbound_flights_str.append(carriers[id])

output_message = """The cheapest flight from {} to {} is {} pounds and your itenary is

outbound: {} at {}

inbound: {} at {} 
"""

output = output_message.format(from_, destination, price, ",".join(outbound_flights_str), departure_date, ",".join(inbound_flights_str), return_date)

print (output)
