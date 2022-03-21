# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:37:00 2021

@author: Usuario
"""


from selenium import webdriver
import pandas as pd
import re
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "http://webtool.framenetbr.ufjf.br/index.php/webtool/report/frame/main"
driver.get(url)

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

frame_title = driver.find_elements_by_class_name('tree-title')
frame_list = []
for x in frame_title:
    frame_list.append(x.text)
frame_list = [x for x in frame_list if x != "Frames"]
    
driver.find_elements_by_class_name('tree-node')[6].click()

frame_name_list = []
frame_definition_list = []
lexical_units_list = []

from time import sleep
for x in range(0, len(frame_list)):
    pasta_frames = driver.find_elements_by_class_name('tree-node')[x].click()
    sleep(2)
    if len(driver.find_elements_by_class_name('tableLU')) > 0:
        frame_name = driver.find_elements_by_class_name('frameName')
        frame_definition = driver.find_elements_by_class_name('text')
        lexical_units = driver.find_elements_by_class_name('tableLU') 
        for y in frame_name:
            frame_name_list.append(y.text)
        for z in frame_definition:
            frame_definition_list.append(z.text)
        for l in lexical_units:
            lexical_units_list.append(l.text)
    else:
        continue

driver.close()
    
    
df = pd.DataFrame()

df['frame_name'] = frame_name_list
df['frame_definition'] = frame_definition_list
df['lexical_units_list'] = lexical_units_list

df.to_csv('framenet_dados.csv')



