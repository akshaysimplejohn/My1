import subprocess
import sys  
result = subprocess.run([sys.executable, '-m', 'pip', 'install', 'selenium'], 
                                check=True, capture_output=True, text=True)
print("Selenium installed successfully!")
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Set up Firefox options (optional)
options = Options()
#options.add_argument("--headless") # Uncomment this line to run without opening the UI

# Initialize the WebDriver
# Selenium Manager automatically handles the driver executable in modern versions
driver = webdriver.Firefox(options=options)

try:
    # Navigate to YouTube
    print("Navigating to YouTube...")
    driver.get("https://www.youtube.com")

    # Wait for 5 seconds to see the result
    time.sleep(5)

    # Verify the title
    print(f"Page title is: {driver.title}")

except Exception as e:
    print(f"An error occurred: {e}")
