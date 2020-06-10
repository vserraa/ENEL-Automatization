from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
import os
import time
import subprocess
import csv

def enable_download_in_headless_chrome(driver, download_dir):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)

downloads_dir = os.path.join(os.getcwd(), "boletos_pdf")

with open('clientes.csv', newline='') as csvfile:
    clientsTable = list(csv.reader(csvfile))[1:]

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
options.add_argument("--disable-gpu")

with Chrome(options = options) as driver:
	enable_download_in_headless_chrome(driver, downloads_dir)
	for (nClient, cnpj) in clientsTable:
		print("Initializing download for client " + nClient + "-" + cnpj, end = "\t\t", flush = True)

		driver.get("https://www.eneldistribuicao.com.br/ce/LoginAcessoRapidoSegundaVia.aspx")

		inputClientNumber = WebDriverWait(driver, timeout = 10).until(lambda d: d.find_element_by_id("CONTENT_Formulario_NumeroCliente"))
		inputClientNumber.send_keys(nClient)

		inputCnpj = WebDriverWait(driver, timeout = 10).until(lambda d: d.find_element_by_id("CONTENT_Formulario_Documento"))
		inputCnpj.send_keys(cnpj)

		accessBtn = WebDriverWait(driver, timeout = 10).until(lambda d: d.find_element_by_id("CONTENT_Formulario_Acessar"))
		accessBtn.click()

		table = WebDriverWait(driver, timeout = 10).until(lambda d: d.find_element_by_id("CONTENT_segviarapida_GridViewSegVia"))

		firstRow = table.find_element_by_xpath(".//tr[2]")
		status = firstRow.find_element_by_xpath(".//td[8]").text

		checkBtn = WebDriverWait(driver, timeout = 10).until(lambda d: d.find_element_by_id("CONTENT_segviarapida_GridViewSegVia_CheckFatura_0"))
		checkBtn.click()

		downloadsPath = os.path.join(downloads_dir, "FaturaIndividual.pdf")

		if os.path.exists(downloadsPath):
		    os.remove(downloadsPath)

		downloadInit = False
		for i in range(10):
		    try:
		        savePdfBtn = WebDriverWait(driver, timeout = 10).until(lambda d: d.find_element_by_id("CONTENT_segviarapida_btnSalvarPDF"))    
		        savePdfBtn.click()
		        downloadInit = True
		        break
		    except ElementClickInterceptedException as e:
		        time.sleep(1)

		if not downloadInit:
		    print("FAILED")
		    continue

		downloadComplete = False
		for i in range(20):
		    if os.path.exists(downloadsPath):
		        downloadComplete = True
		        break
		    else:
		        time.sleep(1)

		if not downloadComplete:
		    print("FAILED")
		    continue

		filename = nClient + "-" + cnpj + ".pdf"
		newPath = os.path.join(downloads_dir, filename)

		if os.path.exists(newPath):
		    os.remove(newPath)

		os.rename(downloadsPath, newPath)
		print("SUCCESSFUL")