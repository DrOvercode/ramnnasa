from fastapi import FastAPI
import requests
import json
import numpy as np
 
prompt = input("Your question to Mr Armstrong: ")

 
url = "http://localhost:11434/api/generate"
 
headers = {"Content-Type": "application/json"}     
 
data = {"model": "ALIENTELLIGENCE/aerospaceengineer", "prompt": prompt, "stream": False}

app = FastAPI()

response = requests.post(url, headers=headers, data=json.dumps(data))
 
if response.status_code == 200:
   response_text = response.text
   data = json.loads(response_text)
   actual_response = data["response"]
   print(actual_response)
else:
   print("Error:", response.status_code, response.text)  

@app.get("/")
def reed_root():
    return {'mesage': 'ALIENTELLIGENCE/aerospaceenginner API'}

@app.post('/predict')
def predict(data: dict):
    features = np.array(data['features'].reshape(1, -1))
    prediction = model.predict(features)
    class_name = class_name[prediction][0]
    return {'predicted_class': class_name}