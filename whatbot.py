from selenium import webdriver
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import shutil
import csv
from tempfile import NamedTemporaryFile
import keyboard
import threading
from preRun import preRun
import os
import caffeine
import easygui
import random
import sys
import subprocess

def sendMsg(msg, name, driver):
    print(name)
    newChat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div')
    newChat.click()

    try:
        chatName = driver.find_element_by_xpath('//input[@title="חפש אנשי קשר"]') #Bug fix
    except:
        chatName = driver.find_element_by_xpath('//input[@title="Search contacts"]')

    chatName.send_keys(name)
    time.sleep(2)
    if(name.isdigit()):
        user = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/span/span')
    else:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    time.sleep(2)
    button.click()

driver = webdriver.Chrome() #Create a driver and open whatsapp web
driver.get("https://web.whatsapp.com/")
input('Scan the barcode, wait for it to load and press Enter.')

names = list() #Create the list of names to send messages to.
pathBase = '/Volumes/M P/contactsFiles/%s.csv' #Path for all CSV files
namesToDo_fileName = 'namesToDo'

while True:

    if(input('Type something to start an action, Leave empty to finish: ')):

        fileName = input('הכנס שם קובץ CSV: ') #Collect data for preparing messages
        path = pathBase % fileName
        filt = input('הכנס מסנן: ')
        filtNum = int(input('הכנס את מספר המילה באיש הקשר לפיה תרצה לסנן: '))
        msgBase = input('הכנס הודעה: ')

        namesPath = pathBase % namesToDo_fileName
        shutil.copyfile(path, namesPath) #Duplicate the names original CSV for manipultaion

        if filt:
            preRun(filt, filtNum, pathBase, namesToDo_fileName) #Manipulate the CSV copy and filter it before running
        with open(namesPath, 'r', encoding="utf-8") as data_file: #Prepare the names list for a run
            csv_reader = csv.reader(data_file)
            names = []
            for line in csv_reader:
                try:
                    name = line[0]
                    names.append(name)
                except:
                    pass

        time.sleep(4)

        count = 0

        caffeine.on(display=True) #Prevents screen to sleep on MacOS

        for name in names: #Send message to all names list

            firstName = name.split(' ', 1)[0]
            if (msgBase.find('%s') != -1): #Prepare the message before sending
                msg = msgBase % firstName
            else:
                msg = msgBase

            try: #Try sending the message
                sendMsg(msg, name, driver) #Send message
                tempPath = pathBase % 'temp' #Create a temporary file for listing the remaining names to send message to
                with open(namesPath, 'r', encoding='utf-8', newline='') as nameFile:
                    delFlag = True
                    csv_reader = csv.reader(nameFile)
                    with open(tempPath, 'w', encoding='utf-8', newline='') as tempFile:
                        csv_writer = csv.writer(tempFile)
                        for line in csv_reader:
                            if (line[0] != name): #Document all the names but the one that just got a message
                                csv_writer.writerow(line)
                                delFlag = False #To make sure the file is not empty
                shutil.move(tempPath, namesPath)
                if (delFlag): #Removes the file if it is empty
                    os.remove(namesPath)
                count = count + 1
            except common.exceptions.NoSuchElementException as e: #Didn't find the "Back" button.
                pass
            except: #Click the "Back" button.
                backBut = WebDriverWait(driver, 10000000000000000000).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="back-light"]')))
                backBut.click()
            time.sleep(3)

        caffeine.off() #Allows screen to sleep from now and on

        print(str(count) + ' messages have been sent out of ' + str(names.__len__()))
    else:
        break

driver.close()