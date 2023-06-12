from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Инициализация WebDriver
driver = webdriver.Chrome()

# Открытие WhatsApp веб-версии
driver.get('https://web.whatsapp.com')

wait = WebDriverWait(driver, 3600)  # Инициализация объекта ожидания с таймаутом в 10 секунд
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')))

# # Список получателей и текст сообщения
# recipients = ['+77712274460', '+77024119256']
# message = 'Привет! Это тестовое сообщение, отправленное ботом'

# # Нахождение поля ввода и отправка сообщения каждому получателю
# # for recipient in recipients:
# #     element = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
# #     element.send_keys(recipient, Keys.ENTER)
# #     time.sleep(2)  # Подождите, пока окно чата откроется
# #     input_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
# #     input_box.send_keys('Это тестовое сообщение отправленное ботом.', Keys.ENTER)
# #     time.sleep(2)
# element = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
# element.send_keys('Python Pro 2 год', Keys.ENTER)
# time.sleep(30)
# # Закрытие браузера
# driver.quit()