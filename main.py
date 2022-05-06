import time
from helpers.scraper import Scraper
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os
from os import listdir
from os.path import isfile, join
import random

def get_accounts():
    with open("accounts.txt", "r") as file:
        data = file.read()
        list = data.split("\n")
        images = [f for f in listdir('images') if isfile(join('images', f))]
        accounts = []
        for data in list:
            index = random.randint(0,len(images)-1)
            image = os.path.abspath(os.getcwd()) + '\images\\' + images[index]
            data = {
                'username': data.split(':')[0],
                'password': data.split(':')[1],
                'phone': data.split(':')[2],
                'img': image
            }
            accounts.append(data)
        return accounts
def setup_profile(scraper, account):
    scraper.element_click_by_xpath('//span[contains(text(), "Set up profile")]')
    scraper.input_file_add_files('input[accept="image/jpeg,image/png,image/webp"]', account['img'])
    scraper.element_click_by_xpath('//span[contains(text(), "Apply")]')
    scraper.element_click_by_xpath('//span[contains(text(), "Next")]')

def edit_profile(scraper, account):
    scraper.element_click('a[data-testid=editProfileButton]')
    # scraper.go_to_page('https://twitter.com/settings/profile')
    profile_pic_element = scraper.driver.find_elements(By.CSS_SELECTOR, 'input[accept="image/jpeg,image/png,image/webp"]')[1]
    profile_pic_element.send_keys(account['img'])
    scraper.element_click_by_xpath('//span[contains(text(), "Apply")]')
    scraper.element_click_by_xpath('//span[contains(text(), "Save")]')

if __name__ == "__main__":
    accounts = get_accounts()
    for idx, account in enumerate(accounts): 
        if idx != 0:
            print('waiting 20secs before next login')
            time.sleep(20)
        scraper = Scraper('https://twitter.com/i/flow/login')
        scraper.element_send_keys('input[name=text]', account['username'])
        scraper.element_click_by_xpath('//span[contains(text(), "Next")]')
        scraper.element_send_keys('input[name=password]', account['password'])
        scraper.element_click_by_xpath('//span[contains(text(), "Log in")]')
        if scraper.find_element('input[type=tel]', False):
            scraper.element_send_keys('input[type=tel]', account['phone'])
            scraper.element_click_by_xpath('//span[contains(text(), "Next")]')
        time.sleep(2)
        scraper.element_click('a[aria-label=Profile]')
        time.sleep(2)
        
        if scraper.find_element_by_xpath('//span[contains(text(), "Set up profile")]', False): 
            setup_profile(scraper, account)
        else:
            edit_profile(scraper, account)
        
        scraper.go_to_page('https://smmalos.xyz/')
        scraper.element_click('a[href="/login"]')
        scraper.element_click('input[id=allow]')
        scraper.driver.close()

