from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path
import autoit
import time
import os
import datetime


options = Options()
options.add_argument("--incognito")

# Metodos Especiais




#Pegando data ontem 
def getYesterday(): 
	today=datetime.date.today() 
	oneday=datetime.timedelta(days=1) 
	yesterday=today-oneday
        
	return yesterday

# Trocar certificados
def trocarCertificado(pulos):
    y = int(pulos)
    if (pulos == 0):
        autoit.send("{ENTER}")    
    else:
        for x in range(y):
            autoit.send("{DOWN}")
            print(x)
            time.sleep(1)
        autoit.send("{ENTER}")
    return print("troca")    

# Trabalhando com dados

def inserindoDados(empresa_cnpj):
    # Inserindo CNPJ Emitente
    status_inserir = False
    status_pesquisar = True
    status_tentativas = 0
    while True:
        
        select = None
        pesquisar = None
        if (status_inserir == False):
            status_inserir = True
            time.sleep(2)
            cnpj = driver.find_element_by_id("CpfCnpj")
            cnpj.send_keys(empresa_cnpj)
            time.sleep(2)

            #Trocando Tico de Nota NFCE
            try:
                select = Select(driver.find_element_by_name("Tipo"))
                # select by value
                select.select_by_value('NFCE')
                time.sleep(2)
            except NoSuchElementException:
                break
            

            # Inserindo data de Inicio
            data_teste = getYesterday()
            date_formated = data_teste.strftime("%d%m%Y")    
            
            try:
                DataInicio = driver.find_element_by_id("DataInicio")
                DataInicio.send_keys('')
                time.sleep(2)
                DataInicio.send_keys(date_formated)
                time.sleep(2)
            except NoSuchElementException:
                break
            #Pegando data atual    .split(‘/’)

            hoje=datetime.date.today()
            date_formated2 = hoje.strftime("%d%m%Y")
            try:
                DataFim = driver.find_element_by_id("DataFim")
                DataFim.send_keys('')
                time.sleep(2)
                DataFim.send_keys(date_formated2)
                time.sleep(2)
            except NoSuchElementException:
                break    

            # Pesquisando
            try:
                
                pesquisar = driver.find_element_by_xpath("//button[@class='btn btn-primary'][@ng-click='ctrl.solicitar()']")
                time.sleep(4)
               
            except NoSuchElementException:  #spelling error making this code not work as expected
                print("Except Pesquisar...")
                inserindoDados(cnpj_belshop)
            else:
                
                print("pesquisando...")
                pesquisar.click()
            
             
               
            #refresh

            print("Depois do except pesquisar")
            try:
                time.sleep(2)
                refresh = driver.find_element_by_xpath("//a[@ng-click='pctrl.atualiza()']")
            except NoSuchElementException:
                print("Except refresh...")
            else:
                time.sleep(1)
                print("refresh iniciando...")
                refresh.click()
            
            # Baixando NFCE
            time.sleep(2)
            try:
                baixando = driver.find_element_by_xpath('//a[img/@src="../../Imagens/dec_baixar.png"]')
            except NoSuchElementException:
                print("Except baixar...")
            else:
                print("baixando...")
                time.sleep(1)
                baixando.click()
                
            # Cancelando Ultima pesquisa
            time.sleep(4)
            try:
                cancelando = driver.find_element_by_xpath('//a[img/@src="../../Imagens/dec_cancela.png"]')
            except NoSuchElementException:
                print("Except cancelar Pesquisar...")
            else:

                cancelando.click()

            return print("dados inseridos com sucesso!!")

        else:
            driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC')
            time.sleep(2)
            cnpj = driver.find_element_by_id("CpfCnpj")
            cnpj.send_keys(empresa_cnpj)
            time.sleep(2)

            #Trocando Tico de Nota NFCE
            try:
                select = Select(driver.find_element_by_name("Tipo"))
                # select by value
                select.select_by_value('NFCE')
                time.sleep(2)
            except NoSuchElementException:
                break
            

            # Inserindo data de Inicio
            data_teste = getYesterday()
            date_formated = data_teste.strftime("%d%m%Y")    
            
            try:
                DataInicio = driver.find_element_by_id("DataInicio")
                DataInicio.send_keys('')
                time.sleep(2)
                DataInicio.send_keys(date_formated)
                time.sleep(2)
            except NoSuchElementException:
                break
            #Pegando data atual    .split(‘/’)

            hoje=datetime.date.today()
            date_formated2 = hoje.strftime("%d%m%Y")
            try:
                DataFim = driver.find_element_by_id("DataFim")
                DataFim.send_keys('')
                time.sleep(2)
                DataFim.send_keys(date_formated2)
                time.sleep(2)
            except NoSuchElementException:
                break    

            # Pesquisando
            try:
                
                pesquisar = driver.find_element_by_xpath("//button[@class='btn btn-primary'][@ng-click='ctrl.solicitar()']")
                time.sleep(4)
               
            except NoSuchElementException:  #spelling error making this code not work as expected
                print("Except Pesquisar...")
                inserindoDados(cnpj_belshop)
            else:
                
                print("pesquisando...")
                pesquisar.click()
            
             
               
            #refresh

            print("Depois do except pesquisar")
            try:
                time.sleep(2)
                refresh = driver.find_element_by_xpath("//a[@ng-click='pctrl.atualiza()']")
            except NoSuchElementException:
                print("Except refresh...")
            else:
                time.sleep(1)
                print("refresh iniciando...")
                refresh.click()
            
            # Baixando NFCE
            time.sleep(2)
            try:
                baixando = driver.find_element_by_xpath('//a[img/@src="../../Imagens/dec_baixar.png"]')
            except NoSuchElementException:
                print("Except baixar...")
            else:
                print("baixando...")
                time.sleep(1)
                baixando.click()
                
            # Cancelando Ultima pesquisa
            time.sleep(4)
            try:
                cancelando = driver.find_element_by_xpath('//a[img/@src="../../Imagens/dec_cancela.png"]')
            except NoSuchElementException:
                print("Except cancelar Pesquisar...")
            else:

                cancelando.click()

            return print("dados inseridos com sucesso!!")

