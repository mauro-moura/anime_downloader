
import requests
from bs4 import BeautifulSoup
from utils import tenta_baixar, preprocessing

# Número de episódios que deseja baixar
numero_de_eps = 10
# Episódio no qual deve começar a contagem
ep = 3
# Nome do anime que vai ficar na pasta
anime_name = "Hunter x Hunter"
# Link do anime no Dream Animes
anime_link = "https://www.dreamanimes.com.br/online/legendado/hunter-x-hunter-2011"
# Diretório no seu HD (Precisa de '\\')
_dir = "D:\\Videos\\Animes\\Hunter x Hunter\\"


for i in range(numero_de_eps):
    nome, HD, SD = preprocessing(anime_link, ep, anime_name)
    tenta_baixar(HD, SD, _dir, nome, ep)
    ep += 1

print('Todos os episódios foram baixados')
