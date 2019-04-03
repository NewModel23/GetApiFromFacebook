# how to get likes from Facebook API with Python
import os
from urllib.request import Request, urlopen
import json
import pandas as pd

# https://developers.facebook.com/tools/explorer/?method=GET&path=me%3Ffields%3Did%2Cname%2Cbirthday%2Clikes&version=v3.2

token = ''
request=Request('https://graph.facebook.com/v3.0/me?fields=id,name,likes&access_token=' + token)
response = urlopen(request)
resultado = response.read()

readable_json = json.loads(resultado)

likes = readable_json['likes']

datos = []

for i in likes['data']:
    datos.append(i['name'])
    

df=pd.DataFrame(datos)
df.to_clipboard(index=False,header=True)

os.getcwd()

df.to_excel("Likes.xlsx",sheet_name='likes del face')


