
import requests
from bs4 import BeautifulSoup
from utils import tenta_baixar, preprocessing

numero_de_eps = 1
'''
ep = 78
anime_name = "One Piece"
anime_link = "https://www.dreamanimes.com.br/online/legendado/one-piece"
_dir = "D:\\Videos\\Animes\\One Piece\\"
'''
ep = 3
anime_name = "Hunter x Hunter"
anime_link = "https://www.dreamanimes.com.br/online/legendado/hunter-x-hunter-2011"
_dir = "D:\\Videos\\Animes\\Hunter x Hunter\\"
'''
ep = 7
anime_name = "Monster"
anime_link = "https://www.dreamanimes.com.br/online/legendado/monster"
_dir = "D:\\Videos\\Animes\\Monster\\"
'''

for i in range(numero_de_eps):
    nome, HD, SD = preprocessing(anime_link, ep, anime_name)
    tenta_baixar(HD, SD, _dir, nome, ep)
    ep += 1
