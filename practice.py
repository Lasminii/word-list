import requests

api_key = '4f6fcbb1-3b32-4d6c-ab5f-55e77cb29383'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definitions in definitions:
    print(definitions)