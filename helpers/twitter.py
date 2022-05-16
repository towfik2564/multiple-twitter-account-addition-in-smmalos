from selenium.webdriver.common.by import By

class Twitter:

    def login(self, scraper, account):
        scraper.element_send_keys('input[name=text]', account['username'])
        scraper.element_click_by_xpath('//span[contains(text(), "Next")]')
        scraper.element_send_keys('input[name=password]', account['password'])
        scraper.element_click_by_xpath('//span[contains(text(), "Log in")]')
        if scraper.find_element('input[type=tel]', False):
            scraper.element_send_keys('input[type=tel]', account['phone'])
            scraper.element_click_by_xpath('//span[contains(text(), "Next")]')

    def upload_pro_pic(self, scraper, img):
        scraper.input_file_add_files('input[accept="image/jpeg,image/png,image/webp"]', img)
        scraper.element_click_by_xpath('//span[contains(text(), "Apply")]')

    def edit_profile(self, scraper, account):
        profile_pic_element = scraper.driver.find_elements(By.CSS_SELECTOR, 'input[accept="image/jpeg,image/png,image/webp"]')[1]
        profile_pic_element.send_keys(account['img'])
        scraper.element_click_by_xpath('//span[contains(text(), "Apply")]')
        scraper.element_click_by_xpath('//span[contains(text(), "Save")]')



    
