import time

import requests
from bs4 import BeautifulSoup
from plyer import notification as n


def notify(title, msg):
    n.notify(
        title=title,
        message=msg,
        app_icon="warnning.ico",
        timeout=10
    )


def scrap_data(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    # notify("Chintan","Stop Spread of COVID-19 virus")
    while True:

        webdata = scrap_data("https://www.mohfw.gov.in/")
        # print(webdata)
        soup = BeautifulSoup(webdata, 'html.parser')
        # print(soup.prettify())
        data_str = ""
        for table in soup.find_all('tbody')[1].find_all('tr'):
            data_str += table.get_text()
        data_str = data_str[1:]
        data_list = data_str.split("\n\n")
        states = ['Gujarat']
        for item in data_list[0:24]:
            state_list = item.split("\n")
            if state_list[1] in states:
                title = 'case of Covid-19'
                text = f"State : {state_list[1]}\nIndian:{state_list[2]}\nForegin: {state_list[3]}\nNo. of Deaths: {state_list[5]}"
                notify(title, text)
        time.sleep(20)
