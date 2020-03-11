
import requests
from bs4 import BeautifulSoup
from utils import get_links, download_file, tenta_baixar, select_hd

ep = 27
anime_name = "One Piece"

for i in range(10):
    anime = "https://www.dreamanimes.com.br/online/legendado/one-piece"
    url = anime + "/episodio/"+ str(ep)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links, names = get_links(soup)
    HD, SD = select_hd(links, names)
    nome = anime_name + " EP " + str(ep) + " " + names[1] + ".mp4"
    #download_file(links[2], _dir = "D:\\Videos\\Animes\\One Piece\\", local_filename = nome)
    tenta_baixar(HD, SD, nome, ep)
    ep += 1

