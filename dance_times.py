from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def studio68(path):
    """ Function to create a dance timetable from Studio68 and save as csv """

    url = "http://studio68london.net/work/timetable/"
    page = urlopen(url)
    soup = BeautifulSoup(page, "html5lib")
    content = soup.find("div", class_="real-content")
    tr = (content.find_all("tr"))

    list_ = []
    for item in tr:
        try:
            name = (item.find("td", width="184").getText())
            if item.find("td", width="206"):
                style = item.find("td", width="206").getText()
            elif item.find("td", width="205"):
                style = item.find("td", width="205").getText()
            if item.find("td", width="113"):
                time = item.find("td", width="113").getText()
            elif item.find("td", width="114"):
                time = item.find("td", width="114").getText()
            level = (item.find("td", width="99").getText())
            studio = (item.find("td", width="57").getText())
            price = (item.find("td", width="69").getText())
            list_.append(([name, style, time, level, studio, price]))
        except:
            AttributeError

    result = pd.DataFrame(list_)
    result.to_csv(path)


if __name__ == "__main__":
    studio68(path)