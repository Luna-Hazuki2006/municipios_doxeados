from geopy.geocoders import Nominatim
from pprint import pprint
from functools import partial
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from geopy.exc import GeocoderServiceError
from countryinfo import CountryInfo
from bs4 import BeautifulSoup
import wikipediaapi
import json

app = FastAPI()

geolocator = Nominatim(user_agent="municipios_doxeados")
# geocode = partial(geolocator.geocode, language="es")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# print(location.address)
# # Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
# print((location.latitude, location.longitude))
# # (52.5094982, 13.3765983)
# pprint(location.raw)

# data = CountryInfo('Venezuela')
# ESTADOS = data.provinces()
# pprint(ESTADOS)

# for esto in ESTADOS: 
#     print(esto)
#     lista = geocode(f"municipio en {esto}, Venezuela", exactly_one=False, limit=100) 
#     # print(lista)
#     try: municipios = [municipio.raw['name'] for municipio in lista]
#     except: continue
#     pprint(municipios)

# import pandas as pd

# Municipios = {}

# Inicializar la API de Wikipedia
# wiki_wiki = wikipediaapi.Wikipedia('municipios_doxeados', 'es')
# wiki_wiki = wikipediaapi.Wikipedia('municipios_doxeados', 'es', extract_format=wikipediaapi.ExtractFormat.HTML)
# page_py = wiki_wiki.page('Anexo:Municipios_de_Venezuela')
# sopa = BeautifulSoup(page_py.text, 'html.parser')
# ol = sopa.find_all('ol')
# for esto in ol: 
#     titulo = esto.find_previous('h2')
#     # pprint(titulo)
#     lis = esto.find_all('li')
#     lista = []
#     for esta in lis: 
#         try: 
#             data = str(esta.text).split('(')
#             lista.append([data[0].strip(), data[1].replace(')', '')])
#         except: 
#             lista.append(['Río Negro', 'San Carlos de Río Negro'])
#     Municipios[str(titulo.text).strip()] = lista

# pprint(Municipios)

# errores = []
# diferencias = []



# for esta in Municipios.items():
#     for esto in esta[1]:
#         try:  
#             data = geolocator.geocode(f'{esto[1]}, {esta[0]}, Venezuela')
#             # if data == None: 
#             #     prueba = str(esto[1]).find(' ')
#             #     data = geolocator.geocode(f'{esto[1][prueba:]}, Venezuela')
#             if data == None and 'Piñal' in str(esto[1]): 
#                 prueba = 'El Piñal'
#                 data = geolocator.geocode(f'{prueba}, {esta[0]}, Venezuela')
#             elif data == None and 'Paraguachí' in str(esto[1]): 
#                 prueba = 'Paraguachí'
#                 data = geolocator.geocode(f'{prueba}, {esta[0]}, Venezuela')
#             elif data == None and 'Villa del Rosario' in str(esto[1]): 
#                 prueba = 'Villa del Rosario'
#                 data = geolocator.geocode(f'{prueba}, {esta[0]}, Venezuela')
#             elif data == None and 'San Sebastián de los Reyes' in str(esto[1]): 
#                 prueba = 'San Sebastián'
#                 data = geolocator.geocode(f'{prueba}, {esta[0]}, Venezuela')
#             if esto[0] in data.address: print(data.address)
#             else: 
#                 data = geolocator.geocode(f'{esto[1]}, {esto[0]}, {esta[0]}, Venezuela')
#                 if data == None and 'Ocumare' in str(esto[0]): 
#                     esto[0] = 'Ocumare'
#                     data = geolocator.geocode(f'{esto[1]}, {esto[0]}, {esta[0]}, Venezuela')
#                 elif data == None and 'Angostura del Orinoco' == str(esto[0]): 
#                     esto[0] = 'Heres'
#                     data = geolocator.geocode(f'{esto[1]}, {esto[0]}, {esta[0]}, Venezuela')
#                 elif data == None and 'Juan José Rondón' == str(esto[0]): 
#                     esto[0] = 'Las Mercedes'
#                     esto[1] = 'Santa Rita de Manapire'
#                     data = geolocator.geocode(f'{esto[1]}, {esto[0]}, {esta[0]}, Venezuela')
#                 elif data == None and 'Antonio Díaz' == str(esto[0]): 
#                     esto[0] = 'Díaz'
#                     data = geolocator.geocode(f'{esto[1]}, {esto[0]}, {esta[0]}, Venezuela')
#                 elif data == None and 'Antonio Rómulo Costa' == str(esto[0]): 
#                     esto[0] = 'Rómulo Acosta'
#                     data = geolocator.geocode(f'{esto[1]}, {esto[0]}, {esta[0]}, Venezuela')
                
