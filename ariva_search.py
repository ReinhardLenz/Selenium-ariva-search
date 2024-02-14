import config_webdriver_manager
import web_actions
import os
#import msvcrt
import time
import datetime
import csv
import numpy as np
import pandas as pd 
import random
import xlsxwriter
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


from locators import Locators
from datetime import date
from dateutil.relativedelta import relativedelta


import openpyxl
from openpyxl import load_workbook
import clipboard as clp

config_webdriver_manager.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "/path/to/download/dir"}}
command_result = config_webdriver_manager.driver.execute("send_command", params)

web_actions.zoom40()
config_webdriver_manager.driver.get("https://www.ariva.de/anleihen/")


#Click Cookie acceptor 
time.sleep(6)
web_actions.Select_frame_simple_XPATH(Locators.cookie_acceptor__inner_iframe_full_xpath)

web_actions.relax()
web_actions.click_operation_Xpath(Locators.cookie_acceptor_full_XP)
time.sleep(6)
config_webdriver_manager.driver.switch_to.default_content()
config_webdriver_manager.driver.execute_script("document.body.style.zoom='40%'")
#config_webdriver_manager.driver.execute_script ("window.scrollTop(0);")
time.sleep(random.randint(2,6))
#web_actions.click_operation_B_Xpath(Locators.Unternehmensanleihe_button_full_XPATH)
#hyppäsi tämän yli
web_actions.click_operation_Xpath(Locators.Low_coupon_button_XPATH)
#web_actions.click_operation_Xpath(Locators.Low_coupon_button_full_XPATH)


web_actions.relax()
web_actions.click_operation_Xpath(Locators.Refine_search_under_low_coupon_selection_XPATH)
#web_actions.click_operation_css(Locators.Refine_search_under_low_coupon_selection_CSS_selector)
web_actions.relax()

#web_actions.click_operation_Xpath(Locators.Refine_search_under_low_coupon_selection_full_XPATH)

web_actions.menu_select(Locators.Refine_search_under_low_coupon_selection_Select_currency_full_XPATH, "5")

web_actions.relax()
web_actions.click_operation_id_A(Locators.Refine_search_under_low_coupon_Rendite_low_ID)
web_actions.write_operation_xpath(Locators.Refine_search_under_low_coupon_Rendite_low_XPATH,"3")

web_actions.click_operation_id_A(Locators.Refine_search_under_low_coupon_Rendite_high_ID)
web_actions.write_operation_xpath(Locators.Refine_search_under_low_coupon_Rendite_high_XPATH,"8")
web_actions.relax()

web_actions.click_operation_id_A(Locators.Refine_search_under_low_coupon_Kupon_high_ID)
web_actions.clear_operation_A_xpath(Locators.Refine_search_under_low_coupon_Kupon_high_XPATH)
web_actions.relax()

web_actions.click_operation_id_A(Locators.Refine_search_Kupon_type_ID)
web_actions.menu_select(Locators.Refine_search_Kupon_type_XPATH,"55")
web_actions.relax()
web_actions.click_operation_id_A(Locators.Refine_Search_min_duration_ID)
web_actions.menu_select(Locators.Refine_Search_min_duration_XPATH,"1800")
web_actions.relax()
web_actions.click_operation_id_A(Locators.Refine_Search_max_duration_ID)
web_actions.menu_select(Locators.Refine_Search_max_duration_XPATH,"7300")
web_actions.click_operation_id_A(Locators.Refine_Search_type_bond_ID)
web_actions.menu_select(Locators.Refine_Search_type_bond_XPATH,"177")

web_actions.relax()

web_actions.click_operation_B_Xpath(Locators.Refine_Search_click_Search_button_XPATH)
web_actions.relax()






#web_actions.menu_select(Locators.Anleihentyp_full_XPath, 1)

html_source =config_webdriver_manager.driver.page_source
soup=BeautifulSoup(html_source, 'html.parser')
table=soup.table
table_rows = table.find_all('tr')
tables=[]
for tr in table_rows:
    td = tr.find_all('td')
    row=[]
    for i in td:
        word= i.text.strip()
        row.append(word)
    tables.append(row)
print(tables)


df = pd.DataFrame(tables)


wb = load_workbook('c:\\temp\\tutorial\\sample_ariva.xlsx')

sheet = wb.worksheets[0]


for x in range(0, 13, 1):
    sheet.insert_cols(0)

web_actions.df_to_excel(df, wb.active)
wb.save("c:\\temp\\tutorial\\sample_ariva.xlsx")


config_webdriver_manager.driver.quit()