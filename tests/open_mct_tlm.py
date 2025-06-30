from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from yts.sys.open_mct import OpenMct


url = "http://localhost:8080/#/browse/example.taxonomy:spacecraft/example.taxonomy:pwr.v?tc.mode=local&tc.startDelta=900000&tc.endDelta=0&tc.timeSystem=utc&view=plot-single"
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser = OpenMct.open_tlm_table(browser, url)
while True:
    print(OpenMct.get_tlm(browser))
    sleep(1)





