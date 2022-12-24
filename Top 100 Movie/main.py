import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
FILE_NAME = "./a.txt"


# Write your code below this line 👇
def load_site():
    response = requests.get(URL)
    print(response.encoding)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    all_entries = soup.find_all(name="h3", class_="title")
    return all_entries


def sort_entries(entries):
    movies_titles = [movie.getText() for movie in entries[::-1]]
    with open(FILE_NAME, mode="w", encoding="ISO-8859-1") as file:
        for movie in movies_titles:
            file.write(f"{movie}\n")


sort_entries(load_site())
