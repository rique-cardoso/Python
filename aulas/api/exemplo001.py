import requests

# Defina a URL da API que você deseja consumir
url = "https://jsonplaceholder.typicode.com/posts/1"  # Exemplo de API pública

# Envie a requisição GET para a URL
response = requests.get(url)

# Verifique se a requisição foi bem-sucedida (status code 200)
if response.status_code == 200:
    # Parse o conteúdo JSON da resposta
    data = response.json()
    print("Dados recebidos:", data)
else:
    print("Erro ao acessar a API. Status Code:", response.status_code)
