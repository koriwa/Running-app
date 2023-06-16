import requests

def get_user_ip():
    response = requests.get("https://api.ipify.org?format=json")
    data = response.json()
    user_ip = data["ip"]

    return user_ip


user_ip = get_user_ip()

print(f"User IP: {user_ip}")
