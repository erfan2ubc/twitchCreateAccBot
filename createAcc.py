from selenium import webdriver
from selenium.webdriver.chrome.service import Service

email = "mohammaderfan22@hotmail.com"
password = "erfan@22"
url = "https://www.stealmylogin.com/demo.html"

# Set up the Chrome driver service
service = Service("C:\\Users\\moham\\Desktop\\chromedriver.exe")

# Start the Chrome driver
driver = webdriver.Chrome(service=service)

# Navigate to the URL
driver.get(url)

