import requests
from api_key import api_key




city_name ='Belém'

#link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json() # 200 -> Funcionou,  404 -> não encontrado, 500 -> não disponível
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] -273.15


print(descricao, f"{temperatura}ºC")
