import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


class PhantomBot:
    def __init__(self, config,):
        self.config = config
    
    @staticmethod
    def setupDriver():
        options = Options()

        options.add_extension("Phantom.crx")
        options.add_argument("--disable-gpu")

        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # options for chrome install | Разрешение на установку расширения
        os.environ['WDM8LOCAL'] = '1'

        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(), options=options)

        return driver

    def initWallet(self, driver):
        print("Init wallet...")
        driver.switch_to.window(driver.window_handles[1])

        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Use Secret Recovery Phrase')]")))
        driver.find_element(
            By.XPATH, "//button[contains(text(),'Use Secret Recovery Phrase')]").click()
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Secret phrase']")))
        driver.find_element(
            By.XPATH, "//textarea[@placeholder='Secret phrase']").send_keys(self.config["seedPhrase"])
        driver.find_element(
            By.XPATH, "//button[@class='sc-bdfBQB bzlPNH']").click()

        time.sleep(5)
        driver.find_element(
            By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Password']")))
        driver.find_element(
            By.XPATH, "//input[@placeholder='Password']").send_keys(self.config["password"])
        driver.find_element(
            By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(self.config["password"])
        driver.find_element(
            By.XPATH, "//input[@type='checkbox']").click()
        driver.find_element(
            By.XPATH, "//button[@type='submit']").click()

        time.sleep(5)
        driver.find_element(
            By.XPATH, "//button[contains(text(),'Continue')]").click()

        time.sleep(5)
        driver.find_element(
            By.XPATH, "//button[contains(text(),'Finish')]").click()

        driver.switch_to.window(driver.window_handles[0])
        print('Done\n')

    def selectWallet(self, driver):
        print("Selecting wallet...")
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Select Wallet')]")))
        main_wallet = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Select Wallet')]")
        main_wallet.click()

        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Phantom')]")))
        phantomExtension = driver.find_element(
            By.XPATH, "//button[contains(text(),'Phantom')]")
        phantomExtension.click()

        WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(2))

        driver.switch_to.window(driver.window_handles[1])

        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Connect')]")))
        popup = driver.find_element(
            By.XPATH, "//button[contains(text(),'Connect')]")
        popup.click()
        driver.switch_to.window(driver.window_handles[0])
        print("Done\n")

    def makePurchase(self, driver, url):
        print('Making purchase...')

        driver.get(url)

        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/section/div[2]/div[1]/div[2]/div/div[3]/div[3]/div/div/div/button[1]')))
        driver.find_element(By.XPATH,
                            '//*[@id="content"]/section/div[2]/div[1]/div[2]/div/div[3]/div[3]/div/div/div/button[1]').click()

        WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(1))
        time.sleep(5)
        print('Done\n')
