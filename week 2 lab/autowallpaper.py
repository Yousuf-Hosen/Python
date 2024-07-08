""" 
download an image and set wallpaper
for this we use API

 """
import requests
import json
import PyWallpaper
api_url="https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&api_key=DEMO_KEY"
#  Get the json
respons=requests.get(api_url)
#  get content in bytes
# content=respons.content
# print(content)


#  convert bytes to string
content=respons.content.decode('UTF-8')
# print(content)
#  convert string to json
dict_content=json.loads(content)
# print(dict_content)
image_url=dict_content['url']
# print(image_url)
#  download image
res=requests.get(image_url)
# print(res)

# save the image
with open  ("apod.png","wb") as image:
    image.write(res.content)


#  set as waallpaper
PyWallpaper.change_wallpaper('D:\Python learning\week 2 lab\apod.png')



