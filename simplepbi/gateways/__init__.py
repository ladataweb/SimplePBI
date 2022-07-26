'''
  /¯¯¯¯¯¯¯¯¯\
 /           \
|   |   __    |  *********************************************
|   |  |  \   |  Code writen by Ignacio and Martin.
|   |  |  |   |
|   |__|_ |   |  La Data Web 
|      |__/   |  *********************************************
 \            /
  \__________/
  
'''

import json
import requests

class Gateways():
    """Simple library to use the Power BI api and obtain gateways and sources from it. The user must have gateway admin permissions.
    """

    def __init__(self, token):
        """Create a simplePBI object to request admin API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
               
    def get_gateway(self, gateway_id):
        """Returns the specified gateway.
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id. 
        ### Returns
        ----
        Dict:
            A dictionary containing a gateway.
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/gateways/{}".format(gateway_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                    
    def get_gateways(self):
        """Returns a list of gateways for which the user is an admin.
        ### Returns
        ----
        Dict:
            A dictionary containing all the gateways.
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/gateways"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def get_datasource(self, gateway_id, datasource_id):
        """Returns a list of datasources for the specified gateway.
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id
        datasource_id: str uuid
            The data source id of a gateway
        ### Returns
        ----
        Dict:
            A dictionary containing the datasource in the gateway.
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.            
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources/{}".format(gateway_id, datasource_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_datasource_status(self, gateway_id, datasource_id):
        """Checks the connectivity status of the specified data source from the specified gateway.
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id
        datasource_id: str uuid
            The data source id of a gateway
        ### Returns
        ----
        Dict:
            A dictionary containing the datasource in the gateway.
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources/{}/status".format(gateway_id, datasource_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            try:
                return res.json()
            except:
                return res.text
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_datasource_users(self, gateway_id, datasource_id):
        """Returns a list of users who have access to the specified data source.
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id
        datasource_id: str uuid
            The data source id of a gateway
        ### Returns
        ----
        Dict:
            A dictionary containing the datasource in the gateway.
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources/{}/users".format(gateway_id, datasource_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_datasources(self, gateway_id):
        """Returns a list of datasources for the specified gateway.
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the gateway.
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources".format(gateway_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def simple_add_datasource_user(self, gateway_id, datasource_id, datasourceAccessRight, emailAddress):
        """Grants or updates the permissions required to use the specified data source for the specified user.
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id
        datasource_id: str uuid
            The data source id of a gateway
        ### Request Body
        ----
        datasourceAccessRight: DatasourceUserAccessRight str
            The access right (permission level) that a user has on the data source. Options: { None, Read, ReadOverrideEffectiveIdentity }
        emailAddress: str
            The email address of the user            
        ### Returns
        ----
        Response object from requests library. 202 OK
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources/{}/users".format(gateway_id, datasource_id)
            body = {
                "emailAddress": emailAddress,
                "datasourceAccessRight": datasourceAccessRight
            }
            
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)         

            
    def simple_delete_datasource_user(self, gateway_id, datasource_id, emailAdress):
        """Deletes the specified data source from the specified gateway.
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id
        datasource_id: str uuid
            The data source id of a gateway
        emailAdress: str
            The user's email address or the object ID of the service principal
        ### Returns
        ----
        Dict:
            A status code 200 OK
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.            
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources/{}/users/{}".format(gateway_id, datasource_id, emailAdress)
            res = requests.delete(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
''' Requests failing for now

    def simple_create_datasource_preview(self, gateway_id, dataSourceType, connectionDetails, datasourceName, credentialType, credentials, privacyLevel=None ):
        """Grants or updates the permissions required to use the specified data source for the specified user.
        Encryption by default "RSA-OAEP"
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id.
        ### Request Body
        ----
        dataSourceType: str
            The data source type
        connectionDetails: str
            The connection details. E.g "{\"server\":\"MyServer\",\"database\":\"MyDatabase\"}"       
        datasourceName: str
            	The data source name
        credentialDetails: dict
            credentialType: { Anonymous, Basic, Key, Windows }. OAuth2 is not supported
            credentials: The credentials, which depend on the 'credentialType' value. For more information, see Update Datasource examples at Docs.            
            privacyLevel: The privacy level, which is relevant when combining data from multiple sources. { None, Organizational, Private, Public }
        ### Returns
        ----
        Response object from requests library. 202 OK
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources".format(gateway_id)
            body = {
                "dataSourceType": dataSourceType,
                "connectionDetails": connectionDetails,
                "datasourceName": datasourceName,
                "credentialDetails": {
                    "credentialType": credentialType,
                    "credentials": credentials,
                    "encryptedConnection": "Encrypted",                    
                    "encryptionAlgorithm": "RSA-OAEP",
                    "privacyLevel": privacyLevel
                }
            }             
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                         
    def simple_update_datasource_preview(self, gateway_id, datasource_id, credentialType, credentials, privacyLevel=None ):
        """Grants or updates the permissions required to use the specified data source for the specified user.
        Encryption by default "RSA-OAEP"
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id.
        datasource_id: str uuid
            The data source id of a gateway
        ### Request Body
        ----
        credentialDetails: dict
            credentialType: { Anonymous, Basic, Key, Windows, OAuth2 }.
            credentials: The credentials, which depend on the 'credentialType' value. For more information, see Update Datasource examples at Docs.
            privacyLevel: The privacy level, which is relevant when combining data from multiple sources. { None, Organizational, Private, Public }      
        ### Returns
        ----
        Response object from requests library. 202 OK
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources/{}".format(gateway_id, datasource_id)
            body = {
                "credentialDetails": {
                    "credentialType": credentialType,
                    "credentials": credentials,
                    "encryptedConnection": "Encrypted",                    
                    "encryptionAlgorithm": "None",
                    "privacyLevel": privacyLevel
                }
            }             
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.patch(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def delete_datasource(self, gateway_id, datasource_id):
        """Deletes the specified data source from the specified gateway.
        ### Parameters
        ----
        gateway_id: str uuid
            The Power Bi gateway id
        datasource_id: str uuid
            The data source id of a gateway
        ### Returns
        ----
        Dict:
            A status code 200 OK
        ### Limitations
        ----
        Virtual network (VNet) gateways aren't supported.            
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/gateways/{}/datasources/{}".format(gateway_id, datasource_id)
            res = requests.delete(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
'''