#                 print(data.address)
#                 # pprint(data.raw)
#                 # diferencias.append((esto[0], data.raw))
#         except AttributeError: 
#             pprint(esto)
#             errores.append(esto)
        # except: 
        #     pprint('Otro error más :v')
        #     continue

# pprint(diferencias)
# pprint(errores)

# with open('municipios.json', 'r+') as f: 
#     finales = []
#     for esto in Municipios.values(): 
#         for cada in esto: 
#             finales.append(cada[0])
#     json.dump([{'Municipios': finales}], f, indent=4)

# datos = [['Aragua', 'Ocumare de la Costa de Oro', 'Ocumare de la Costa'],
#  ['Bolívar', 'Angostura del Orinoco', 'Ciudad Bolívar'],
#  ['Guárico', 'Juan José Rondón', 'Santa Rita de Manapire'],
#  ['Nueva Esparta', 'Antonio Díaz', 'San Juan Bautista'],
#  ['Táchira', 'Antonio Rómulo Costa', 'Las Mesas']]

# for esto in datos: 
#     data = geolocator.geocode(f'{esto[2]}, {esto[0]}, Venezuela')
#     pprint(data.raw)

# Función para obtener los municipios de un estado
# def get_municipios(state):
#     page = wiki_wiki.page(f"Anexo:Municipios_del_estado_{state}")
#     pprint(page)
#     municipios = []
#     if page.exists():
#         for section in page.sections:
#             if section.title == "Municipios":
#                 for subsection in section.sections:
#                     municipios.append(subsection.title)
#     return municipios

# Lista de estados en Venezuela
# states_of_venezuela = [
#     "Amazonas", "Anzoátegui", "Apure", "Aragua", "Barinas", "Bolívar", 
#     "Carabobo", "Cojedes", "Delta Amacuro", "Falcón", "Guárico", "Lara", 
#     "Mérida", "Miranda", "Monagas", "Nueva Esparta", "Portuguesa", "Sucre", 
#     "Táchira", "Trujillo", "Yaracuy", "Zulia", "La Guaira"
# ]

# Obtener municipios para todos los estados
# all_municipios = {}
# for state in ESTADOS:
#     municipios = get_municipios(state)
    # all_municipios[state] = municipios

# Convertir a DataFrame para mejor visualización
# df = pd.DataFrame.from_dict(all_municipios, orient='index').transpose()
# print(df)



# data = geolocator.reverse('10.069157193640715, -69.34237616042773')
# pprint(data.raw)

# data = geolocator.geocode('San Carlos de Río Negro')
# pprint(data.raw)

class Datos(BaseModel): 
    latitud : float 
    longitud : float

@app.get('/')
def mostrar(): 
    return 'Para obtener los municipios, utilizar esta misma ruta con el método "POST", y en el body mandar un json con "latitud" y "longitud" (sin las comillas dobles)'

@app.post('/')
def obtener(datos : Datos): 
    try: 
        location = geolocator.reverse(f"{datos.latitud}, {datos.longitud}")
        data = dict(location.raw)
        if data["address"]['country'] != 'Venezuela': return 'Las coordenas están fuera del territorio venezolano'
        return f'Municipio: {data["address"]["county"]}'
    except GeocoderServiceError: 
        return 'Para que este api funcione necesita estar conectado con alguna red wifi'
    
@app.get('/municipios')
def obtener(): 
    lista = []
    with open('municipios.json', 'r+') as f: 
        lista = json.load(f)
    return lista