def reniciandoBelshop():
    options7 = Options()
    options7.add_argument("user-data-dir=C:\\Users\\root\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
    #Nome: BELSHOP
    #CNPJ: 01.762.204/0001-22
    #Validade: 26/02/2020
    cnpj_belshop = "01762204000122"
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options7)
    driver.get("about:blank")
    driver.delete_all_cookies()
    #driver.execute_script('localStorage.clear();')
    #driver.find_element_by_xpath("//*[@id='clearBrowsingDataConfirm']").click()
    driver.get('http://google.com.br')

    autoit.send("!dhttps://www2.agencianet.fazenda.df.gov.br/DEC")
    time.sleep(2)
    autoit.send("{ENTER}")
    time.sleep(2)
    autoit.send("{DOWN}")
    time.sleep(2)
    autoit.send("{ENTER}")
    time.sleep(4)
    belshop_name = driver.find_element_by_xpath("//div[@class='boxInfo']/ul/li//span[@class='ng-binding']").get_attribute("innerHTML")
    print(belshop_name)
    if(belshop_name == "BELSHOP…"):
        time.sleep(5)
        driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC/#/')
        time.sleep(2)
        inserindoDados(cnpj_belshop)    
        time.sleep(4)
    else:
        driver.close()
        os.system("C:\\PROJETO\\exec.cmd")
        exit()
        reniciandoBelshop()
    driver.close()



def reniciandoTecbeli():
    options8 = Options()
    options8.add_argument("user-data-dir=C:\\Users\\root\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
    #EMPRESA TECBELI
    #CNPJ: 16.527.753/0001-90
    #Validade: 06/03/2020
    cnpj_tecbeli = "16527753000190"
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options8)
    driver.get("about:blank")
    driver.delete_all_cookies()
    #driver.execute_script('localStorage.clear();')
    #driver.find_element_by_xpath("//*[@id='clearBrowsingDataConfirm']").click()
    driver.get('http://google.com.br')

    autoit.send("!dhttps://www2.agencianet.fazenda.df.gov.br/DEC")
    time.sleep(2)
    autoit.send("{ENTER}")
    time.sleep(2)
    autoit.send("{ENTER}")
    time.sleep(4)
    tecbeli_name = driver.find_element_by_xpath("//div[@class='boxInfo']/ul/li//span[@class='ng-binding']").get_attribute("innerHTML")
    print(tecbeli_name)
    if(tecbeli_name == "TECBELI…"):
        time.sleep(5)
        driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC/#/')
        time.sleep(2)
        inserindoDados(cnpj_tecbeli)
        time.sleep(4)
    else:
        driver.close()
        os.system("C:\\PROJETO\\exec.cmd")
        exit()
        reniciandoTecbeli()

    driver.close()

