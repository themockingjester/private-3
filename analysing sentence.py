import sys
#note: for running this app your pc must have geckodriver.exe file
#Developer : Yash-mathur
#language-python3
import time
from selenium import webdriver
browser = webdriver.Firefox(executable_path=r'D:\New folder\geckodriver.exe')

browser.get('https://translate.google.com')

more = browser.find_element_by_css_selector('.tl-more')
more.click()

hindi = browser.find_element_by_css_selector('div.language_list_item_wrapper-hi:nth-child(39) > div:nth-child(2)')
hindi.click()


english_more = browser.find_element_by_css_selector('.sl-more')
english_more.click()
english = browser.find_element_by_css_selector('div.language_list_section:nth-child(3) > div:nth-child(22)')
english.click()
entry = browser.find_element_by_css_selector('#source')
entry.click()
entry.send_keys('i went that place')
time.sleep(2)
youranswer = browser.find_element_by_css_selector('.tlid-result-transliteration-container > div:nth-child(1)')
a=youranswer.text
print('youranswer '+a)
clear = browser.find_element_by_css_selector('.clear > div:nth-child(1)')
clear.click()
#entry.click()
entry.send_keys('i gone there\n')
time.sleep(2)
myanswer = browser.find_element_by_css_selector('.tlid-result-transliteration-container > div:nth-child(1)')
b=myanswer.text
print('correct answer '+b)
ctr=0
for i in a:
    if i in b:
        ctr+=1
    else:
        pass
    
result=(ctr/len(a))*100
print('your answer was '+str(format("%.2f" % result))+'% correct')

#entry.send_keys('text you required')
#text_printed = browser.find_element_by_css_selector('.tlid-result-transliteration-container > div:nth-child(1)')
#text_printed=text_printed.text


