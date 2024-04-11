from flask import request

payloadurl = "discord api here, where you send everything" 

while True:
    message = input()
    r = request.post(url, data={"content":message})

#online money transfer checking function
def get_balance(address):
    url = f"http//54.183.17.224/accounts/{address}/balance"
    print("url:", url)
    r = requests.get(url)
    balance = r.json().get("balance")
    if balance is None:
        return 0
    else:
        return balance