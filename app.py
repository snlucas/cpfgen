import multiprocessing
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_cpf_value():
    url = "https://www.4devs.com.br/gerador_de_cpf"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Find the "GERAR CPF" button and click it
    gerar_cpf_button = driver.find_element(By.CSS_SELECTOR, "#bt_gerar_cpf")
    gerar_cpf_button.click()

    # Find the CPF input value
    cpf_input = driver.find_element(By.ID, "texto_cpf")
    cpf_value = cpf_input.get_attribute('innerText')

    while cpf_value == "Gerando...":
        cpf_value = cpf_input.get_attribute('innerText')
    
    pyperclip.copy(cpf_value)
    print(cpf_value)

    driver.quit()

if __name__ == '__main__':
    p = multiprocessing.Process(target=get_cpf_value)
    p.start()
    p.join()

