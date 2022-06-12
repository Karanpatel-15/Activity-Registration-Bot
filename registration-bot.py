from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#Activity Detail
link = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata/ReserveTime/StartReservation?pageId=b3b9b36f-8401-466d-b4c4-19eb5547b43a&buttonId=cd60113e-888a-4371-a894-9b0345735f5a&culture=en&uiCulture=en"
date = "Monday January 3, 2022"
time = "07:45"
numberOfPeople = '2'

#Personal details
number = "6139815014"
email = "inbox.kpatel@yahoo.ca"
name = "Karan Patel"

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get(link)

reservationCount = driver.find_element_by_name('ReservationCount')
reservationCount.clear()
reservationCount.send_keys(numberOfPeople)

countSubmit = driver.find_element_by_class_name('mdc-button__ripple')
countSubmit.click()

dateCount = 2
while(True): 
    dates = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div[2]/div[' + str(dateCount) + ']/a')
    if date in dates.get_attribute('innerHTML'):
        dates.click()
        break
    dateCount+=1
timeCount = 1
while(True):
    times = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div[2]/div[' + str(dateCount) + ']/ul/li['+str(timeCount)+']')
    if time in times.get_attribute('innerHTML'):
        times.click()
        break
    timeCount+=1

number = driver.find_element_by_name('PhoneNumber')
number.send_keys('6139815014')

email = driver.find_element_by_name('Email')
email.send_keys('inbox.kpatel@gmail.com')

timeSelection = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/form/div[2]/div/div[4]/div[1]/label/input')
timeSelection.send_keys(name)

Submit = driver.find_element_by_class_name('mdc-button__ripple')
Submit.click()

finalSubmit = driver.find_element_by_xpath('/html/body/div/main/div[2]/div/form/div[8]/button/span')
# finalSubmit.click()
