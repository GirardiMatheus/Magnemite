import os
import requests

def download_data(url: str, destination: str):
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    print(f"Starting data download from: {url}")
    response = requests.get(url)

    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"Download completed. File saved at: {destination}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

if __name__ == "__main__":
    DATA_URL = "https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/dados-abertos/Documents/Dados%20brutos.xlsx"
    DESTINATION_PATH = os.path.join("data", "dados_brutos.xlsx")
    
    download_data(DATA_URL, DESTINATION_PATH)