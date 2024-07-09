import time
import csv
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Send Bulk WhatsApp messages through CSV.')
parser.add_argument('-d', '--data', required=True, help='Path to the CSV file containing contacts and messages.')
parser.add_argument('-i', '--image', default='', help='Path to the image to send.')
parser.add_argument('-l', '--login', action='store_true', help='Force login to WhatsApp Web.')
args = parser.parse_args()

# Specify the directory to store the Chrome user profile
# This is where the user's data is stored, including the login information
# Currently, it is stored in the same directory as the script
current_dir = os.path.dirname(os.path.abspath(__file__))
profile_path = os.path.join(current_dir, "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={profile_path}")

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Check if profile exists and handle login
if not os.path.exists(profile_path) or args.login:
  print("Scan the QR code to log in to WhatsApp Web")
  time.sleep(30)  # Time to scan QR code and log in

def send_message(phone, message, image_path):
  url = f"https://wa.me/{phone}?text={message}"
  driver.get(url)
  time.sleep(2)

  try:
    # Click "Continue to Chat" button
    continue_button = driver.find_element(By.LINK_TEXT, 'Continue to Chat')
    continue_button.click()
    time.sleep(2)

    # Click "use WhatsApp Web" button
    continue_button = driver.find_element(By.LINK_TEXT, 'use WhatsApp Web')
    continue_button.click()
    time.sleep(5)

    if image_path != '':
      # Click on the plus button (to attach image)
      attach_button = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Attach"]')
      attach_button.click()
      time.sleep(2)

      # Click on the "Photos & videos" option
      photos_videos_button = driver.find_element(By.CSS_SELECTOR, 'input[accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
      photos_videos_button.send_keys(image_path)
      time.sleep(2)

      # Wait for the image to be uploaded and the send button to be clickable
      send_button = WebDriverWait(driver, 20).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Send"]'))
      )
    else:
      # Wait for the text send button to be clickable
      send_button = WebDriverWait(driver, 20).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-tab="11"]'))
      )
    driver.execute_script("arguments[0].scrollIntoView(true);", send_button)
    send_button.click()
    time.sleep(5)

  except Exception as e:
    print(f"Error sending message to {phone}: {e}")

# Read the CSV file
with open(args.data, newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    phone = row['Phone']
    message = row['Message']
    send_message(phone, message, args.image)

# Close the WebDriver
driver.quit()

