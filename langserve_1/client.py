import requests

response = requests.post(
    " http://localhost:8000/essay/invoke", # /invoke is added to call the essay api
    json={'input':{'topic':"my best friend"}}
)

print(response.json()['output']['content'])
