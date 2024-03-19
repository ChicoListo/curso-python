import os
import requests
from bs4 import BeautifulSoup
import csv

def get_desktop_path():
    # Obtener la ruta del escritorio según el sistema operativo
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    return desktop_path

def scrape_coppel(search_query):
    # Reemplazar espacios con '+', aunque la estructura de URL de Coppel puede variar
    search_query_formatted = search_query.replace(' ', '+')
    # URL de la página de búsqueda de Coppel podría necesitar ajustes
    url = f'https://www.coppel.com/SearchDisplay?categoryId=&storeId=12761&catalogId=10001&langId=-5&sType=SimpleSearch&resultCatEntryType=2&showResultsPage=true&searchSource=Q&pageView=&beginIndex=0&pageSize=20&searchTerm={search_query_formatted}'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Realizar solicitud HTTP con headers para simular un navegador
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # La clase de los productos en Coppel puede variar, necesitarás investigar la estructura actual
        items = soup.find_all('div', class_='product')
        
        desktop_path = get_desktop_path()
        csv_file_path = os.path.join(desktop_path, 'datos_coppel.csv')
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Titulo', 'Precio', 'Enlace'])  # Escribir el encabezado
            
            for item in items:
                try:
                    # Los nombres de las clases deben ser actualizados según la estructura de la página
                    title = item.find('a', class_='WC_CatalogEntryDBThumbnailDisplayJSPF_4592058_link_9b').text.strip()
                    price = item.find('span', class_='price').text.strip()
                    link = item.find('a', class_='product_name')['href']
                    full_link = f'https://www.coppel.com{link}'
                    
                    writer.writerow([title, price, full_link])
                except AttributeError:
                    # Si falta algún campo, se omite el producto
                    continue
                
        print(f"Los datos han sido guardados en '{csv_file_path}' en el escritorio.")
    else:
        print("Error al obtener la página:", response.status_code)

# Consulta de búsqueda en Coppel
search_query = 'tenis hombre'

# Llamar a la función de scraping
scrape_coppel(search_query)
