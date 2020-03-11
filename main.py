
import requests
from bs4 import BeautifulSoup
from utils import get_links, download_file, tenta_baixar, select_hd

#ep = 37
#anime_name = "One Piece"
ep = 1
anime_name = "Cowboy Bebop"
_dir = "D:\\Videos\\Animes\\Cowboy Bebop\\"

for i in range(5):
    #anime = "https://www.dreamanimes.com.br/online/legendado/one-piece"
    anime = ""
    url = anime + "/episodio/"+ str(ep)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links, names = get_links(soup)
    HD, SD = select_hd(links, names)
    nome = anime_name + " EP " + str(ep) + " " + names[1] + ".mp4"
    tenta_baixar(HD, SD, _dir, nome, ep)
    ep += 1

