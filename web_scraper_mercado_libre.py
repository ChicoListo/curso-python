
#El siguiente script realiza web scraping de los precios de productos en Mercado Libre utilizando la biblioteca requests para realizar solicitudes HTTP y BeautifulSoup para analizar el HTML:

import os
import requests
from bs4 import BeautifulSoup
import csv

def get_desktop_path():
    # Obtener la ruta del escritorio según el sistema operativo
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    return desktop_path

def scrape_mercado_libre(search_query):
    # URL de la página de búsqueda de Mercado Libre
    url = f'https://listado.mercadolibre.com.mx/{search_query}#D[A:{search_query}%20]'
    
    # Realizar solicitud HTTP
    response = requests.get(url)
    
    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrar todos los contenedores de productos
        items = soup.find_all('li', class_='ui-search-layout__item')
        
        # Obtener la ruta del escritorio
        desktop_path = get_desktop_path()
        
        # Crear un archivo CSV para escribir los datos en el escritorio
        csv_file_path = os.path.join(desktop_path, 'datos_mercado_libre.csv')
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Titulo', 'Precio', 'Enlace'])  # Escribir el encabezado
            
            # Iterar sobre cada producto y extraer los datos
            for item in items:
                title = item.find('h2', class_='ui-search-item__title').text.strip()
                price = item.find('span', class_='andes-money-amount__fraction').text.strip() 
                link = item.find('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')['href']
                
                # Escribir los datos en el archivo CSV
                writer.writerow([title, price, link])
                
        print(f"Los datos han sido guardados en '{csv_file_path}' en el escritorio.")
    else:
        # Si la solicitud no fue exitosa, mostrar el mensaje de error
        print("Error al obtener la página:", response.status_code)

# Consulta de búsqueda en Mercado Libre
search_query = 'laptop gamer'

# Llamar a la función de scraping
scrape_mercado_libre(search_query)