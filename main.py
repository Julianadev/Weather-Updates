import requests

API_KEY = "3b0c3b4a41a972374836ef35cd321be9"
cidade = input("Digite sua cidade: ")
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15

print(descricao, f"{temperatura:.2f}ºC")