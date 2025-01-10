from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv() # carrega as variáveis de ambiente do arquivo .env
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("""Vamos jogar um jogo RPG, você vai gerar o contexto e a história.
Segue a configuração de contexto inicial para iniciarmos o jogo:
Nome do personagem: Neil Oprhélius
Sexo: masculino
Gênero do jogo: Futurista
Localização inicial: PunkCity
Estilo de narrativa: mistério e investigação
Objetivo inicial: Salvar a humanidade da Matrix controlada pela empresa HacksNow junto a um pequeno grupo de sobreviventes programadores.
Tamanho máximo dos textos: apenas um parágrafo de até, no máximo, 2000 caracteres.
Regras do jogo: você deve gerar um texto descrevendo a situação e me dar opções de escolha, cada opção será referenciada por um número, por exemplo, 1 - Correr, 2 - Ficar, se eu digitar 1 estou escolhendo a opção correr, se eu digitar 2 estou escolhendo a opção ficar.
Cada escolha tem uma consequência e essa consequência é definida por você.
O jogo deve ter um final baseado na minha escolha, dependendo do que eu escolher você pode: (1) gerar um novo contexto mostrando as consequências da minha escolha e me dando novas opções de escolha, (2) Game Over: essa escolha ocasionou a morte do meu personagem ou em danos graves para mim ou para outrem, prejudicando o objetivo do jogo, tornando-o impossível e por isso o resultado é jogo perdido, (3) Game Win: alcancei o objetivo inicial da história e portanto venci o jogo, apesar das consequências ocorridas durante o jogo, sejam boas ou ruins.""")
print(response.text)