# -*- coding: utf-8 -*-
"""
Baseado em: https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt
@author: Mauro
"""

import requests

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
    with open(_dir + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return local_filename

def tenta_baixar(HD_Links, SD_Links, name, ep):
    try:
        print("Tentando HD 1")
        download_file(HD_Links[2], _dir = "D:\\Videos\\Animes\\One Piece\\", local_filename = name)
    except requests.exceptions.Timeout:
        print("Timeout, Tentanto HD 2")
        download_file(HD_Links[0], _dir = "D:\\Videos\\Animes\\One Piece\\", local_filename = name)
    except requests.exceptions.HTTPError:
        print("Erro de HTTP, tentando SD 1")
        download_file(SD_Links[-1], _dir = "D:\\Videos\\Animes\\One Piece\\", local_filename = name)
    except requests.exceptions.RequestException as e:
        print(e)
        print("Parou no ep " + str(ep))

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
