from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

class WhatsAppScraper:
    def __init__(self, wait_time=15):
        options = Options()
        options.add_argument("--user-data-dir=whatsapp_profile")  # Persist login
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.wait_time = wait_time

    def login(self):
        print("🔓 Scan the QR code in the opened browser...")
        self.driver.get("https://web.whatsapp.com")
        sleep(self.wait_time)

    def get_messages(self):
        messages = []
        message_blocks = self.driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]')
        for block in message_blocks[-5:]:  # limit to latest 5 messages for now
            try:
                sender = block.find_element(By.XPATH, './/span[contains(@class, "copyable-text")]').get_attribute("data-pre-plain-text").strip("[]").split("]")[1].strip()
                text = block.find_element(By.XPATH, './/span[@class="selectable-text copyable-text"]').text
                messages.append((sender, text))
            except:
                continue
        return messages
