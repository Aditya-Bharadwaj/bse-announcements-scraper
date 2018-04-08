from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from flask import Flask,render_template,request,jsonify
import os
#import selenium
from time import sleep

def init_webdriver(path_to_driver,download_path):	
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList",2)
	profile.set_preference("browser.download.manager.showWhenStarting",False)
	profile.set_preference("browser.download.dir", download_path)
	profile.set_preference("browser.download.downloadDir", download_path)
	profile.set_preference("browser.download.defaultFolder", download_path)
	profile.set_preference("browser.helperApps.alwaysAsk.force", False)

	#driver = webdriver.Firefox(firefox_profile=profile)
	#options.add_experimental_option("prefs", preferences)
	#options.add_argument('safebrowsing-disable-download-protection')
	driver = webdriver.Firefox(path_to_driver)
	return driver

def check_for_updates(driver,url):
	driver.get(url)
	current_element = str()
	current_id = str()

	while True:
		new_element = driver.find_element_by_xpath("//img[@alt='Download XBRL']")
		new_id = new_element.get_attribute('id')
		if new_id !=  current_id:
			current_element = new_element
			#print(current_element.get_attribute('id'))
			current_element.click()	
			sleep(3)
			xml = find_new_XML(download_path)
		sleep(30)

	print(current_element.get_attribute('id'))
	#element.click()
def find_new_XML(download_path):
	files_list = sorted(os.listdir(download_path),key=lambda x: os.path.getmtime(x),reverse=True)
	xml_file= files_list[0]
	with open(xml_file) as file:
		data = file.read()
	print(data)
	#print(files_list)

download_path = 'C:\\Users\\Aditya\\Downloads\\'
os.chdir(download_path)
chromedriver_path = "C:\\Users\\Aditya\\AppData\\Local\\Programs\\Python\\Python36-32\\selenium\\webdriver\\chrome\\chromedriver.exe"
geckodriver_path = "C:\\Users\\Aditya\\AppData\\Local\\Programs\\Python\\Python36-32\\selenium\\webdriver\\firefox\\amd64\\geckodriver.exe"
if __name__ == '__main__':
	url = 'https://www.bseindia.com/corporates/ann.aspx'
	driver = init_webdriver(geckodriver_path,download_path)
	check_for_updates(driver,url)
	find_new_XML(download_path)
	#element = driver.find_element_by_xpath("//img[@alt='Download XBRL']")
	##element.click()
#print(element.text)
#soup = BeautifulSoup(r.text)

#xml = soup.findAll("img",{"alt":"Download XBRL"})

#print(xml)