import google.generativeai as genai

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explique um pouco sobre modulos e pacotes em Python.")
print(response.text)