import os

#install selenium using the line below
#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#install config using the line below
#pip install config
import config
import time

#install playsound using the line below
#pip install playsound
from playsound import playsound

#install requests using the line below
#pip install requests
import requests

#copy and paste the youtube link below to install the Chrome Web Driver for Selenium in python
#https://youtu.be/2WVxzRD6Ds4

os.environ['PATH'] += r"C:\Users\hp\Desktop\A\CS\Selenium_dev"
driver = webdriver.Chrome()
driver.get("https://sakai.ug.edu.gh/portal/site/!gateway/tool/!gateway-110")

driver.implicitly_wait(20)

def Login(studID, pin):
    student_id = driver.find_element(By.ID,'eid')
    password = driver.find_element(By.ID,'pw')

    student_id.send_keys(str(studID))
    password.send_keys(str(pin))

    loginbtn = driver.find_element(By.ID,'submit')
    loginbtn.click()

#Substitute the parameters 'studentID' and 'pin' with your student ID and pin below
#Example
#Login(1234567, 01234)
Login(studentID, pin)

#Default grades
#Each value of the 'grade' dictionary can be replaced with your default grades
grade = {
    'DCIT200_grade' : '-',
    'DCIT202_grade' : '-',
    'DCIT204_grade' : 'A (99.33%)',
    'DCIT206_grade' : 'C (62.5%) [50/80]',
    'DCIT208_grade' : 'A (98.15%)',
    'DCIT212_grade' : 'A (87.5%) [35/40]',
    }

#Navigate to each course's gradebook and assign the grade for each course
try:
    #works if you have starred the courses
    btn200 = driver.find_element(By.CSS_SELECTOR,'a[title="DCIT 200 1 S2-2021"]')
    btn200.click()
    btn200_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn200_gradebook.click()
    grade200 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn202 = driver.find_element(By.CSS_SELECTOR,'a[title="DCIT 202 1 S2-2021"]')
    btn202.click()
    btn202_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn202_gradebook.click()
    grade202 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn204 = driver.find_element(By.CSS_SELECTOR,'a[title="DCIT 204 1 S2-2021"]')
    btn204.click()
    btn204_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn204_gradebook.click()
    grade204 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn206 = driver.find_element(By.CSS_SELECTOR,'a[title="DCIT 206 1 S2-2021"]')
    btn206.click()
    btn206_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn206_gradebook.click()
    grade206 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn208 = driver.find_element(By.CSS_SELECTOR,'a[title="DCIT 208 1 S2-2021"]')
    btn208.click()
    btn208_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn208_gradebook.click()
    grade208 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn212 = driver.find_element(By.CSS_SELECTOR,'a[title="DCIT 212 1 S2-2021"]')
    btn212.click()
    btn212_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn212_gradebook.click()
    grade212 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

except:
    #if the courses have not been starred this block runs
    btn200 = driver.get("https://sakai.ug.edu.gh/portal/site/DCIT-200-1-S2-2021")
    btn200_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn200_gradebook.click()
    grade200 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn202 = driver.get("https://sakai.ug.edu.gh/portal/site/DCIT-202-1-S2-2021")
    btn202_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn202_gradebook.click()
    grade202 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn204 = driver.get("https://sakai.ug.edu.gh/portal/site/DCIT-204-1-S2-2021")
    btn204_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn204_gradebook.click()
    grade204 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn206 = driver.get("https://sakai.ug.edu.gh/portal/site/DCIT-206-1-S2-2021")
    btn206_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn206_gradebook.click()
    grade206 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text
  
    btn208 = driver.get("https://sakai.ug.edu.gh/portal/site/DCIT-208-1-S2-2021")
    btn208_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn208_gradebook.click()
    grade208 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

    btn212 = driver.get("https://sakai.ug.edu.gh/portal/site/DCIT-212-1-S2-2021")
    btn212_gradebook = driver.find_element(By.CSS_SELECTOR,'a[title="Gradebook - For storing, calculating, and viewing grades"]')
    btn212_gradebook.click()
    grade212 = driver.find_element(By.CSS_SELECTOR,'span[aria-labelledby="summaryCourseGradeLabel"]').text

#Check whether any grade has changed or not
while True:

    if grade['DCIT200_grade'] == grade200 and grade['DCIT202_grade'] == grade202 and grade['DCIT204_grade'] == grade204 and grade['DCIT206_grade'] == grade206 and grade['DCIT208_grade'] == grade208 and grade['DCIT212_grade'] == grade212:   
        #executes if no grade has been uploaded yet
        print('\nNo grade has been uploaded.')
        print('DCIT 200: ' + grade200)
        print('DCIT 202: ' + grade202)
        print('DCIT 204: ' + grade204)
        print('DCIT 206: ' + grade206)
        print('DCIT 208: ' + grade208)
        print('DCIT 212: ' + grade212)
        print('')
        time.sleep(30)
        driver.refresh()
        break

    elif grade['DCIT200_grade'] != grade200 or grade['DCIT202_grade'] != grade202 or grade['DCIT204_grade'] != grade204 or grade['DCIT206_grade'] != grade206 or grade['DCIT208_grade'] != grade208 or grade['DCIT212_grade'] != grade212:
        #executes if a grade(s) has been uploaded
        print('\nGrade has been uploaded.')
        print('DCIT 200: ' + grade200)
        print('DCIT 202: ' + grade202)
        print('DCIT 204: ' + grade204)
        print('DCIT 206: ' + grade206)
        print('DCIT 208: ' + grade208)
        print('DCIT 212: ' + grade212)
        #driver.get(whatsapp)
        playsound("Legacy.mp3")
        break
        
        
    else:
        print("Refreshing....")
        driver.refresh()
        


