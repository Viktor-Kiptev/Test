import requests

url = 'https://api.pwnedpasswords.com/range/' + 'cbfdac6008f9cab4083784cbd1874f76618d2a97'
res = requests.get(url)
print(res)
