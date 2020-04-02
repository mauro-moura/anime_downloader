# -*- coding: utf-8 -*-
"""
Baseado em: https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt
@author: Mauro
"""

import requests
from requests import ConnectionError
from bs4 import BeautifulSoup
import sys

def get_info(soup):
    name_list = soup.find(class_='body')
    name_list_items = name_list.find_all('a')
    # Cria loop para imprimir todos os nomes
    for name in name_list_items:
        print(name.prettify())

def get_links(soup):
    name_list = soup.find(class_='body') #Define a classe
    name_list_items = name_list.find_all('a') #Define a div
    links = []
    names = []
    for name in name_list_items:
        names.append(name.contents[0]) #Pega os textos
        links.append(name.get('href')) #Pega os links
    return links, names

def download_file(url, _dir = "", local_filename = ""):
    #local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    total = r.headers['Content-Length']
    progress = 0
    with open(_dir + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                progress += 1024
                progress_bar(progress, total)
    sys.stdout.write('\b\b\b\bBaixado!\n')
    return local_filename

def progress_bar(count, total, suffix=''):
    bar_len = 40
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percents, '%', suffix))
    sys.stdout.flush()

def tenta_baixar(HD_Links, SD_Links, _dir, name, ep):
    print("Baixando Ep " + str(ep))
    try:
        print("Tentando HD 1")
        download_file(HD_Links[-1], _dir, local_filename = name)
    except requests.exceptions.Timeout:
        print("Timeout, Tentanto HD 2")
        download_file(HD_Links[0], _dir, local_filename = name)
    except requests.exceptions.HTTPError:
        print("Erro de HTTP, tentando SD 1")
        download_file(SD_Links[-1], _dir, local_filename = name)
    except ConnectionError:
        print("Sua internet caiu, tente novamente mais tarde")
        sys.exit()
    except requests.exceptions.RequestException as e:
        print(e)
        print("Parou no ep " + str(ep))
        sys.exit()

def select_hd(links, names):
    pos = 0
    HD_Link = []
    SD_Link = []
    for name in names:
        if "HD" in name:
            HD_Link.append(links[pos])
        else:
            SD_Link.append(links[pos])
        pos += 1
    return HD_Link, SD_Link

def verifica_link(link):
    r = requests.get(link, stream=True)
    if ('Content-Length' in r.headers):
        return True
    else:
        return False

def filter_links(links):
    link_filtrado = []
    for link in links:
        if verifica_link(link):
            if (link != None):
                link_filtrado.append(link)
    return link_filtrado

def preprocessing(anime_link, ep, anime_name):
    url = anime_link + "/episodio/"+ str(ep)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links, names = get_links(soup)
    HD, SD = select_hd(links, names)
    HD_filtrado = filter_links(HD)
    SD_filtrado = filter_links(SD)

    if (HD):
        definition = "HD"
    else:
        definition = "SD"
    nome = anime_name + " EP " + str(ep) + " " + definition + ".mp4"

    return nome, HD_filtrado, SD_filtrado