def reniciandobelserv():
    options9 = Options()
    options9.add_argument("user-data-dir=C:\\Users\\root\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
    #Nome: BELSERV
    #CNPJ 15.423.028/0001-09
    #Validade: 14/02/2020
    cnpj_belserv = "15423028000109"
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options9)
    #driver.find_element_by_xpath("//*[@id='clearBrowsingDataConfirm']").click()
    driver.get("about:blank")
    driver.delete_all_cookies()
    #driver.execute_script('localStorage.clear();')
    driver.get('http://google.com.br')

    autoit.send("!dhttps://www2.agencianet.fazenda.df.gov.br/DEC")
    time.sleep(2)
    autoit.send("{ENTER}")
    time.sleep(2)
    autoit.send("{DOWN}")
    time.sleep(2)
    autoit.send("{DOWN}")
    time.sleep(2)
    autoit.send("{ENTER}")
    time.sleep(4)
    belserv_name = driver.find_element_by_xpath("//div[@class='boxInfo']/ul/li//span[@class='ng-binding']").get_attribute("innerHTML")
    print(belserv_name)
    if(belserv_name == "BELSERV…"):
        time.sleep(2)
        driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC/#/')
        time.sleep(2)
        inserindoDados(cnpj_belserv)
        time.sleep(4)
    else:
        driver.close()
        reniciandobelserv() 
    driver.close()
    os.system("C:\\PROJETO\\exec.cmd")
    exit()
    autoit.send("! {F4}") 

options2 = Options()
options2.add_argument("--incognito")
#EMPRESA TECBELI
#CNPJ: 16.527.753/0001-90
#Validade: 06/03/2020
cnpj_tecbeli = "16527753000190"
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options2)
driver.get("about:blank")
driver.delete_all_cookies()
#driver.execute_script('localStorage.clear();')
#driver.find_element_by_xpath("//*[@id='clearBrowsingDataConfirm']").click()
driver.get('http://google.com.br')
time.sleep(1)
autoit.send("!d          https://www2.agencianet.fazenda.df.gov.br/DEC")
#driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC')
time.sleep(2)
autoit.send("{ENTER}")
time.sleep(2)
autoit.send("{ENTER}")
time.sleep(4)
try:    
    time.sleep(2)
    driver.find_element_by_xpath("//input[@class='ng-pristine ng-untouched ng-valid'][@ng-click='acao=1']").click() 
except:
    print("Erro ao marcar como lido")    
else:
    print("Marcado como lido")   
try:
    time.sleep(2)
    driver.find_element_by_css_selector("input[type='submit']").click()
except:
    print("Erro ao clicar em ok")
else:
    print("Confirmado com sucesso!")
time.sleep(3)    
tecbeli_name = driver.find_element_by_xpath("//div[@class='boxInfo']/ul/li//span[@class='ng-binding']").get_attribute("innerHTML")
print(tecbeli_name)
if(tecbeli_name == "TECBELI…"):
    time.sleep(5)
    driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC/#/')
    time.sleep(2)
    inserindoDados(cnpj_tecbeli)

    # Validando tamanho do arquivo
    time.sleep(4)
    data_criacao = lambda f: f.stat().st_ctime
    data_modificacao = lambda f: f.stat().st_mtime

    directory = Path('C:\\Users\\root\\Downloads')
    files = directory.glob('*.zip')
    sorted_files = sorted(files, key=data_modificacao, reverse=False)
    names = []
    for f in sorted_files:
        names = f

    names2 = str(names)

    new_file_name_2 = names2.replace(".zip", "")
    file_name_2 = new_file_name_2.split("_")
    name_file_2 = file_name_2[8]    
    print(name_file_2)

    if(name_file_2 == "0"):
        os.remove(names2)
        print("File Removed!")
        inserindoDados(cnpj_tecbeli)
    else:
        print("File não removido!")    
    print(name_file_2)   

    time.sleep(4)

else:
    driver.close()
    reniciandoTecbeli()

driver.close()


options3 = Options()
options3.add_argument("--incognito")
#Nome: BELSHOP
#CNPJ: 01.762.204/0001-22
#Validade: 26/02/2020
cnpj_belshop = "01762204000122"
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options3)
driver.get("about:blank")
driver.delete_all_cookies()
#driver.execute_script('localStorage.clear();')
#driver.find_element_by_xpath("//*[@id='clearBrowsingDataConfirm']").click()
driver.get('http://google.com.br')
time.sleep(1)
autoit.send("!d          https://www2.agencianet.fazenda.df.gov.br/DEC")
#driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC')
time.sleep(2)
autoit.send("{ENTER}")
time.sleep(2)
autoit.send("{DOWN}")
time.sleep(2)
autoit.send("{ENTER}")
time.sleep(4)

