from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
import os
import sys
import logging
import requests



pwd = sys.path[0]
logging.basicConfig(filename=os.path.join(pwd,'logs.txt'),level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')


driver_path =  os.path.join(pwd,'chromedriver')
options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

drvr = webdriver.Chrome(options = options, executable_path = driver_path)
drvr.get("https://www.atg.party/ "); 
r = requests.get("https://www.atg.party/")

logging.info('opened log in page. response code is {} and time elapsed is {}'.format(r.status_code, r.elapsed.total_seconds()))
drvr.find_element_by_xpath('/html/body/div[5]/header/div[1]/div[2]/div/ul/li[2]/a').click()
 
x1 = '/html/body/div[5]/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[1]/div[1]/input'
x2 = '/html/body/div[5]/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[1]/div[2]/input'
x3 = '/html/body/div[5]/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button'
wait = WebDriverWait(drvr, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, x1)))
drvr.find_element_by_xpath(x1).send_keys("wiz_saurabh@rediffmail.com")
drvr.find_element_by_xpath(x2).send_keys("Pass@123")
drvr.find_element_by_xpath(x3).click()
logging.info('Logged in to website')

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="create-btn-dropdown"]')))

drvr.get('https://www.atg.party/article')

inp = drvr.find_element_by_xpath("//*[@id=\"cover_image\"]");
folderpath = "/Users/nandan/cd/rpp/atg/"
imgpath = os.path.join(folderpath, 'globe.jpeg')
if (os.stat(imgpath).st_size // (1024 * 1024)) > 0:
    logging.warning("compressing image since it is greater than 1 mb")
    newimagepath = os.path.join(folderpath, 'globe_compressed.jpeg')
    image = Image.open(imgpath)
    image.save(newimagepath,quality=20,optimize=True)
    inp.send_keys(newimagepath);
else:
    
    inp.send_keys(imgpath);
logging.info("image is uploaded")
drvr.find_element_by_xpath('//*[@id="title"]').send_keys("Accross the globe")
drvr.find_element_by_xpath('//*[@id="description"]/div/div[1]/div[1]/div/div').send_keys("the globe is round and so are we")
wait.until(EC.invisibility_of_element_located((By.XPATH,'//*[@id="upload_progress"]')))
drvr.find_element_by_xpath('//*[@id="hpost_btn"]').click()
logging.info("text written and submitted")
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="closeModal"]')))
drvr.find_element_by_xpath('//*[@id="closeModal"]').click()


# The following test needs to be done using python selenium:
# •    Open website:  https://www.atg.party/ Please check the following conditions:
# o    HTTP response code = 200
# o    Response time of page load should be logged
# •    Click on LOGIN. use the following email/password: wiz_saurabh@rediffmail.com / Pass@123
# •    Go to the URL:https://www.atg.party/article . Fill in the title and description. Upload a cover image. Click on POST. The page will redirect to a new page as the article gets posted. Log the URL of the new page.
 
# Logs from the run should get stored on both console and a text file locally.
 
# DM 1 min video (explaining how automation works mentioning all the deliverable points) as a report to your hiring manager. Github link will be asked later after task 2.
# PS: Task highly preferred on Linux. Try VirtualBox or dual boot. Windows task can be submitted just in case Linux wasn't possible.