import requests
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def generate_access_token(authorization_code, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="sai.kumar.yerra", grant_type="authorization_code"):
    """
    Generates an access token from Zoho API.

    Args:
        authorization_code (str): The authorization code.
        client_id (str): The client ID.
        client_secret (str): The client secret.
        redirect_uri (str): The redirect URI.
        grant_type (str): The grant type.

    Returns:
        dict: A dictionary containing the access token details.
        eg.
            {
                "access_token": "***",
                "refresh_token": "***",
                "scope": "ZohoMail.messages.ALL ZohoMail.folders.ALL ZohoMail.accounts.ALL",
                "api_domain": "https://www.zohoapis.com",
                "token_type": "Bearer",
                "expires_in": 3600,
            }
    """
    url = f"https://accounts.zoho.com/oauth/v2/token?grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&code={authorization_code}"

    payload = {}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()

if __name__ == "__main__":
    authorization_code = input("Enter the authorization code: ")
    act = generate_access_token(authorization_code)
    print(act)