import requests,json
import http.client
conn = http.client.HTTPSConnection("accuweatherstefan-skliarovv1.p.rapidapi.com")
payload = "apiKey=%3CREQUIRED%3E&locationKey=%3CREQUIRED%3E" 
headers = { 'content-type': "application/x-www-form-urlencoded", 'X-RapidAPI-Key': "79771164ecmshb0039822a7a799ep138660jsn4cfbf06ec283", 'X-RapidAPI-Host': "AccuWeatherstefan-skliarovV1.p.rapidapi.com" } 
conn.request("POST", "/get24HoursConditionsByLocationKey", payload, headers) 
res = conn.getresponse() 
data = res.read() 
print(data.decode("utf-8"))