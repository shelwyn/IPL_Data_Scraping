from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

class IPL:
    def most_runs():
        url = "https://www.iplt20.com/stats/2021/most-runs"
        options = Options()
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get(url)
        time.sleep(1)

        class_names = ['top-players__player', 'top-players__m', 'top-players__inns', 'top-players__no',
                       'top-players__r', 'top-players__hs ', 'top-players__a '
            , 'top-players__b', 'top-players__sr', 'top-players__100s', 'top-players__50s', 'top-players__4s',
                       'top-players__6s']

        data_frame = pd.DataFrame()
        for Class in class_names:
            data_i = []
            values = driver.find_elements_by_class_name(Class)
            for value in values:
                data_i.append(value.text.replace("\n", ""))
            data_frame[data_i[0]] = data_i
        data_frame.to_csv(r'c:\IPL\runs.csv', index=False)

        driver.close()

    def most_wickets():
        url = "https://www.iplt20.com/stats/2021/most-wickets"
        options = Options()
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get(url)
        time.sleep(1)

        class_names = ['top-players__player', 'top-players__m', 'top-players__inns', 'top-players__ov','top-players__r  ',
                       'top-players__w', 'top-players__bbi', 'top-players__a '
            , 'top-players__e', 'top-players__sr', 'top-players__4w', 'top-players__5w']

        data_frame = pd.DataFrame()
        for Class in class_names:
            data_i = []
            values = driver.find_elements_by_class_name(Class)
            for value in values:
                data_i.append(value.text.replace("\n", ""))
            data_frame[data_i[0]] = data_i
        data_frame.to_csv(r'c:\IPL\wickets.csv', index=False)

        driver.close()

start=IPL
start.most_runs()
start.most_wickets()