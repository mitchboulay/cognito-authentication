
import os

import json
import os
import datetime
import requests
import time
import base64
import hmac
import hashlib
import base64



f = open('dev_env_var.json')
data = json.load(f)
client_id=data["cognitoClientId"]
client_secret=data["cognitoClientSecret"]
username=data["cognitoUserName"]
password=data["cognitoUserPassword"]
AWSregion=data["cognitoUserPoolRegion" ]
url=data["apiGatewayUrl_idp"].format(AWSregion)

client_secret = client_secret.encode()

def get_secret_hash(client_secret, username):
    # A keyed-hash message authentication code (HMAC) calculated using
    # the secret key of a user pool client and username plus the client
    # ID in the message.
    message = username + client_id
    dig = hmac.new(
        client_secret, 
        msg=message.encode('UTF-8'),
        digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()

def getCognitoToken():
    json_secret_hash=get_secret_hash(client_secret, username)
    auth_params = {"AuthParameters":
            {
                "USERNAME":username,
                "PASSWORD":password,
                "SECRET_HASH":json_secret_hash},
                "AuthFlow":"USER_PASSWORD_AUTH",
                "ClientId":client_id
            }

    auth_params=json.dumps(auth_params)
    headers={
        "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth",
        "Content-Type": "application/x-amz-json-1.1"
        }
    
    response = requests.request( "POST", url, auth=(username, password), headers=headers, data=auth_params )
    response = json.loads(response.text)
    auth_result = response['AuthenticationResult']
    access_token = auth_result['AccessToken']

    print(access_token)



if __name__ == '__main__':
    getCognitoToken()
    

    # Iterating through the json
    # list
    #for i in data['emp_details']:
    #    print(i)
    