import requests
from bs4 import BeautifulSoup
import pandas as pd 

def studio68(output_path):
    url = "http://studio68london.net/work/timetable/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    tables = soup.findAll("table",{"width":728})
    data = pd.read_html(str(tables[0]))[0]
    data.to_csv(output_path, index=False, header=0, encoding="utf-8")
    
    
if __name__ == "__main__":
    studio68("/Users/ssathiamoorthi/Documents/result.csv")
    
