from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

web = webdriver.Chrome()
web.get('https://web.whatsapp.com/')

sleep(20)

nomes = ['Nel', 'Eu']

mensagem = 'oiie, tudo bom?'


def pesquisa_nome(nome):
    web.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(nome)
    web.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)


def mandar_msg(msg):
    web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(msg)
    web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)


for nome in nomes:
    pesquisa_nome(nome)
    mandar_msg(mensagem)