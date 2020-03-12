
import requests
from bs4 import BeautifulSoup
from utils import tenta_baixar, preprocessing

ep = 78
anime_name = "One Piece"
anime_link = "https://www.dreamanimes.com.br/online/legendado/one-piece"
_dir = "D:\\Videos\\Animes\\One Piece\\"
#ep = 1
#anime_name = "Cowboy Bebop"
#anime_link = "https://www.dreamanimes.com.br/online/legendado/cowboy-bebop"
#_dir = "D:\\Videos\\Animes\\Cowboy Bebop\\"

for i in range(10):
    nome, HD, SD = preprocessing(anime_link, ep, anime_name)
    tenta_baixar(HD, SD, _dir, nome, ep)
    ep += 1
