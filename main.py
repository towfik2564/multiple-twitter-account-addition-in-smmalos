import time
from helpers.scraper import Scraper
from selenium.common.exceptions import TimeoutException
from helpers.fivesim import FiveSim 
import os

from helpers.functions import get_acc_info, read_txt, formatted_time, countdown
from helpers.twitter import Twitter

if __name__ == "__main__":
    proxies = read_txt('proxies.txt')

    for proxy in proxies:
        print(f'proxy connected: {proxy}')
        try: 
            users = get_acc_info()
            sim = FiveSim()
            twitter = Twitter()
            sites_to_authenticate = read_txt('websites.txt') 
            waiting_delay = 5
            time_str = formatted_time(waiting_delay)
            asian = False

            for idx, user in enumerate(users):
                scraper = Scraper('https://twitter.com/i/flow/signup')
                # time.sleep(5)
                if scraper.find_element_by_xpath('//*[contains(text(), "Sign up with phone or email")]', False):
                    asian = False
                    scraper.element_force_click_by_xpath('//*[contains(text(), "Sign up with phone or email")]')
                else:
                    scraper.element_force_click_by_xpath('//*[contains(text(), "Sign up with a phone number or email address")]')
                    asian = True

                providers = sim.get_best_providers()
                phone_info = sim.purchase_a_number(providers)
                scraper.element_send_keys('input[name="name"]', user['name'])
                scraper.element_send_keys('input[name=phone_number]', phone_info['phone'])
                scraper.select_dropdown('select[id=SELECTOR_1]', user['dob']['month'])
                scraper.select_dropdown('select[id=SELECTOR_2]', user['dob']['day'])
                scraper.select_dropdown('select[id=SELECTOR_3]', user['dob']['year'])
                
                scraper.element_force_click_by_xpath('//*[contains(text(), "Next")]')
                scraper.element_force_click_by_xpath('//*[contains(text(), "Next")]')
                scraper.element_force_click_by_xpath('//*[contains(text(), "Sign up")]')
                scraper.element_force_click_by_xpath('//span[contains(text(), "OK")]')
                    
                otp = sim.get_otp(phone_info['id'])
                if otp:
                    scraper.element_send_keys('input[name=verfication_code]', otp)
                    scraper.element_force_click_by_xpath('//span[contains(text(), "Next")]')
                else: 
                    break
                scraper.element_send_keys('input[name=password]', user['password'])
                scraper.element_force_click_by_xpath('//span[contains(text(), "Next")]')
                
                twitter.upload_pro_pic(scraper, user['img'])
                scraper.element_force_click_by_xpath('//span[contains(text(), "Next")]')

                scraper.element_send_keys('textarea', 'Hi there!')
                scraper.element_force_click_by_xpath('//span[contains(text(), "Next")]')

                username = scraper.find_elements('span[role="button"]')[0]
                user['username'] = username.text
                username.click()
                scraper.element_force_click_by_xpath('//span[contains(text(), "Next")]')
                

                print(user)
                os.system('pause')
                # scraper.element_force_click_by_xpath('//span[contains(text(), "Next")]')

                scraper.go_to_page('www.twitter.com')
                scraper.driver.execute_script("window.open('')")
                scraper.driver.switch_to.window(scraper.driver.window_handles[1])

                for site in sites_to_authenticate:
                    scraper.go_to_page(site)
                    scraper.element_click('a[href="/login"]')
                    scraper.element_click('input[id=allow]')
                    time.sleep(3)
                print(user)
                
                scraper.driver.close()
                print(f'Waiting {time_str} before next signup')
                countdown(waiting_delay)
                os.system('pause')
        except TimeoutException: 
            print('Something unpredictable occured, retrying..')
            continue

                

        

