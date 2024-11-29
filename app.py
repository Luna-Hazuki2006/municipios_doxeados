from geopy.geocoders import Nominatim
from pprint import pprint
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

geolocator = Nominatim(user_agent="municipios_doxeados")

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

class Datos(BaseModel): 
    latitud : float 
    longitud : float

@app.get('/')
def mostrar(): 
    return 'Para obtener los munipios, utilizar esta misma ruta con el método "POST", y en el body mandar un json con "latitud" y "longitud" (sin las comillas dobles)'

@app.post('/')
def obtener(datos : Datos): 
    location = geolocator.reverse(f"{datos.latitud}, {datos.longitud}")
    data = dict(location.raw)
    if data["address"]['country'] != 'Venezuela': return 'Las coordenas están fuera del territorio venezolano'
    return f'Municipio: {data["address"]["county"]}'