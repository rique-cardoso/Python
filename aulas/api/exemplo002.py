import requests

# Definição da URL da API que vou consumir
url = "https://rickandmortyapi.com/api/character/?name=rick" # API Pública Rick and Morty

# Enviando a requisição GET para a URL
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida (status code 200)
if response.status_code == 200:
    # Parse o conteúdo JSON da resposta
    data = response.json()
    print("Dados recebidos: ", data)
else:
    print("Erro ao acessar a API. Status Code: ", response.status_code)