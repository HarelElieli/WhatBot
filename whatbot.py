from selenium import webdriver
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import shutil
import csv
import keyboard
import threading
from multiprocessing import Process
from preRun import preRun
import os

def sendMsg(msg, name, driver):
    print(name)
    newChat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div')
    newChat.click()
    chatName = driver.find_element_by_xpath('//input[@title="חפש אנשי קשר"]')
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

def fullRun():
    print('הכנס שם קובץ CSV')  # Collect data for preparing messages
    fileName = input()
    path = pathBase % fileName
    print('הכנס מסנן')
    filt = input()
    print('הכנס הודעה')
    msgBase = input()

    namesPath = pathBase % namesToDo_fileName
    shutil.copyfile(path, namesPath)  # Duplicate the names original CSV for manipultaion

    if filt:
        preRun(filt, -1, pathBase, namesToDo_fileName)  # Manipulate the CSV copy and filter it before running
    with open(namesPath, 'r', encoding="utf-8") as data_file:  # Prepare the names list for a run
        csv_reader = csv.reader(data_file)
        names = []
        for line in csv_reader:
            try:
                name = line[0]
                names.append(name)
            except:
                pass

    time.sleep(2)

    count = 0

    for name in names:  # Send message to all names list
        firstName = name.split(' ', 1)[0]
        if (msgBase.find('%s') != -1):  # Prepare the message before sending
            msg = msgBase % firstName
        else:
            msg = msgBase

        try:  # Try sending the message
            sendMsg(msg, name, driver)  # Send message
            count = count + 1
            tempPath = pathBase % 'temp'  # Create a temporary file for listing the remaining names to send message to
            with open(namesPath, 'r', encoding='utf-8', newline='') as nameFile:
                delFlag = True
                csv_reader = csv.reader(nameFile)
                with open(tempPath, 'w', encoding='utf-8', newline='') as tempFile:
                    csv_writer = csv.writer(tempFile)
                    for line in csv_reader:
                        if (line[0] != name):  # Document all the names but the one tjat just got a message
                            csv_writer.writerow(line)
                            delFlag = False  # To make sure the file is not empty
            shutil.move(tempPath, namesPath)
            if (delFlag):  # Removes the file if it is empty
                os.remove(namesPath)

        except keyboard:
            print('Bye')
            continue

        except common.exceptions.NoSuchElementException as e:  # Didn't find the "Back" button.
            pass

        except:  # Click the "Back" button.
            backBut = WebDriverWait(driver, 10000000000000000000).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="back-light"]')))
            backBut.click()

        time.sleep(3)

    print(str(count) + ' messages have been sent out of ' + str(names.__len__()))

def count():
    for i in range(1,10):
        time.sleep(1)
        print(i)

'''
driver = webdriver.Chrome() #Create a drier and open whatsapp web
driver.get("https://web.whatsapp.com/")

input('Scan the barcode, wait for it to load and press Enter.')

names = list() #Create the list of names to send messages to.
pathBase = '/Volumes/M P/contactsFiles/%s.csv' #Path for all CSV files
namesToDo_fileName = 'namesToDo' '''

while True:

    if(input('Type something to start an action, Leave empty to finish: ')):

        fullSend_prcs = Process(target=count())
        fullSend_prcs.start()
        print('m')
    else:
        break

driver.close()