import requests
from bs4 import BeautifulSoup
import re

class Cardapio:
    def __init__(self) -> None:
        self.base_url = "http://ufpi.br"
        self.page_url = f"{self.base_url}/restaurante-universitario"
        self.response = None
        self.status = None
    
    def get(self):
        self.response = requests.get(self.page_url)
        if self.response.status_code == 200:
            soup = BeautifulSoup(self.response.content, "html.parser")
            pdf_links = soup.find_all("a", string=re.compile("^Confira o cardápio em Teresina"))
            if pdf_links:
                pdf_link = pdf_links[0]["href"]
                pdf_url = f"{self.base_url}{pdf_link}"

                """ pdf_response = requests.get(pdf_url)
                if pdf_response.status_code == 200:
                    filename = "Out/cardapio.pdf"
                    with open(filename, "wb") as file:
                        file.write(pdf_response.content)
                    
                    self.status = f"Download do cardápio concluído com sucesso. Arquivo salvo como {filename}."
                else:
                    self.status = "Erro ao baixar o cardápio." """
            else:
                self.status = "Link do cardápio não encontrado."
        else:
            self.status = "Erro ao acessar a página do cardápio."
        
        return pdf_url

if __name__ == "__main__":
    c = Cardapio()
    c.get()