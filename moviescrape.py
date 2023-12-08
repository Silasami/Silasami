
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
#print(response.text)

whole_page = response.text
soup = BeautifulSoup(whole_page,"html.parser")
movie_list = []
movie_name = soup.find(name="h3")

for moviename in soup.find_all(name="h3",class_="title"):
    movie_list.append(moviename.getText())
#print(movie_name.text)
#print(movie_list)

with open ("movies.txt" ,mode="w") as file:
    for movie in movie_list:
        file.write(movie + '\n')