#script para la extraccion dde informacion de level 3 de UCPROTECT
#author: Raul Villano Obregon
#Fecha:31.01-2025
#version3.0
import time

#importando librerias

import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from lxml import etree
from datetime import datetime
import pandas as pd
import glob
import os

now = datetime.now()
date = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M:%S")
ASN=['12252','6147','21575','19180','3132','262210','27843']
#automatizacion del ingreso de datos
for isp in ASN:
    #driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_argument('headless')
    driver=webdriver.Chrome(options=options)
    driver.get('https://www.uceprotect.net/en/rblcheck.php')        #conectandose a la URL
    dropdown=Select(driver.find_element(By.NAME ,'whattocheck'))    #Identificando el elemento de seleccion
    dropdown.select_by_value('ASN')                                 #seleccionando la opcion ASN
    valor=driver.find_element(By.NAME,'ipr')                        #seleccionando el campo de entrada de texto
    asn=isp
    valor.clear()                                                   #limpiando el campo de entrada de texto
    valor.send_keys(asn)                                         #ingresando el valor de busqueda
    valor.send_keys(Keys.ENTER)                                     #enviado la orden de presionar la tecla ENTER
    sleep(10)                                                       #tiempo de espera de la pagina
    page=driver.page_source                                         #extrayendo informacion de la pagina web
    #print(page)


    soup=BeautifulSoup(page, 'lxml')                                #parseando la pagina web

    dom=etree.HTML(str(soup))                                       #creando el DOM de la pagina web y el arbol de estructura

    #identificando el contenedor del texto y extrayendo los campos utilizando xpath
    l3=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[1]/th[1]')
    l3_t=[i.text for i in l3]
    l4=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[1]/th[2]')
    l4_t=[i.text for i in l4]
    l5=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[1]/th[3]')
    l5_t=[i.text for i in l5]
    l6=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[1]/th[4]')
    l6_t=[i.text for i in l6]
    l7=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[1]/th[5]')
    l7_t=[i.text for i in l7]
    l8=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[1]/th[6]')
    l8_t=[i.text for i in l8]
    l9=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[1]/th[7]')
    l9_t=[i.text for i in l9]
    l10=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[1]/th[8]')
    l10_t=[i.text for i in l10]
    level=[['Date'],['Time'],l3_t,l4_t,l5_t,l6_t,l7_t,l8_t,l9_t,l10_t]                #creando el erreglo de los nombres de las columnas
    data=pd.DataFrame(level)                                        #convirtiendo el arreglo en un dataframe
    data_t=data.transpose()                                         #realizando la transpuesta de los elementos del dataframe
    #print(data_t)

    #identificando el contenedor del texto y extrayendo los valores utilizando xpath

    l3_v=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[2]/td[1]/strong')
    l3_tv=[i.text for i in l3_v]
    l4_v=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[2]/td[2]/strong')
    l4_tv=[i.text for i in l4_v]
    l5_v=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[2]/td[3]/center')
    l5_tv=[i.text for i in l5_v]
    l6_v=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[2]/td[4]/center')
    l6_tv=[i.text for i in l6_v]
    l7_v=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[2]/td[5]/center')
    l7_tv=[i.text for i in l7_v]
    l8_v=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[2]/td[6]/table/tbody/tr/td[1]/center')
    l8_tv=[i.text for i in l8_v]
    l9_v=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[2]/td[7]/center')
    l9_tv=[i.text for i in l9_v]
    l10_v=dom.xpath('/html/body/table/tbody/tr[2]/td[2]/center[2]/table[2]/tbody/tr[2]/td[8]/table/tbody/tr/td[2]/form/input[3]')
    l10_tv=[i.text for i in l10_v]
    level_v=[[date],[hour],l3_tv,l4_tv,l5_tv,l6_tv,l7_tv,l8_tv,l9_tv,l10_tv]      #creando el arreglo con los valores de las columnas
    data=pd.DataFrame(level_v)                                      #convirtiendo el arreglo a dataframe
    data_tv=data.transpose()                                        #realizando la transpuesta a los valores del dataframe
    #print(data_tv)
    data_final=data_t._append(data_tv)                              #creando el dataframe final juntando los dataframes de texto y de valores
    print(data_final)                                               #mostrando el resultado del scrapping en consola

    data_final.to_excel(asn+".xlsx")                              #convirtiendo el dataframe en un archivo excel

    time.sleep(30)

#programa que forma el archivo base con informacion de los ISP
def importa_excel(archivo):
    temp=pd.read_excel(archivo,skiprows=[0])
    return temp
lista=glob.glob("*.xlsx")
for archivo in lista:
    print(archivo)
lista_df=[importa_excel(archivo) for archivo in lista]
print(lista_df)
todo=pd.concat(lista_df,axis=0,ignore_index=True)
todo.drop(todo.columns[[0]],axis=1,inplace=True)
print(todo.columns)
todo.to_excel('C:/Users/devil/Desktop/work/ucprotect/todo.xlsx',index=None)

print(todo)

#programa que actualiza la base de datos
def importa_excel(archivo):
    temp=pd.read_excel(archivo)
    return temp
lista=glob.glob("C:/Users/devil/Desktop/work/ucprotect/*.xlsx")
for archivo in lista:
    print(archivo)
lista_df=[importa_excel(archivo) for archivo in lista]
print(lista_df)
todo=pd.concat(lista_df,axis=0,ignore_index=True,join="inner")
todo.to_excel('C:/Users/devil/Desktop/work/ucprotect/base.xlsx')


print(todo)
file='C:/Users/devil/Desktop/work/ucprotect/todo.xlsx'
if os.path.exists(file):
    os.remove(file)
else:
    print('no existe el archivo')