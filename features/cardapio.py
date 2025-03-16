import requests
from bs4 import BeautifulSoup
import re

class Cardapio:
    def __init__(self) -> None:
        self.base_url = "https://ufpi.br"
        self.page_url = f"{self.base_url}/restaurante-universitario"
        self.response = None
        self.pdf_url = None
        self.filename = "Download/cardapio.pdf"
    
    def get(self):
        self.response = requests.get(self.page_url)
        
        if self.response.status_code != 200:
            return None, self.response.status_code
        
        soup = BeautifulSoup(self.response.content, "html.parser")
        pdf_links = soup.find_all("a", string=re.compile("^Confira o cardápio em Teresina"))
        
        if not pdf_links:
            return None, "Erro ao resgatar cardápio :("
            
        pdf_link = pdf_links[0]["href"]
        self.pdf_url = f"{self.base_url}{pdf_link}"
        
        pdf_response = requests.get(self.pdf_url)
        if pdf_response.status_code != 200:
            return None, pdf_response.status_code
        
        with open(self.filename, "wb") as file:
            file.write(pdf_response.content)
            
        return self.filename, None

if __name__ == "__main__":
    c = Cardapio()