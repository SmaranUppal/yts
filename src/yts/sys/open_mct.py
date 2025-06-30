from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenMct:
    @staticmethod
    def open_tlm_table(browser: webdriver, url: str) -> webdriver:
        browser.get(url)
        plot_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[4]/div[2]/div[2]/div[1]/div[2]/div[1]/button/span'))
        )
        plot_btn.click()
        tlm_table_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/ul/li[2]'))
        )
        tlm_table_btn = browser.find_element(By.XPATH, '/html/body/div[2]/ul/li[2]')
        tlm_table_btn.click()
        orient_timestamp_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[4]/div[2]/div[2]/div[2]/div/div/div/div[2]/table/thead/tr[1]/th[3]/div/span'))
        )
        orient_timestamp_btn.click()
        return browser


    @staticmethod
    def get_tlm(browser: webdriver) -> dict:    
        name = browser.find_element(By.XPATH, '/html/body/div/div/div[4]/div[2]/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[1]')
        value = browser.find_element(By.XPATH, '/html/body/div/div/div[4]/div[2]/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[2]')
        timestamp = browser.find_element(By.XPATH, '/html/body/div/div/div[4]/div[2]/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[3]')

        try:
            name_str = str(name.text)
            value_str = str(value.text)
            timestamp_str = str(timestamp.text)
            data = {
                'name': name_str,
                'value': value_str,
                'timestamp': timestamp_str
            }
        except Exception as e:
            data = {
                'name': None,
                'value': None,
                'timestamp': None
            }
        return data