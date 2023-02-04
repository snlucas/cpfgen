import multiprocessing
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_cpf_value():
    url = "https://www.4devs.com.br/gerador_de_cpf"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Find the "GERAR CPF" button and click it
    driver.find_element(By.ID, "bt_gerar_cpf").click()

    # Find the CPF input value
    cpf_input = driver.find_element(By.ID, "texto_cpf")
    cpf_value = cpf_input.get_attribute('innerText')

    while cpf_value == "Gerando...":
        cpf_value = cpf_input.get_attribute('innerText')

    driver.quit()
    pyperclip.copy(cpf_value)
    print(cpf_value)
if __name__ == '__main__':
    p = multiprocessing.Process(target=get_cpf_value)
    p.start()
    p.join()
