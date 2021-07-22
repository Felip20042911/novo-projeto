from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def abrir_pagina():
    web.get('https://www.google.com')

def abrir_whats():
    web.get('https://web.whatsapp.com/')
    sleep(20)

def pesquisa_nome(nome):
    web.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(nome)
    web.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)

def mandar_msg(msg):
    web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(msg)
    web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)


web = webdriver.Chrome()
#pegando os valores

abrir_pagina()
    
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Dólar')
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dolar = web.find_element_by_xpath('<span class="DFlfde SwHCTb" data-precision="2" data-value="5.2002">5,20</span>').get_attribute('data-value')
print(dolar)

abrir_pagina()

web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Euro')
web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro = web.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(euro)
