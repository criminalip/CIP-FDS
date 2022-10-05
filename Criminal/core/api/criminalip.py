import urllib3
import requests


# from core.utils import utils


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getipdata(ip: str) -> dict:
    
    url = "https://api.criminalip.io/v1/ip/data?ip={}".format(ip)
    api_key = "insert your api-key"
    headers = {"User-Agent": "CRIP_Verifier", "x-api-key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if response.json()["status"] == 200:
            return response.json()
    return {}
