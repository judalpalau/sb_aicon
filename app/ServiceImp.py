#import mongoengine
import os
import requests
import PIL.Image
#from app.DBConnection import MongoDBConnection as Mongo
#from app.models import MedicineValues as MedicineValues
from app.Utilities.UtilLog import UtilLog as _log

import google.generativeai as genai
genai.configure(api_key = os.environ.get('APIKEY_GEMINI'))

instructions = """You are an expert in real estate.
You speak spanish. You should create a sellable description of the property including the characteristics users gives to you.
Answer should be less than 2 paragraphs. If there's a phone number, change it to 'Haz click en solicitar más información' """ 
model = genai.GenerativeModel(
    "models/gemini-1.5-flash",
    system_instruction=instructions,
)

instructions2 = """You are an expert in real estate.
You speak spanish. List and rank the characteristics of an atractive property with short answers whithout price, security and location.
---
#Example:
Light: 20%
Condition 10%
  """ 
agent2 = genai.GenerativeModel(
    "models/gemini-1.5-flash",
    system_instruction=instructions2,
)

class ServiceImp:
    def hello(name = "World"):
        return f'Hello {name}'
    
    def example(descriptions):
        response = model.generate_content(descriptions)   
        return response.text     
    
    def example2(image_url):
        img_data = requests.get(image_url).content
        with open('image.jpg', 'wb') as handler:
            handler.write(img_data)
        
        # image_file = genai.upload_file(path="image_name.jpg", display_name="Foto")
        # _log.info(f"Uploaded file '{image_file.display_name}' as: {image_file.uri}")
        img = PIL.Image.open('image.jpg')
        response = agent2.generate_content(["Califica la propiedad con las características anteriores", img])
        _log.info(response)
        _log.info(list(response))
        return response.text