import os
import requests
from bs4 import BeautifulSoup
import csv

def get_desktop_path():
    # Obtener la ruta del escritorio según el sistema operativo
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    return desktop_path

def scrape_liverpool(search_query):
    # Convertir el espacio en búsqueda en '+', que es el formato de URL de Liverpool
    search_query = search_query.replace(' ', '+')
    # URL de la página de búsqueda de Liverpool
    url = f'https://www.liverpool.com.mx/tienda?s={search_query}&d3106047q={search_query}'
    
    # Headers para simular una solicitud desde un navegador web
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Realizar solicitud HTTP con headers
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Liverpool tiene varias clases para productos, esto puede requerir ajustes
        items = soup.find_all('div', class_='product-cell')
        
        desktop_path = get_desktop_path()
        csv_file_path = os.path.join(desktop_path, 'datos_liverpool.csv')
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Titulo', 'Precio', 'Enlace'])  # Escribir el encabezado
            
            for item in items:
                try:
                    title = item.find('div', class_='product-name').text.strip()
                    price = item.find('div', class_='product-price').text.strip()
                    link = item.find('a')['href']
                    full_link = f'https://www.liverpool.com.mx{link}'
                    
                    writer.writerow([title, price, full_link])
                except AttributeError:
                    # Si falta algún campo, se omite el producto
                    continue
                
        print(f"Los datos han sido guardados en '{csv_file_path}' en el escritorio.")
    else:
        print("Error al obtener la página:", response.status_code)

# Consulta de búsqueda en Liverpool
search_query = 'televisor'

# Llamar a la función de scraping
scrape_liverpool(search_query)
