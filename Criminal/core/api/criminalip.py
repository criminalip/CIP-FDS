import requests


def getipdata(ip: str) -> dict:
    
    url = "https://api.criminalip.io/v1/ip/data?ip={}".format(ip)
    api_key = "insert your api-key"
    headers = {"User-Agent": "CIP_FDS", "x-api-key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if response.json()["status"] == 200:
            return response.json()
    return {}
