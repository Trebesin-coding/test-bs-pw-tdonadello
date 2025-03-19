from bs4 import BeautifulSoup
import requests


def main():

    url = "https://js-trebesin.github.io/bsoup-exam/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser") # <--- Úkol: popiš krátce, co tohle dělá = umožní nám hledat html prvky a pracovat s nimi

    ingredience = soup.find(style="z-index")
    print(f"Ingredience pro češnečku jsou ({ingredience.text})")




if __name__ == "__main__":
    main()
