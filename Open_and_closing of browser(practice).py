import os
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

def Open_close_browser():
	
	browserExe = "firefox.exe" #"chrome.exe" for chrome termination

	browser = webdriver.Firefox(executable_path=r'C:\Users\Test\Miniconda3\Lib\site-packages\notebook\tests\selenium\geckodriver-v0.21.0-win64\geckodriver.exe') #geckdriver.exe is in this folder
	#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
	browser.get('https://kuselokusi.github.io')

	time.sleep(5) #stops for afew seconds

	os.system("taskkill /f /im "+browserExe) #to terminate chrome browser in windows
	#os.system("pkill "+browserExe) for linux system

for x in range(1,50): #repeat ipen_close_browser() afew times
		print("Now on iteration..."+str(x))
		Open_close_browser()