try:    
    time.sleep(2)
    driver.find_element_by_xpath("//input[@class='ng-pristine ng-untouched ng-valid'][@ng-click='acao=1']").click() 
except:
    print("Erro ao marcar como lido")    
else:
    print("Marcado como lido")   
try:
    time.sleep(2)
    driver.find_element_by_css_selector("input[type='submit']").click()
except:
    print("Erro ao clicar em ok")
else:
    print("Confirmado com sucesso!")
time.sleep(3) 

belshop_name = driver.find_element_by_xpath("//div[@class='boxInfo']/ul/li//span[@class='ng-binding']").get_attribute("innerHTML")
print(belshop_name)
if(belshop_name == "BELSHOP…"):
    time.sleep(5)
    driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC/#/')
    time.sleep(2)
    inserindoDados(cnpj_belshop)
    
    # Validando tamanho do arquivo
    time.sleep(4)
    data_criacao = lambda f: f.stat().st_ctime
    data_modificacao = lambda f: f.stat().st_mtime

    directory = Path('C:\\Users\\root\\Downloads')
    files = directory.glob('*.zip')
    sorted_files = sorted(files, key=data_modificacao, reverse=False)
    names = []
    for f in sorted_files:
        names = f

    names2 = str(names)

    new_file_name_2 = names2.replace(".zip", "")
    file_name_2 = new_file_name_2.split("_")
    name_file_2 = file_name_2[8]    
    print(name_file_2)

    if(name_file_2 == "0"):
        os.remove(names2)
        print("File Removed!")
        inserindoDados(cnpj_belshop)
    else:
        print("File não removido!")    
    print(name_file_2)   

        
    time.sleep(4)
else:
    driver.close()
    reniciandoBelshop()
driver.close()



options4 = Options()
options4.add_argument("--incognito")
#Nome: BELSERV
#CNPJ 15.423.028/0001-09
#Validade: 14/02/2020
cnpj_belserv = "15423028000109"
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", chrome_options=options4)
#driver.find_element_by_xpath("//*[@id='clearBrowsingDataConfirm']").click()
driver.get("about:blank")
driver.delete_all_cookies()
#driver.execute_script('localStorage.clear();')
driver.get('http://google.com.br')
time.sleep(1)
autoit.send("!d          https://www2.agencianet.fazenda.df.gov.br/DEC")
#driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC')
time.sleep(2)
autoit.send("{ENTER}")
time.sleep(2)
autoit.send("{DOWN}")
time.sleep(2)
autoit.send("{DOWN}")
time.sleep(2)
autoit.send("{ENTER}")
time.sleep(4)

try:    
    time.sleep(2)
    driver.find_element_by_xpath("//input[@class='ng-pristine ng-untouched ng-valid'][@ng-click='acao=1']").click() 
except:
    print("Erro ao marcar como lido")    
else:
    print("Marcado como lido")   
try:
    time.sleep(2)
    driver.find_element_by_css_selector("input[type='submit']").click()
except:
    print("Erro ao clicar em ok")
else:
    print("Confirmado com sucesso!")
time.sleep(3) 

belserv_name = driver.find_element_by_xpath("//div[@class='boxInfo']/ul/li//span[@class='ng-binding']").get_attribute("innerHTML")
print(belserv_name)
if(belserv_name == "BELSERV…"):
    time.sleep(2)
    driver.get('https://www2.agencianet.fazenda.df.gov.br/DEC/#/')
    time.sleep(2)
    inserindoDados(cnpj_belserv)
    
    # Validando tamanho do arquivo
    time.sleep(4)
    data_criacao = lambda f: f.stat().st_ctime
    data_modificacao = lambda f: f.stat().st_mtime

    directory = Path('C:\\Users\\root\\Downloads')
    files = directory.glob('*.zip')
    sorted_files = sorted(files, key=data_modificacao, reverse=False)
    names = []
    for f in sorted_files:
        names = f

    names2 = str(names)

    new_file_name_2 = names2.replace(".zip", "")
    file_name_2 = new_file_name_2.split("_")
    name_file_2 = file_name_2[8]    
    print(name_file_2)

    if(name_file_2 == "0"):
        os.remove(names2)
        print("File Removed!")
        inserindoDados(cnpj_belserv)
    else:
        print("File não removido!")    
    print(name_file_2)   

    time.sleep(4)
else:
    driver.close()
    reniciandobelserv() 
driver.close()
exit()
autoit.send("! {F4}")