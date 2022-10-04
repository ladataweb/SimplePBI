'''.
           @@@@@@@@@@
       @@@@..........@@@@
    @@@         .        @@@
  @@.           .         . @@
 @  .     _     .         .   @
@........| |...................@    *********************************************
@      . | |   _____  .        @
@      . | |  |  __ \ .        @    La Data Web
@      . | |__| |  | |.   ***  @
@........|____| |  | |...*   *.@    Copyright © 2022 Ignacio Barrau
@   .       . | |__| |. *     *@
@   .       . |_____/ . *     *@    *********************************************
@   .       .         . *     *@
@   .       .         . *******@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''

import json
import requests

class Token():
    """Simple library to use the Power BI api and obtain datasets from it.
    """

    def __init__(self, tenant_id=None, power_bi_client_id=None, power_bi_username=None, power_bi_password=None, power_bi_secret=None, use_service_principal=False):
        """Create a simplePBI object to get authentication token.
        
        You can use:
            1) User and pass authentication
                Provide:    tenant_id
                            power_bi_client_id
                            power_bi_username
                            power_bi_password
            2) Service principal authentication (set use_service_principal to True)
                Provide:    tenant_id
                            power_bi_client_id
                            power_bi_secret
                            use_service_principal=True
        Args:
            tenant_id : String
                Tenant ID to connect to.
            power_bi_client_id : String
                Client ID (also known as App ID)
            power_bi_username : String
                Username to use when authenticating.
            power_bi_password : String
                Password to use when authenticating.
            power_bi_secret : String
                The secret to authenticate with the Client ID.
            use_service_principal : Bool
                False by default, if set to true it will authenticate using power_bi_client_id and power_bi_secret.
        """

        POWER_BI_RESOURCE_ENDPOINT = "https://analysis.windows.net/powerbi/api"
        MICROSOFT_OAUTH2_API_ENDPOINT = "https://login.microsoftonline.com/" + tenant_id + "/oauth2/token/"
        if not use_service_principal:
            try:
                url = MICROSOFT_OAUTH2_API_ENDPOINT
                body = {
                    "resource":POWER_BI_RESOURCE_ENDPOINT, 
                    "client_id":power_bi_client_id,
                    "grant_type":"password",
                    "username":power_bi_username,
                    "password":power_bi_password,
                    "scope":"openid"                    
                }
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded"
                    }
                r = requests.post(url = url, data = body, headers = headers)
                access_token = r.json().get('access_token')
                self.token = access_token
            except requests.exceptions.HTTPError as ex:
                print(ex)
            except Exception as e:
                print(e)
        else:
            try:
                url = MICROSOFT_OAUTH2_API_ENDPOINT #is this different?
                body = {
                    "grant_type":"client_credentials",
                    "client_id":power_bi_client_id,
                    "client_secret":power_bi_secret,
                    "resource":POWER_BI_RESOURCE_ENDPOINT            
                }
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded"
                    }
                r = requests.post(url = url, data = body, headers = headers)
                access_token = r.json().get('access_token')
                self.token = access_token
            except requests.exceptions.HTTPError as ex:
                print(ex)
    
    