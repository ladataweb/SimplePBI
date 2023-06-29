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
@........|____| |  | |...*   *.@    Copyright © 2023 Ignacio Barrau
@   .       . | |__| |. *     *@
@   .       . |_____/ . *     *@    *********************************************
@   .       .         . *     *@
@   .       .         . *******@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''

import requests

class Azpause():
    """Simple library to use the Azure management resource to pause or resume AAS and PBI Embedded.
    """

    def __init__(self, tenant_id, client_id, client_secret):
        """Create a simplePBI azure on off to get authentication token.
        
        Service principal authentication (set use_service_principal to True)
            Provide:    tenant_id
                        power_bi_client_id
                        power_bi_secret
                        use_service_principal=True
        Args:
            tenant_id : String
                Tenant ID to connect to.
            client_id : String
                Client ID (also known as App ID)
                Password to use when authenticating.
            ecret : String
                The secret to authenticate with the Client ID.
            use_service_principal : Bool
                False by default, if set to true it will authenticate using power_bi_client_id and power_bi_secret.
        """        
        
        authority_url = 'https://login.microsoftonline.com/' + tenant_id + "/oauth2/token/"
        resource = 'https://management.azure.com/'
        resource2 =  'https://management.core.windows.net/'
        
        body = {
        "grant_type":"client_credentials",
        "client_id":client_id,
        "client_secret":client_secret,
        "resource":resource
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
            }
        try:
            r = requests.post(url = authority_url, data = body, headers = headers)
            self.token = r.json().get('access_token')
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except Exception as e:
                print(e)
                
    def pause_resource(self, subscriptionId, resourceGroupName, resourceType, resourceName):
        """Function to pause Azure Analysis Services or PowerBi Embedded capacity
        ### Parameters
        ----
        subscriptionId: str uuid
            The Azure subscription id
        resourceGroupName: str
            The Azure resource group name containing the resource
        resourceType: str
            The Azure resource type. It can be "FABRIC", "AAS" or "PBI"
        resourceName: str
            The Azure resource name. If it's AAS server name, if it's PBI embedded then capacity name.
        ### Returns
        ----
        Dict:
            A dictionary containing the specified installed app.
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            if resourceType == "FABRIC":
                resource = "Microsoft.Fabric/capacities"
                version = "2022-07-01-preview"
            elif resourceType == "AAS":
                resource = "Microsoft.AnalysisServices/servers"
                version = "2017-08-01"
            elif resourceType == "PBI":
                resource = "Microsoft.PowerBIDedicated/capacities"
                version = "2021-01-01"
            else:
                raise ValueError("resourceType must be AAS or PBI")                
            url = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/{}/{}/suspend?api-version={}".format(subscriptionId, resourceGroupName, resource, resourceName, version)
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def resume_resource(self, subscriptionId, resourceGroupName, resourceType, resourceName):
        """Function to resume Azure Analysis Services or PowerBi Embedded capacity
        ### Parameters
        ----
        subscriptionId: str uuid
            The Azure subscription id
        resourceGroupName: str
            The Azure resource group name containing the resource
        resourceType: str
            The Azure resource type. It can be "FABRIC", "AAS" or "PBI"
        resourceName: str
            The Azure resource name. If it's AAS server name, if it's PBI embedded then capacity name.
        ### Returns
        ----
        Dict:
            A dictionary containing the specified installed app.
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            if resourceType == "FABRIC":
                resource = "Microsoft.Fabric/capacities"
                version = "2022-07-01-preview"
            elif resourceType == "AAS":
                resource = "Microsoft.AnalysisServices/servers"
                version = "2017-08-01"
            elif resourceType == "PBI":
                resource = "Microsoft.PowerBIDedicated/capacities"
                version = "2021-01-01"
            else:
                raise ValueError("resourceType must be AAS or PBI") 
            url = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/{}/{}/resume?api-version={}".format(subscriptionId, resourceGroupName, resource, resourceName, version)
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
