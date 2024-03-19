import os
import requests
from bs4 import BeautifulSoup
import csv

def get_desktop_path():
    # Obtener la ruta del escritorio según el sistema operativo
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    return desktop_path

def scrape_shein(search_query):
    # Preparar la URL de búsqueda. Nota: SHEIN carga productos dinámicamente, esto puede no funcionar correctamente.
    url = f'https://www.shein.com.mx/pdsearch/{search_query}/'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Realizar solicitud HTTP con headers para simular una solicitud de navegador
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Intentar encontrar los contenedores de productos
        # Esta clase puede no ser correcta debido a la carga dinámica de contenido
        items = soup.find_all('div', class_='S-product-item__info')
        
        desktop_path = get_desktop_path()
        csv_file_path = os.path.join(desktop_path, 'productos_shein.csv')
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Titulo', 'Precio', 'Enlace'])  # Escribir el encabezado
            
            for item in items:
                try:
                    # La estructura de estos elementos puede variar
                    title = item.find('a', class_='S-product-item__name').text.strip()
                    price = item.find('span', class_='S-product-item__price').text.strip()
                    link = item.find('a', class_='S-product-item__img')['href']
                    full_link = f'https://www.shein.com.mx{link}'
                    
                    writer.writerow([title, price, full_link])
                except Exception as e:
                    # Si falta algún campo o hay un error, se omite el producto
                    continue
                
        print(f"Los datos han sido guardados en '{csv_file_path}' en el escritorio.")
    else:
        print("Error al obtener la página:", response.status_code)

# Consulta de búsqueda en SHEIN
search_query = 'short%20hombre'

# Llamar a la función de scraping
scrape_shein(search_query)
