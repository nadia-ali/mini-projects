import requests
import json 
import pandas as pd

def get_requests(url):
    response = requests.get(url)
    output = response.json()
    return output 

def get_personal_details(url):
    r = get_requests(url)
    name = r["name"]
    company = r["company"]
    followers = r["followers"]
    followers_url = r["followers_url"]
    email = r["email"]
    return name,company,followers,followers_url,email

if __name__ == '__main__':
    details = []
    user_name = "Wes McKinney"
    user_name = user_name.replace(" ","+")
    search_url = "https://api.github.com/search/users?q={}".format(user_name)
    user = get_requests(search_url)
    user_profile_url = user["items"][0]["url"]
    name,company,followers,followers_url,email = get_personal_details(user_profile_url)
    details.append([name,company,followers,followers_url,email])
    followers_details = get_requests(followers_url)
    
    for follower in followers_details:
        profile_url = follower["url"]
        name,company,followers,followers_url,email = get_personal_details(profile_url)
        details.append([name,company,followers,followers_url,email])

    
    data = pd.DataFrame(details,columns=["name","company","followers","followers_url","email"])
    print(data)
