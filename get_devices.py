import requests
import json

base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

login = "devnetuser"
passwd = "Cisco123!"

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", auth=(login, passwd)).json()

token = auth_response["Token"]

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

