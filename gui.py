#!/usr/bin/env python
import time
import sys
from PyPDF2 import PdfFileReader
import re
import csv
from selenium import webdriver
import tkinter as tk
from tkinter import ttk
import os
import requests
#pdf global variable
serialnumber=1

#Adding first row in the data.csv file
#change path here---------->>>>>>>>>>where ur gui file save now goto line no. 246 and make changes there
path2='/home/kabir/Desktop/data.csv'
data=["S.No.","Title","Author","Pages","Email Address","Subject"]
with open(path2,'w') as writefile:
	writer=csv.writer(writefile)
	writer.writerow(data)
#from PIL import Image, ImageTk
from tkinter import messagebox
win = tk.Tk()
win.title("                                PDF Extractor")

#You can set the geometry attribute to change the root windows size
win.geometry("500x300") #You want the size of the app to be 500x500
win.resizable(0, 0) #Don't allow resizing in the x or y direction
#to create keyword column
label = ttk.Label(win, text='::Welcome::')
label.grid(row=0,column=3,sticky=tk.W)
#for blank space
ttk.Label(win, text='                      ').grid(row=1,column=0,sticky=tk.W)
ttk.Label(win, text='                      ').grid(row=2,column=0,sticky=tk.W)
ttk.Label(win, text='                      ').grid(row=3,column=0,sticky=tk.W)
ttk.Label(win, text='                      ').grid(row=4,column=0,sticky=tk.W)
ttk.Label(win, text='                      ').grid(row=5,column=0,sticky=tk.W)

keyword_label = ttk.Label(win, text='Keyword : ')
keyword_label.grid(row=7,column=2,sticky=tk.W)
#create entry box
keyword_var = tk.StringVar()
keyword_entrybox=ttk.Entry(win,width=16,textvariable= keyword_var)
keyword_entrybox.grid(row=7,column=3)
keyword_entrybox.focus()
ttk.Label(win, text='  ').grid(row=8,column=4,sticky=tk.W)
#links
	
ttk.Label(win, text='                      ').grid(row=9,column=0,sticky=tk.W)




#https://www.sciencedirect.com/search/advanced?qs=blockchain&accessTypes=openaccess&lastSelectedFacet=accessTypes
#science direct links crawl
def science():
	key=keyword_var.get()
	messagebox.showinfo( "Welcome to ", "searching your "+key)	
	sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
	G_url=("https://www.sciencedirect.com/search/advanced?qs="+key+"&accessTypes=openaccess&lastSelectedFacet=accessTypes")
	driver.get(G_url)
	print(G_url)
#link=driver.find_elements_by_xpath('//a[@class="download-link"]')
	link = driver.find_elements_by_css_selector("a.download-link")
	url = [lik.get_attribute("href") for lik in link]
	print(url)
	for i in url:
		print("This file no. {} and Pending Files {} ".format(serialnumber,len(url)-serialnumber))
		dele(extract(down(i)))
	driver.close()
	print("******Completed******")
	messagebox.showinfo("Results Available","Click Result Button")

#for IEEE
def ieee():
	key=keyword_var.get()
	messagebox.showinfo( "Welcome to ","Searching Your "+key+"error~403~")	
	sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
	G_url= "https://ieeexplore.ieee.org/search/searchresult.jsp?queryText="+key+"&highlight=true&returnFacets=ALL&returnType=SEARCH&openAccess=true"
	driver.get(G_url)
	print(G_url)
#link=driver.find_elements_by_xpath('//*[@id="xplMainContent"]/div[2]/div[2]/xpl-results-list/div[3]/xpl-results-item/div[1]/div[2]/ul/li[3]/div/a')
#link = selenium.getAttribute("css=@href")
	link = driver.find_elements_by_css_selector("a.icon-pdf")
	url = [lik.get_attribute("href") for lik in link]
	for i in url:
		print("This file no. {} and Pending Files {} ".format(serialnumber,len(url)-serialnumber))
		dele(extract(down(i)))

	driver.close()
	print("******Completed******")
	messagebox.showinfo("Results Available","Click Result Button")
