from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/reactiontime')
start = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]')
start.click()
box = driver.find_element_by_class_name('css-saet2v')
print(box.get_attribute('class').split(' '))
while True:
    if box.get_attribute('class').split(' ')[0] == 'view-waiting':
        continue
    elif box.get_attribute('class').split(' ')[0] == 'view-go':
        box.click()
    elif box.get_attribute('class').split(' ')[0] == 'view-result':
        sleep(1)
        box.click()
    else:
        break  # add
driver.close()
print('Completed')
