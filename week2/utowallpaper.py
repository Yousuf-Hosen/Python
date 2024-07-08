import requests
import json
import PyWallpaper
api_url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
# get the json 
respons=requests.get(api_url)
content=respons.content.decode('UTF-8')
# convert string to json
dict_content=json.loads(content)
print(dict_content)
# get the image url
image_url=dict_content['url']
#  download image
res=requests.get(image_url)
# save the image
with open('apod.png','wb')as image:
    image.write(res.content)
    #  set as pywallpaper in my pc


# PyWallpaper.change_wallpaper('D:\Python learning\week1\module1\apod.png')
