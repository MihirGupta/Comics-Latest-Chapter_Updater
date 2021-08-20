from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date
import os
''' Newer versions of PyInstaller do not set the env variable anymore
    Now the path gets set as sys._MEIPASS:
    function resource_path(relative_path) is just takes care of it'''
def resource_path(relative_path):
    try:
        base_path = os._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# finding the current path where the .exe file is located to access the chrome driver
current_file_path = os.path.abspath(__file__)
file_path = os.path.split(current_file_path)
current_folder_path = str(file_path[0])
driver_path = current_folder_path + "\\chromedriver.exe"
new_driver_path = resource_path(driver_path)
# Configuring ChromeDriver to initiate Chrome browser in Headless mode through Selenium
option = webdriver.ChromeOptions()
option.add_argument('headless')
# Extrcting page source of url using Selenium module
driver = webdriver.Chrome(new_driver_path,options=option)
url = "https://www.asurascans.com/comics/solo-leveling/"
driver.get(url)
html_source = driver.page_source
driver.quit()
# Used BeautifulSoup Module to filter out the specific html tags to get desired data from the specific website
soup = BeautifulSoup(html_source,"lxml")
box = soup.find("div", class_ = "bixbox bxcl epcheck")
main_chap_buttons = box.find_all("div", class_ = "inepcx")
latest_chap_url = main_chap_buttons[1].a["href"]
latest_chap_number = main_chap_buttons[1].find("span", class_ = "epcur epcurlast").text
# Writing the extracted data into a text file
with open("solo-leveling-chapter-update.txt", "a") as f:
    f.write(f"Latest!! {date.today()}")
    f.write(f"""\nChapter Number : {latest_chap_number}
Chapter Url : {latest_chap_url}\n""")