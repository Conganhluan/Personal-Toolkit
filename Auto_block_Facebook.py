from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from alive_progress import alive_bar
import sys

# Get the input and output
username = sys.argv[1]
if not username:
    print("Please input the username as an argument!")
    quit()
link_list  = [line.strip('\n') for line in open("Block_list.txt", "r", encoding="utf-8").readlines()]
result_file = open("result.txt","w",encoding='utf-8')

# Prepare driver
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data' % username)
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")
wait_for_login = input("")
wait = WebDriverWait(driver,3600)

# Loop
with alive_bar(len(link_list)) as bar:
    for link in link_list:
        driver.get(link)
        # Check if this user is banned already
        try:
            driver.find_element("xpath", '//div[@aria-label="See Options"]')
        except NoSuchElementException:
            print(f"{link:55} already blocked/banned by Facebook")
            result_file.write(f"{link:55} already blocked/banned by Facebook")
            bar()
            continue
        # Bypass the Facebook anti-script
        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="x1uvtmcs x4k7w5x x1h91t0o x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1n2onr6 x1qrby5j x1jfb8zj"])[1]')))
        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="x1uvtmcs x4k7w5x x1h91t0o x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1n2onr6 x1qrby5j x1jfb8zj"])[2]')))
        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="x1uvtmcs x4k7w5x x1h91t0o x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1n2onr6 x1qrby5j x1jfb8zj"])[3]')))
        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="x1uvtmcs x4k7w5x x1h91t0o x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1n2onr6 x1qrby5j x1jfb8zj"])[4]')))
        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="x1uvtmcs x4k7w5x x1h91t0o x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1n2onr6 x1qrby5j x1jfb8zj"])[5]')))
        wait.until(EC.invisibility_of_element_located((By.XPATH, '(//div[@class="x1uvtmcs x4k7w5x x1h91t0o x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1n2onr6 x1qrby5j x1jfb8zj"])[6]')))
        # Click "..."
        while True:
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="See Options"]'))).click()
                break
            except:
                continue
        # Click "Block"
        wait.until(lambda x: x.find_element("xpath", '//span[text()="Block"]')).click()
        # Click "Ban all ..."
        wait.until(lambda x: x.find_element("xpath", '(//div[@class="xod5an3 x16n37ib x14vqqas x1n2onr6 xqcrz7y"])[2]/div[1]/div[1]/div[1]')).click()
        # Click "Confirm"
        wait.until(lambda x: x.find_element("xpath", '//div[@aria-label="Confirm"]')).click()
        # Click "Confirm" the second time
        wait.until(lambda x: x.find_element("xpath", '(//span[text()="Confirm"])[2]')).click()
        print(f"{link:55} newly blocked")
        result_file.write(f"{link:55} newly blocked")
        bar()

result_file.close()
driver.quit()
