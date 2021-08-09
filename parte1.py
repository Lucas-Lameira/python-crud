import requests
cnpj = 17895646000187
req = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
print(req.json())