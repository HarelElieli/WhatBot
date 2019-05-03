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
from preRun import preRun
import os
import easygui
import random

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

class checkC(object):

    def __init__(self):
        cancelThread = threading.Thread(target=self.run, args=())
        cancelThread.daemon = True
        cancelThread.start()

    def run(self):
        while True:
            if (keyboard.is_pressed('a')):
                #sender.kill()
                pass

class sendMis(object):

    def __init__(self):
        self.sendThread = threading.Thread(target=self.run, args=())
        self.sendThread.daemon = False

    def run(self):

        '''if (os.name == 'posix'):
                path = easygui.fileopenbox()
                filt = easygui.enterbox(title='WhatBot', msg='הכנס מסנן')
                msgBase = easygui.enterbox(title='WhatBot', msg='הכנס הודעה (%s במקום שם פרטי)')
            else:'''  # ForWin

        print('הכנס קובץ')
        path = input()
        print('הכנס מסנן')
        filt = input()
        print('הכנס הודעה')
        msgBase = input()
        shutil.copyfile(path, 'names1.csv')

        if filt:
            preRun(filt, -1)
        with open('names1.csv', 'r', encoding="utf-8") as data_file:
            csv_reader = csv.reader(data_file)
            names = []
            for line in csv_reader:
                try:
                    name = line[0]
                    names.append(name)
                except:
                    pass

        with open('temp.csv', 'w', encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            time.sleep(4)
            for name in names:
                firstName = name.split(' ', 1)[0]
                if (msgBase.find('%s') != -1):
                    msg = msgBase % firstName
                else:
                    msg = msgBase
                try:
                    sendMsg(msg, name, driver)
                    writer.writerow([name])
                except common.exceptions.NoSuchElementException as e:
                    pass
                except:
                    try:
                        backBut = WebDriverWait(driver, 10000000000000000000).until(
                            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="back-light"]')))
                        backBut.click()
                    except:
                        pass
                time.sleep(3)

    def flash(self):
        self.sendThread = threading.Thread(target=self.run, args=())
        self.sendThread.daemon = False

    def start(self):
        self.sendThread.start()

    def kill(self):
        self.sendThread._stop()

#check = checkC()

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input()

names = list()

#sender = sendMis()
while True:
    print('Type something to start an action. Leave empty to finish.')
    if(input()):

        '''if (os.name == 'posix'):
                        path = easygui.fileopenbox()
                        filt = easygui.enterbox(title='WhatBot', msg='הכנס מסנן')
                        msgBase = easygui.enterbox(title='WhatBot', msg='הכנס הודעה (%s במקום שם פרטי)')
                    else:'''  # ForWin

        print('הכנס קובץ')
        path = input()
        print('הכנס מסנן')
        filt = input()
        print('הכנס הודעה')
        msgBase = input()
        shutil.copyfile(path, 'names1.csv')

        if filt:
            preRun(filt, -1)
        with open('names1.csv', 'r', encoding="utf-8") as data_file:
            csv_reader = csv.reader(data_file)
            names = []
            for line in csv_reader:
                try:
                    name = line[0]
                    names.append(name)
                except:
                    pass

        with open('temp.csv', 'w', encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            time.sleep(4)
            for name in names:
                firstName = name.split(' ', 1)[0]
                if (msgBase.find('%s') != -1):
                    msg = msgBase % firstName
                else:
                    msg = msgBase
                try:
                    sendMsg(msg, name, driver)
                    writer.writerow([name])
                except common.exceptions.NoSuchElementException as e:
                    pass
                except:
                    try:
                        backBut = WebDriverWait(driver, 10000000000000000000).until(
                            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="back-light"]')))
                        backBut.click()
                    except:
                        pass
                time.sleep(3)
    else:
        break

driver.close()