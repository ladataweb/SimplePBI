r'''.
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
from simplepbi import utils
import pandas as pd
import math

class Datasets():
    """Simple library to use the Power BI api and obtain datasets from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request admin API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
    
    def get_dataset(self, dataset_id):
        """Returns the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a dataset in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}".format(dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_dataset_in_group(self, workspace_id, dataset_id):
        """Returns the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a dataset in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}".format(workspace_id, dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_datasets(self):
        """Returns a list of datasets from My workspace.
        ### Parameters
        ----
        None
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasets in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_datasets_in_group(self, workspace_id):
        """Returns a list of datasets from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasets in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def get_datasources(self, dataset_id):
        """Returns a list of data sources for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the dataset from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/datasources".format(dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_datasources_in_group(self, workspace_id, dataset_id):
        """Returns a list of data sources for the specified dataset from the specified workspace
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the dataset from the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/datasources".format(workspace_id, dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_dataset_to_dataflows_links_in_group(self, workspace_id):
        """Returns a list of upstream dataflows for datasets from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all upstream dataflows in the dataset from a workspace
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/upstreamDataflows".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            if res.text == '':
                res.raise_for_status()
                return res
            else:
                res.raise_for_status()
                return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def get_direct_query_refresh_schedule(self, dataset_id):
        """Returns the refresh schedule for a specified DirectQuery or LiveConnection dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing the direct query refresh schedule in a dataset from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/directQueryRefreshSchedule".format(dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_direct_query_refresh_schedule_in_group(self, workspace_id, dataset_id):
        """Returns the refresh schedule for a specified DirectQuery or LiveConnection dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing the direct query refresh schedule in a dataset from a workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/directQueryRefreshSchedule".format(workspace_id, dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_gateway_datasources(self, dataset_id):
        """This API is deprecated, use Get Datasources instead.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        """
        print("This API is deprecated, use Get Datasources instead.")
    def get_gateway_datasources_in_group(self, dataset_id):
        """This API is deprecated, use Get Datasources In Group instead.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        """
        print("This API is deprecated, use Get Datasources In Group instead.")
        
    def get_parameters(self, dataset_id):
        """Returns a list of parameters for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the parameters in the dataset from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/parameters".format(dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_parameters_in_group(self, workspace_id, dataset_id):
        """Returns a list of parameters for the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the parameters in the dataset from workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/parameters".format(workspace_id, dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
    
    def get_refresh_history(self, dataset_id, top=None):
        """Returns the refresh history for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        top: int
            The requested number of entries in the refresh history. If not provided, the default is all available entries.
        ### Returns
        ----
        Dict:
            A dictionary containing a refresh history in a dataset in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/refreshes".format(dataset_id)
            if top != None:
                url = url + "?$top={}".format(str(top))
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_refresh_history_in_group(self, workspace_id, dataset_id, top=None):
        """Returns the refresh history for the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        top: int
            The requested number of entries in the refresh history. If not provided, the default is all available entries.
        ### Returns
        ----
        Dict:
            A dictionary containing a refresh history in a dataset from workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/refreshes".format(workspace_id, dataset_id)
            if top != None:
                url = url + "?$top={}".format(str(top))
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_refresh_schedule(self, dataset_id):
        """Returns the refresh schedule for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a refresh schedule in a dataset from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/refreshSchedule".format(dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_refresh_schedule_in_group(self, workspace_id, dataset_id):
        """Returns the refresh schedule for the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a refresh schedule in a dataset from workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/refreshSchedule".format(workspace_id, dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def refresh_dataset(self, dataset_id, notifyOption):
        """Triggers a refresh for the specified dataset from My workspace.
        For Shared capacities, a maximum of eight requests per day, which includes refreshes executed using a scheduled refresh.
        ### Parameters
        ----    
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        notifyOption: NotifyOption str
            Mail notification options (success and/or failure, or none). Options: { MailOnCompletion, MailOnFailure, NoNotification }
        ### Returns
        ----
        Response object from requests library. 202 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/refreshes".format(dataset_id)
            body = {
                "notifyOption": notifyOption 
            }                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def refresh_dataset_in_group(self, workspace_id, dataset_id, notifyOption):
        """Triggers a refresh for the specified dataset from the specified workspace.
        For Shared capacities, a maximum of eight requests per day, which includes refreshes executed using a scheduled refresh.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        notifyOption: NotifyOption str
            Mail notification options (success and/or failure, or none). Options: { MailOnCompletion, MailOnFailure, NoNotification }
        ### Returns
        ----
        Response object from requests library. 202 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/refreshes".format(workspace_id, dataset_id)
            body = {
                "notifyOption": notifyOption 
            }               
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def take_over_dataset_in_group(self, workspace_id, dataset_id):
        """Transfers ownership over the specified dataset to the current authorized user.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        None
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/Default.TakeOver".format(workspace_id, dataset_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def discover_gateways(self, dataset_id):
        """Returns a list of gateways that the specified dataset from My workspace can be bound to.
        This API call is only relevant to datasets that have at least one on-premises connection. For datasets with cloud-only connections, this API call returns an empty list.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a list of gateways from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/Default.DiscoverGateways".format(dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def discover_gateways_in_group(self, workspace_id, dataset_id):
        """Returns a list of gateways that the specified dataset from the specified workspace can be bound to.
        This API call is only relevant to datasets that have at least one on-premises connection. For datasets with cloud-only connections, this API call returns an empty list.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a list of gateways from the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/Default.DiscoverGateways".format(workspace_id, dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def delete_dataset(self, dataset_id):
        """Deletes the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}".format(dataset_id)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def delete_dataset_in_group(self, workspace_id, dataset_id):
        """Deletes the specified dataset from the specified workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}".format(workspace_id, dataset_id)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def execute_queries(self, dataset_id, query, return_pandas=False):
        """Executes Data Analysis Expressions (DAX) queries against the provided dataset. The dataset must reside in My workspace or another new workspace experience workspace.
        DAX query errors will result in: A response error, such as DAX query failure. A failure HTTP status code (400).
        Limitation: A query that requests more than one table, or more than 100,000 table rows, will result in Error.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        query: str
            DAX query returning a Table. Starts with EVALUATE
        return_pandas: bool
            Flag to specify if you want to return a dict response or a pandas dataframe of events.
        ### Returns
        ----
        If return_pandas = True returns a Pandas dataframe concatenating iterations otherwise it returns a dict of the response
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/executeQueries".format(dataset_id)
            body = {"queries": [{"query": query}], "serializerSettings": {"includeNulls": "true"}}
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)      
            #Encode text in json to avoid Unexpected UTF-8 BOM (decode using utf-8-sig)
            encoded_data = json.loads(res.text.encode().decode('utf-8-sig'))
            if return_pandas:
                #get columns from json response - keys from dict
                tabla_columnas = list(encoded_data['results'][0]['tables'][0]['rows'][0].keys())
                columnas = [columnita.split("[")[1].split("]")[0] for columnita in tabla_columnas]
                print(columnas)
                #get the number of rows to loop data
                rows = len(encoded_data['results'][0]['tables'][0]['rows'])        
                print(rows)
                #get data from json response - values from dict
                datos = [list(encoded_data['results'][0]['tables'][0]['rows'][n].values()) for n in range(rows-1)]
                print("datos")
                #build a dataframe from the collected data
                df = pd.DataFrame(data=datos, columns=columnas)
                print(df.head())
                return df
            else:
                return encoded_data
        except requests.exceptions.HTTPError as ex:
            print("ERROR ", ex)
        except Exception as e:
            print("ERROR ", e)
            
    def execute_queries_in_group(self, workspace_id, dataset_id, query, return_pandas=False, impersonatedUserName=None):
        """Executes Data Analysis Expressions (DAX) queries against the provided dataset. The dataset must reside in My workspace or another new workspace experience workspace.
        DAX query errors will result in: A response error, such as DAX query failure. A failure HTTP status code (400).
        Limitation: A query that requests more than one table, or more than 100,000 table rows, will result in Error.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL    
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL        
        return_pandas: bool
            Flag to specify if you want to return a dict response or a pandas dataframe of events.
        ### Body
        ----
        query: str
            Requested. DAX query returning a Table. Starts with EVALUATE
        impersonatedUserName: str
            The UPN of a user to be impersonated. If the model is not RLS enabled, this will be ignored. E.g. "someuser@mycompany.com"
        ### Returns
        ----
        If return_pandas = True returns a Pandas dataframe concatenating iterations otherwise it returns a dict of the response
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/executeQueries".format(workspace_id, dataset_id)
            body = {"queries": [{"query": query}], "serializerSettings": {"includeNulls": "true"}}
            if impersonatedUserName != None:
                body["impersonatedUserName"]=impersonatedUserName
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)      
            res.raise_for_status()
            #Encode text in json to avoid Unexpected UTF-8 BOM (decode using utf-8-sig)
            encoded_data = json.loads(res.text.encode().decode('utf-8-sig'))
            if return_pandas:
                #get columns from json response - keys from dict
                tabla_columnas = list(encoded_data['results'][0]['tables'][0]['rows'][0].keys())
                columnas = [columnita.split("[")[1].split("]")[0] for columnita in tabla_columnas]
                print(columnas)
                #get the number of rows to loop data
                rows = len(encoded_data['results'][0]['tables'][0]['rows'])        
                print(rows)
                #get data from json response - values from dict
                datos = [list(encoded_data['results'][0]['tables'][0]['rows'][n].values()) for n in range(rows-1)]
                print("datos")
                #build a dataframe from the collected data
                df = pd.DataFrame(data=datos, columns=columnas)
                print(df.head())
                return df
            else:
                return encoded_data
        except requests.exceptions.HTTPError as ex:
            print("ERROR ", ex)
        except Exception as e:
            print("ERROR ", e)
            
    def update_parameters(self, dataset_id, updateDetails):
        """Updates the parameters values for the specified dataset from My workspace.
        If you're using enhanced dataset metadata, refresh the dataset to apply the new parameter values.
        If you're not using enhanced dataset metadata, wait 30 minutes for the update data sources operation to complete, and then refresh the dataset.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        updateDetails: UpdateMashupParameterDetails [] str
            The dataset parameter list to update. Example:
            [
                {
                    "name": "ParameterName1",
                    "newValue": "NewDB"
                },
                {
                    "name": "ParameterName2",
                    "newValue": "5678"
                }
            ]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        Datasets created using the public XMLA endpoint aren't supported. To make changes to those data sources, the admin must use the Azure Analysis Services client library for Tabular Object Model.
        DirectQuery connections are only supported with enhanced dataset metadata.
        Datasets with Azure Analysis Services live connections aren't supported.
        Maximum of 100 parameters per request.
        All specified parameters must exist in the dataset.
        Parameters values should be of the expected type.
        The parameter list cannot be empty or include duplicate parameters.
        Parameters names are case-sensitive.
        Parameter IsRequired must have a non-empty value.
        The parameter types Any and Binary cannot be updated.
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/Default.UpdateParameters".format(dataset_id)
            body = {
                "updateDetails": updateDetails
            }               
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_parameters_in_group(self, workspace_id, dataset_id, updateDetails):
        """Updates the parameters values for the specified dataset from the specified workspace.
        If you're using enhanced dataset metadata, refresh the dataset to apply the new parameter values.
        If you're not using enhanced dataset metadata, wait 30 minutes for the update data sources operation to complete, and then refresh the dataset.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        updateDetails: UpdateMashupParameterDetails [] str
            The dataset parameter list to update. Example:
            [
                {
                    "name": "ParameterName1",
                    "newValue": "NewDB"
                },
                {
                    "name": "ParameterName2",
                    "newValue": "5678"
                }
            ]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        Datasets created using the public XMLA endpoint aren't supported. To make changes to those data sources, the admin must use the Azure Analysis Services client library for Tabular Object Model.
        DirectQuery connections are only supported with enhanced dataset metadata.
        Datasets with Azure Analysis Services live connections aren't supported.
        Maximum of 100 parameters per request.
        All specified parameters must exist in the dataset.
        Parameters values should be of the expected type.
        The parameter list cannot be empty or include duplicate parameters.
        Parameters names are case-sensitive.
        Parameter IsRequired must have a non-empty value.
        The parameter types Any and Binary cannot be updated.
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/Default.UpdateParameters".format(workspace_id, dataset_id)
            body = {
                "updateDetails": updateDetails
            }               
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_refresh_schedule(self, dataset_id, NotifyOption=None, days=None, enabled=None, localTimeZoneId=None, times=None):
        """Updates the refresh schedule for the specified dataset from My workspace.
        A request that disables the refresh schedule should contain no other changes.
        At least one day must be specified. If no times are specified, then Power BI will use a default single time per day.        
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        NotifyOption: ScheduleNotifyOption str
            Notification option at scheduled refresh termination. Example MailOnFailure or NoNotification.
        days: str []
            Days to execute the refresh. Example: ["Sunday", "Tuesday"]
        enabled: bool
            is the refresh enabled
        localTimeZoneId: str
            The ID of the timezone to use. See TimeZone Info. Example "UTC"
        times: str []
            Times to execute the refresh within each day. Example: ["07:00", "16:00"]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        The limit on the number of time slots per day depends on whether a Premium or Shared capacity is used.
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/refreshSchedule".format(dataset_id)
            body = {
                "value": {}
            }
            
            if NotifyOption != None:
                body["value"]["NotifyOption"]=NotifyOption
            if days != None:
                body["value"]["days"] = days
            if enabled != None:
                body["value"]["enabled"] = enabled
            if localTimeZoneId != None:
                body["value"]["localTimeZoneId"] = localTimeZoneId
            if times != None:
                body["value"]["times"]=times
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_refresh_schedule_in_group(self, workspace_id, dataset_id, NotifyOption=None, days=None, enabled=None, localTimeZoneId=None, times=None):
        """Updates the refresh schedule for the specified dataset from the specified workspace.
        A request that disables the refresh schedule should contain no other changes.
        At least one day must be specified. If no times are specified, then Power BI will use a default single time per day.       
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        NotifyOption: ScheduleNotifyOption str
            Notification option at scheduled refresh termination. Example MailOnFailure or NoNotification.
        days: str []
            Days to execute the refresh. Example: ["Sunday", "Tuesday"]
        enabled: bool
            is the refresh enabled
        localTimeZoneId: str
            The ID of the timezone to use. See TimeZone Info. Example "UTC"
        times: str []
            Times to execute the refresh within each day. Example: ["07:00", "16:00"]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        The limit on the number of time slots per day depends on whether a Premium or Shared capacity is used.
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/refreshSchedule".format(workspace_id, dataset_id)
            body = {
                "value": {}
            }
            
            if NotifyOption != None:
                body["value"]["NotifyOption"]=NotifyOption
            if days != None:
                body["value"]["days"] = days
            if enabled != None:
                body["value"]["enabled"] = enabled
            if localTimeZoneId != None:
                body["value"]["localTimeZoneId"] = localTimeZoneId
            if times != None:
                body["value"]["times"]=times
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def bind_to_gateway_preview(self, dataset_id, gatewayObjectId, datasourceObjectIds):
        """Binds the specified dataset from My workspace to the specified gateway, optionally with a given set of data source IDs. If you don’t supply a specific data source ID, the dataset will be bound to the first matching data source in the gateway. Only supports the on-premises data gateway
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        gatewayObjectId: str uuid
            The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster and is similar to the gateway cluster ID.
        datasourceObjectIds: str []
            The unique identifier for the datasource in the gateway
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/Default.BindToGateway".format(dataset_id)
            body = {
                "gatewayObjectId": gatewayObjectId,
                "datasourceObjectIds": datasourceObjectIds
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def bind_to_gateway_in_group_preview(self, workspace_id, dataset_id, gatewayObjectId, datasourceObjectIds):
        """Binds the specified dataset from the specified workspace to the specified gateway, optionally with a given set of data source IDs. If you don’t supply a specific data source ID, the dataset will be bound to the first matching data source in the gateway. Only supports the on-premises data gateway
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        gatewayObjectId: str uuid
            The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster and is similar to the gateway cluster ID.
        datasourceObjectIds: str []
            The unique identifier for the datasource in the gateway
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/Default.BindToGateway".format(workspace_id, dataset_id)
            body = {
                "gatewayObjectId": gatewayObjectId,
                "datasourceObjectIds": datasourceObjectIds
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_direct_query_refresh_schedule_in_group_preview(self, dataset_id, frequency=None, days=None, enabled=None, localTimeZoneId=None, times=None):
        """Updates the refresh schedule for a specified DirectQuery or LiveConnection dataset from My workspace.
        A request should contain either a set of days and times or a valid frequency, but not both. If you choose a set of days without specifying any times, then Power BI will use a default single time per day. Setting the frequency will automatically overwrite the days and times setting.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        frequency: int
            The interval in minutes between successive refreshes. Supported values are 15, 30, 60, 120, and 180.
        days: str []
            Days to execute the refresh. Example: ["Sunday", "Tuesday"]
        enabled: bool
            is the refresh enabled
        localTimeZoneId: str
            The ID of the timezone to use. See TimeZone Info. Example "UTC"
        times: str []
            Times to execute the refresh within each day. Example: ["07:00", "16:00"]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        The limit on the number of time slots per day depends on whether a Premium or Shared capacity is used.
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/directQueryRefreshSchedule".format(dataset_id)
            body = {
                "value": {}
            }
            
            if frequency != None:
                body["value"]["frequency"]=frequency
            if days != None:
                body["value"]["days"] = days
            if enabled != None:
                body["value"]["enabled"] = enabled
            if localTimeZoneId != None:
                body["value"]["localTimeZoneId"] = localTimeZoneId
            if times != None:
                body["value"]["times"]=times
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_direct_query_refresh_schedule_in_group_preview(self, workspace_id, dataset_id, frequency=None, days=None, enabled=None, localTimeZoneId=None, times=None):
        """Updates the refresh schedule for a specified DirectQuery or LiveConnection dataset from the specified workspace.
        A request should contain either a set of days and times or a valid frequency, but not both. If you choose a set of days without specifying any times, then Power BI will use a default single time per day. Setting the frequency will automatically overwrite the days and times setting.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        frequency: int
            The interval in minutes between successive refreshes. Supported values are 15, 30, 60, 120, and 180.
        days: str []
            Days to execute the refresh. Example: ["Sunday", "Tuesday"]
        enabled: bool
            is the refresh enabled
        localTimeZoneId: str
            The ID of the timezone to use. See TimeZone Info. Example "UTC"
        times: str []
            Times to execute the refresh within each day. Example: ["07:00", "16:00"]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        The limit on the number of time slots per day depends on whether a Premium or Shared capacity is used.
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/directQueryRefreshSchedule".format(workspace_id, dataset_id)
            body = {
                "value": {}
            }
            
            if frequency != None:
                body["value"]["frequency"]=frequency
            if days != None:
                body["value"]["days"] = days
            if enabled != None:
                body["value"]["enabled"] = enabled
            if localTimeZoneId != None:
                body["value"]["localTimeZoneId"] = localTimeZoneId
            if times != None:
                body["value"]["times"]=times
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_datasources_in_group_preview(self, workspace_id, dataset_id, updateDetails):
        """Updates the data sources of the specified dataset from the specified workspace.
        Only these data sources are supported: SQL Server, Azure SQL Server, Azure Analysis Services, Azure Synapse, OData, SharePoint, Teradata, and SAP HANA.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body (PLEASE READ THE DOCS)
        ----
        UpdateDetails[]: list
            A list of data source connection update requests. PLEASE READ THE DOCS
            E.g.[
                {
                  "datasourceSelector": {
                    "datasourceType": "Sql",
                    "connectionDetails": {
                      "server": "My-Sql-Server",
                      "database": "My-Sql-Database"
                    }
                  },
                  "connectionDetails": {
                    "server": "New-Sql-Server",
                    "database": "New-Sql-Database"
                  }
                }
            ]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        Datasets created using the public XMLA endpoint aren't supported.
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/Default.UpdateDatasources".format(workspace_id, dataset_id)
            body = {
                "updateDetails": updateDetails
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)            
            
    def enhanced_refresh_dataset_in_group(self, workspace_id, dataset_id, objects, typeProcessing="Full", commitMode="transactional", maxParallelism=1, retryCount=1, applyRefreshPolicy=True):
        """Triggers a refresh for the specified dataset from the specified workspace.
        For Shared capacities, a maximum of eight requests per day, which includes refreshes executed using a scheduled refresh.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL        
        ### Request Body
        ----
        typeProcessing: Enum (str)
            The type of processing to perform. Types are aligned with the TMSL refresh command types: full, clearValues, calculate, dataOnly, automatic, and defragment. Add type isn't supported.
        commitMode: Enum (str)
            Determines if objects will be committed in batches or only when complete. Modes include: transactional, partialBatch.
        maxParallelism: int
            Determines the maximum number of threads on which to run processing commands in parallel. This value aligned with the MaxParallelism property that can be set in the TMSL Sequence command or by using other methods.
        retryCount: int
            Number of times the operation will retry before failing.
        objects: array
            An array of objects to be processed. Each object includes table when processing the entire table, or table and partition when processing a partition. If no objects are specified, the entire dataset is refreshed.
            E.g. [ { "table": "DimCustomer", "partition": "DimCustomer" }  ,  { "table": "DimDate" } ]
        applyRefreshPolicy: boolean
            If an incremental refresh policy is defined, applyRefreshPolicy will determine if the policy is applied or not
        effectiveDate: date
            Comming Soon            
        ### Returns
        ----
        Response object from requests library. 202 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/refreshes".format(workspace_id, dataset_id)
            body = {
                "type": typeProcessing,
                "commitMode": commitMode,
                "maxParallelism": maxParallelism,
                "retryCount": retryCount,
                "objects": objects,
                "applyRefreshPolicy": applyRefreshPolicy
            }         
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_query_scaleout_sync_status(self, dataset_id):
        """Returns the query scale-out sync status for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing data about scaleout sync dataset in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/queryScaleOut/syncStatus".format(dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_query_scaleout_sync_status_in_group(self, workspace_id, dataset_id):
        """Returns the query scale-out sync status for the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing data about scaleout sync dataset in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/queryScaleOut/syncStatus".format(workspace_id, dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def trigger_query_scaleout_sync(self, dataset_id):
        """Triggers a query scale-out sync of read-only replicas for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL        
        ### Returns
        ----
        Response object from requests library. 202 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/queryScaleOut/sync".format(dataset_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def trigger_query_scaleout_sync_in_group(self, workspace_id, dataset_id):
        """Triggers a query scale-out sync of read-only replicas for the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL        
        ### Returns
        ----
        Response object from requests library. 202 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/queryScaleOut/sync".format(workspace_id, dataset_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_dataset_in_group(self, workspace_id, dataset_id, targetStorageMode=None, autoSyncReadOnlyReplicas=None, maxReadOnlyReplicas=None):
        """Updates the properties for the specified dataset from the specified workspace. The user must be the dataset owner.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Request Body
        ----
        autoSyncReadOnlyReplicas: bool
            Whether the dataset automatically syncs read-only replicas
        maxReadOnlyReplicas: int
            Maximum number of read-only replicas for the dataset (0-64, -1 for automatic number of replicas)
        UpdateDatasetRequest: str
            Update dataset request
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}".format(workspace_id, dataset_id)
            body = {
                "queryScaleOutSettings":{}
            }
            
            if targetStorageMode != None:
                body["targetStorageMode"]=targetStorageMode
            if autoSyncReadOnlyReplicas != None:
                body["queryScaleOutSettings"]["autoSyncReadOnlyReplicas"]=autoSyncReadOnlyReplicas
            if maxReadOnlyReplicas != None:
                body["queryScaleOutSettings"]["maxReadOnlyReplicas"]=maxReadOnlyReplicas
            if targetStorageMode==None and autoSyncReadOnlyReplicas==None and maxReadOnlyReplicas==None:
                print("Error: You need to specify a parameter to modify.")                
            else:
                headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
                res = requests.patch(url, data = json.dumps(body), headers = headers)
                res.raise_for_status()
                return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_tables_from_dataset_in_group(self, workspace_id, dataset_id):
        """Get the tables from specific dataset in a workspace
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL        
        ### Returns
        ----
        Response dict of tables from requests library. 200 OK
        """
        try:
            query = '''
            EVALUATE SELECTCOLUMNS( 
                		INFO.TABLES() 
                		, "ID", [ID]
                		, "Name", [Name]
                		, "IsHidden", [IsHidden]
                		, "ModifiedTime", [ModifiedTime]
                		, "StructureModifiedTime", [StructureModifiedTime]
                )
            '''
            diccio = "The request was limitated by Microsoft. Power Bi Rest API can't query INFO.DAX Functions for now. We are sorry about this."
            #diccio = self.execute_queries_in_group(workspace_id, dataset_id, query)
            if diccio is None:
                print("Error getting tables from dataset.")
            return diccio
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)        
            
    def get_measures_from_dataset_in_group(self, workspace_id, dataset_id):
        """Get all measures from specific dataset in a workspace
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL        
        ### Returns
        ----
        Response dict of measures from requests library. 200 OK
        """
        try:
            query = '''
            DEFINE
                	VAR _tablas = SELECTCOLUMNS(INFO.TABLES(), "TableID", [ID], "Name", [Name])
                	VAR _measures = SELECTCOLUMNS(INFO.MEASURES(), "TableID", [TableID], "MeasureID", [ID], "MeasureName", [Name], "Description", [Description], "ExplicitDataType", [DataType], "Expression", [Expression] )
                	VAR _map = SELECTCOLUMNS({ (1, "any"), (2, "text"), (6, "whole number"), (8, "decimal"), (9, "date or datetime"), (10, "fixed decimal"), (11, "bool")}, "ExplicitDataType", [Value1], "DataType", [Value2])
                	VAR _ready_measures = SELECTCOLUMNS(NATURALINNERJOIN(_measures, _tablas), "TableID", [TableID], "Name", [Name], "ItemType", "Measure", "ItemID", [MeasureID], "ItemName", [MeasureName], "Description", [Description], "ExplicitDataType", [ExplicitDataType], "Expression", [Expression])
                	VAR _measures_with_type = SELECTCOLUMNS(NATURALINNERJOIN(_ready_measures, _map), "TableID", [TableID], "Name", [Name], "ItemType", [ItemType], "ItemID", [ItemID], "ItemName", [ItemName], "Description", [Description], "DataType", [DataType], "Expression", [Expression])
            EVALUATE 
                	_measures_with_type
            '''
            diccio = "The request was limitated by Microsoft. Power Bi Rest API can't query INFO.DAX Functions for now. We are sorry about this."
            #diccio = self.execute_queries_in_group(workspace_id, dataset_id, query)
            if diccio is None:
                print("Error getting tables from dataset.")
            return diccio
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_columns_from_dataset_in_group(self, workspace_id, dataset_id):
        """Get all columns from specific dataset in a workspace
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL        
        ### Returns
        ----
        Response dict of measures from requests library. 200 OK
        """
        try:
            query = '''
            DEFINE
        			VAR _tablas = SELECTCOLUMNS(INFO.TABLES(), "TableID", [ID], "Name", [Name])
        			VAR _columnas = SELECTCOLUMNS(INFO.COLUMNS(), "TableID", [TableID], "ColumnID", [ID], "ColumnName", [ExplicitName], "ExplicitDataType", [ExplicitDataType], "Expression", [Expression])
        			VAR _map = SELECTCOLUMNS({ (1, "any"), (2, "text"), (6, "whole number"), (8, "decimal"), (9, "date or datetime"), (10, "fixed decimal"), (11, "bool")}, "ExplicitDataType", [Value1], "DataType", [Value2])
        			VAR _ready_columns = SELECTCOLUMNS(NATURALINNERJOIN(_columnas, _tablas), "TableID", [TableID], "Name", [Name], "ItemType", "Column", "ItemID", [ColumnID], "ItemName", [ColumnName], "ExplicitDataType", [ExplicitDataType], "Expression", [Expression])				
        			VAR _columns_with_type = SELECTCOLUMNS(NATURALINNERJOIN(_ready_columns, _map), "TableID", [TableID], "Name", [Name], "ItemType", [ItemType], "ItemID", [ItemID], "ItemName", [ItemName], "DataType", [DataType], "Expression", [Expression])
        		EVALUATE 
        			_columns_with_type
            '''
            diccio = "The request was limitated by Microsoft. Power Bi Rest API can't query INFO.DAX Functions for now. We are sorry about this."
            #diccio = self.execute_queries_in_group(workspace_id, dataset_id, query)
            if diccio is None:
                print("Error getting tables from dataset.")
            return diccio
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_roles_from_dataset_in_group(self, workspace_id, dataset_id):
        """Get all roles from specific dataset in a workspace
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL                
        ### Limitations
        ----
            This request will only work for User and Password credentials. It won't work with Service Principal due to API limitations.
        ### Returns
        ----
        Response dict of measures from requests library. 200 OK
        """
        try:
            query = '''
            EVALUATE 
                INFO.ROLES()
            '''
            diccio = "The request was limitated by Microsoft. Power Bi Rest API can't query INFO.DAX Functions for now. We are sorry about this."
            #diccio = self.execute_queries_in_group(workspace_id, dataset_id, query)
            if diccio is None:
                print("Error getting tables from dataset.")
            return diccio
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def create_doc_by_content_dataset_in_group(self, workspace_id, dataset_id, doc_type='text', path=None ):   
        """Create an html doc of a semantic model
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL                
        doc_type: str
            It can be file or string text
        path: str
            Path to store the html file like C:/Folder/SemanticModelDocument.html 
        ### Limitations
        ----
            API can't get info from Semantic models in direct lake and direct query.
            Service Principal can't query a semantic model with RLS by API
        ### Returns
        ----
        Returns a string of text of an html code to paste on a file or the literal file in the path specified
        """
        if 1 == 1:
            return "The request was limitated by Microsoft. Power Bi Rest API can't query INFO.DAX Functions for now. We are sorry about this."

        try:
            # Get Dataset details
            print("Getting Semantic Model Details...")
            dset = self.get_dataset_in_group(workspace_id, dataset_id)
            dsource = self.get_datasources_in_group(workspace_id, dataset_id)
            # Get Tables
            print("Getting Tables...")
            tabless = self.get_tables_from_dataset_in_group(workspace_id, dataset_id)
            df = utils.to_pandas(tabless['results'][0]['tables'][0], "rows")[["[Name]","[IsHidden]", "[ModifiedTime]","[StructureModifiedTime]"]]
            tabless_html = pd.DataFrame.to_html(df).replace('class="dataframe"', 'class="styled-table"')
            # Get Columns
            print("Getting Columns...")
            colss = self.get_columns_from_dataset_in_group(workspace_id, dataset_id)
            df_col = utils.to_pandas(colss['results'][0]['tables'][0], "rows")
            df_col = df_col[~df_col["[ItemName]"].str.contains("RowNumber", na=False) ]
            colss_html = pd.DataFrame.to_html(df_col[["[Name]","[ItemType]", "[ItemName]","[DataType]", "[Expression]"]]).replace('class="dataframe"', 'class="styled-table"')            
            # Build tables dict for diagram
            print("Getting Relationships...")
            query='''
            DEFINE
                VAR _tablas_from = SELECTCOLUMNS(INFO.TABLES(), "FromTableID", [ID], "FromName", [Name])
                VAR _tablas_to = SELECTCOLUMNS(INFO.TABLES(), "ToTableID", [ID], "ToName", [Name])
                VAR _rels = SELECTCOLUMNS(INFO.RELATIONSHIPS(), "FromTableID", [FromTableID], "ToTableID", [ToTableID], "FromCardinality", [FromCardinality], "ToCardinality", [ToCardinality], "FromColumnID", [FromColumnID], "ToColumnID", [ToColumnID] )
                VAR _ready_rels1 = SELECTCOLUMNS(NATURALINNERJOIN(_rels, _tablas_from), "FromTableID", [FromTableID], "FromName", [FromName], "ToTableID", [ToTableID], "FromCardinality", [FromCardinality], "ToCardinality", [ToCardinality], "FromColumnID", [FromColumnID], "ToColumnID", [ToColumnID] )
                VAR _ready_rels2 = SELECTCOLUMNS(NATURALINNERJOIN(_ready_rels1, _tablas_to), "FromTableID", [FromTableID], "FromName", [FromName], "ToTableID", [ToTableID], "ToName", [ToName], "FromCardinality", [FromCardinality], "ToCardinality", [ToCardinality], "FromColumnID", [FromColumnID], "ToColumnID", [ToColumnID] )
            EVALUATE 
                _ready_rels2
            '''
            rel = self.execute_queries_in_group(workspace_id, dataset_id, query=query)
            df_rel = utils.to_pandas(rel['results'][0]['tables'][0], "rows")
            key_columns = list(set(df_rel["[FromColumnID]"].tolist() + df_rel["[ToColumnID]"].tolist()))
            print("Building Diagram...")
            # Generating a matrix for adjusting diagram positions
            allin = []
            dic = {}
            columnas=[]
            raiz = math.sqrt(len(df))
            x = int(raiz)
            y = int(raiz)
            if x*y < len(df):
                x=x+1
            else:
                pass
            x_count=0
            y_count=0
            
            for i, row in df.iterrows():
                if y_count == y:
                    x_count= x_count+1
                    y_count=0
                else:
                    y_count= y_count+1
                #print("i es ",str(i),"(", str(par*100) , ", " , str(impar*100) + ")")
                dic["key"] = row["[Name]"]
                dic["location"] = "new go.Point(" + str(x_count*400) + ", " + str(y_count*100) + ")"
                for j, wor in df_col[df_col['[Name]'] == row["[Name]"]].iterrows():
                    if wor["[ItemName]"]!=None:
                        #if "RowNumber" not in wor["[ItemName]"]:
                        if wor["[ItemID]"] in key_columns:
                            columnas.append({"name":wor["[ItemName]"], 'iskey': 'true', 'figure': 'Decision', 'color': 'purple'})                
                        else:
                            columnas.append({"name":wor["[ItemName]"], 'iskey': 'false', 'figure': 'Circle', 'color': 'blue'})            
                dic["items"]=columnas
                dic["inheritedItems"]=[]
                allin.append(dic)
                dic = {}
                columnas=[]
            # Clean Table
            nodeDataArray = ','.join(map(str,allin))
            nodeDataArray = nodeDataArray.replace("'key'","key")
            nodeDataArray = nodeDataArray.replace("'name'","name")
            nodeDataArray = nodeDataArray.replace("'new","new")
            nodeDataArray = nodeDataArray.replace("0)'","0)")
            nodeDataArray = nodeDataArray.replace("'item'","item")
            nodeDataArray = nodeDataArray.replace("'iskey'","iskey")
            nodeDataArray = nodeDataArray.replace("'figure'","figure")
            nodeDataArray = nodeDataArray.replace("'color'","color")
            nodeDataArray = nodeDataArray.replace("'true'","true")
            nodeDataArray = nodeDataArray.replace("'false'","false")
            # Build relationships dict for diagram             
            relations = []
            for i, row in df_rel.iterrows():
                fromy = 1
                tomy = 1
                if row["[FromCardinality]"]== 2:
                    fromy="*"
                if row["[ToCardinality]"]== 2:
                    tomy="*"
                relations.append({ "from": row["[FromName]"], "to": row["[ToName]"], "text": fromy, "toText": tomy })
            # Clean Relationships
            linkDataArray = ','.join(map(str,relations))
            linkDataArray = linkDataArray.replace("'from'","from")
            linkDataArray = linkDataArray.replace("'to'","to")
            linkDataArray = linkDataArray.replace("'text'","text")
            linkDataArray = linkDataArray.replace("'toText'","toText")
            # Get Measures
            print("Getting Measures...")
            mea = self.get_measures_from_dataset_in_group(workspace_id, dataset_id)
            df_mea = utils.to_pandas(mea['results'][0]['tables'][0], "rows")[["[Name]","[ItemType]", "[ItemName]", "[Description]", "[DataType]", "[Expression]"]]
            mea_html = pd.DataFrame.to_html(df_mea).replace('class="dataframe"', 'class="styled-table"')
            
            print("Building Document...")
            # Create Document
            html_doc = '''
                <html lang="en"><head>
                <title>Semantic Model Document with SimplePBI</title>
                <meta name="description" content="This document was autogenerated with SimplePBI, the python library for Power Bi Rest API developed by ibarrau." />
                <meta name="generator" content="http://www.ladataweb.com.ar/">
                <meta name="author" content="ibarrau">
                <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
                <link rel="stylesheet" href="http://web.simmons.edu/~grovesd/comm244/css/notes.css" media="screen">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-3DEZ6EPPHR&amp;cx=c&amp;_slc=1"></script><script async="" src="https://www.google-analytics.com/analytics.js"></script><script src="http://web.simmons.edu/~grovesd/comm244/js/prism.js"></script><style type="text/css" id="operaUserStyle"></style>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                <script src="https://unpkg.com/gojs@3.0.10/release/go.js"></script>
                <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet" />
                <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
                <style>
                    .styled-table { 
                        margin: 25px 0;
                        border-collapse: collapse;
                        font-size: 0.9em;
                        font-family: sans-serif;
                        min-width: 400px;
                        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                    }
                    .styled-table thead tr {
                        background-color: #F3A977;
                        color: #ffffff;
                        text-align: left;
                    }
                    .styled-table th,
                    .styled-table td {
                        padding: 12px 15px;
                    }
                    .styled-table tbody tr {
                        border-bottom: 1px solid #dddddd;
                    }
                
                    .styled-table tbody tr:nth-of-type(even) {
                        background-color: #f3f3f3;
                    }
                
                    .styled-table tbody tr:last-of-type {
                        border-bottom: 2px solid #F3A977;
                    }
                    .styled-table tbody tr.active-row {
                        font-weight: bold;
                        color: #009879;
                    }
                </style>
                </head>
                
                <body>
                <!-- Button on top like "back"> <p class="backlink"><a href="../../week3">Back to Week 3 page »</a></p> -->
                <br>
                <h1>Semantic Model '''+dset['name']+''' documentation</h1>
                <br>
                <p>The semantic model was configured by '''+ dset['configuredBy'] +'''. The target storage mode is '''+ dset['targetStorageMode'] +'''. Its refresh setting is set to '''+ str(dset['isRefreshable']) +'''. The configuration for RLS is '''+str(dset['isEffectiveIdentityRolesRequired'])+'''. It was created the date '''+dset['createdDate']+'''.</p>
                <p>The sources types involved are '''+', '.join([item['datasourceType'] for item in dsource['value']])+'''.
                <p>In order to get started with the document we are splitting the document with the following sections, feel free to click on them to navigate fast to the topic:</p>
                <ul>
                    <li><a href="#Tables">Tables</a></li>
                    <li><a href="#Diagram">Model Diagram</a></li>
                    <li><a href="#Columns">Columns</a></li>
                    <li><a href="#Measures">Measures</a></li>
                </ul>
                <h2 id="Tables">Tables</h2>
                <p>Here you can find the list of tables in the data model.</p>
                
                '''+tabless_html+'''
                
                <h2 id="Diagram">Model Diagram</h2>
                
                <p>In addition you can see this data model interactive diagram. You can move tables, scroll or ctrl + wheel in order to adjust the view.</p>
                
                <div id="allSampleContent" class="p-4 w-full">
                          
                <script src="https://unpkg.com/create-gojs-kit@3.0.10/dist/extensions/Figures.js"></script>
                <script src="https://unpkg.com/create-gojs-kit@3.0.10/dist/extensions/Themes.js"></script>
                <script id="code">
                  function init() { 
                    myDiagram = new go.Diagram('myDiagramDiv', {
                      allowDelete: false,
                      allowCopy: false,
                      layout: new go.ForceDirectedLayout({ isInitial: false }),
                      'undoManager.isEnabled': true,
                      // use "Modern" themes from extensions/Themes
                      'themeManager.themeMap': new go.Map([
                        { key: 'light', value: Modern },
                        { key: 'dark', value: ModernDark }
                      ]),
                      'themeManager.changesDivBackground': true,
                      'themeManager.currentTheme': document.getElementById('theme').value
                    });
                
                    myDiagram.themeManager.set('light', {
                      colors: {
                        primary: '#f7f9fc',
                        green: '#62bd8e',
                        blue: '#3999bf',
                        purple: '#7f36b0',
                        red: '#c41000'
                      }
                    });
                    myDiagram.themeManager.set('dark', {
                      colors: {
                        primary: '#4a4a4a',
                        green: '#429e6f',
                        blue: '#3f9fc6',
                        purple: '#9951c9',
                        red: '#ff4d3d'
                      }
                    });
                
                    // the template for each attribute in a node's array of item data
                    const itemTempl = new go.Panel('Horizontal', { margin: new go.Margin(2, 0) })
                      .add(
                        new go.Shape({
                          desiredSize: new go.Size(15, 15),
                          strokeWidth: 0,
                          margin: new go.Margin(0, 5, 0, 0)
                        })
                          .bind('figure')
                          .themeData('fill', 'color'),
                        new go.TextBlock({
                          font: '14px sans-serif',
                          stroke: 'black'
                        })
                          .bind('text', 'name')
                          .bind('font', 'iskey', (k) => (k ? 'italic 14px sans-serif' : '14px sans-serif'))
                          .theme('stroke', 'text')
                      );
                
                    // define the Node template, representing an entity
                    myDiagram.nodeTemplate = new go.Node('Auto', { // the whole node panel
                      selectionAdorned: true,
                      resizable: true,
                      layoutConditions: go.LayoutConditions.Standard & ~go.LayoutConditions.NodeSized,
                      fromSpot: go.Spot.LeftRightSides,
                      toSpot: go.Spot.LeftRightSides
                    })
                      .bindTwoWay('location')
                      // whenever the PanelExpanderButton changes the visible property of the "LIST" panel,
                      // clear out any desiredSize set by the ResizingTool.
                      .bindObject('desiredSize', 'visible', (v) => new go.Size(NaN, NaN), undefined, 'LIST')
                      .add(
                        // define the node's outer shape, which will surround the Table
                        new go.Shape('RoundedRectangle', {
                          stroke: '#e8f1ff',
                          strokeWidth: 3
                        })
                          .theme('fill', 'primary'),
                        new go.Panel('Table', {
                          margin: 8,
                          stretch: go.Stretch.Fill
                        })
                          .addRowDefinition(0, { sizing: go.Sizing.None })
                          .add(
                            // the table header
                            new go.TextBlock({
                              row: 0,
                              alignment: go.Spot.Center,
                              margin: new go.Margin(0, 24, 0, 2), // leave room for Button
                              font: 'bold 18px sans-serif'
                            })
                              .bind('text', 'key')
                              .theme('stroke', 'text'),
                            // the collapse/expand button
                            go.GraphObject.build('PanelExpanderButton', {
                              row: 0,
                              alignment: go.Spot.TopRight
                            },'LIST') // the name of the element whose visibility this button toggles
                              .theme('ButtonIcon.stroke', 'text'),
                            new go.Panel('Table', {
                              name: 'LIST',
                              row: 1,
                              alignment: go.Spot.TopLeft
                            })
                              .add(
                                new go.TextBlock('Attributes', {
                                  row: 0,
                                  alignment: go.Spot.Left,
                                  margin: new go.Margin(3, 24, 3, 2),
                                  font: 'bold 15px sans-serif'
                                })
                                  .theme('stroke', 'text'),
                                go.GraphObject.build('PanelExpanderButton', {
                                  row: 0,
                                  alignment: go.Spot.Right
                                }, 'NonInherited')
                                  .theme('ButtonIcon.stroke', 'text'),
                                new go.Panel('Vertical', {
                                  row: 1,
                                  visible: false,
                                  name: 'NonInherited',
                                  alignment: go.Spot.TopLeft,
                                  defaultAlignment: go.Spot.Left,
                                  itemTemplate: itemTempl
                                })
                                  .bind('itemArray', 'items'),
                                new go.TextBlock('Inherited Attributes', {
                                  row: 2,
                                  visible: false,
                                  alignment: go.Spot.Left,
                                  margin: new go.Margin(3, 24, 3, 2), // leave room for Button
                                  font: 'bold 15px sans-serif'
                                })
                                  .bind('visible', 'inheritedItems', (arr) => Array.isArray(arr) && arr.length > 0)
                                  .theme('stroke', 'text'),
                                go.GraphObject.build('PanelExpanderButton', {
                                  row: 2,
                                  alignment: go.Spot.Right
                                }, 'Inherited')
                                  .bind('visible', 'inheritedItems', (arr) => Array.isArray(arr) && arr.length > 0)
                                  .theme('ButtonIcon.stroke', 'text'),
                                new go.Panel('Vertical', {
                                  row: 3,
                                  name: 'Inherited',
                                  alignment: go.Spot.TopLeft,
                                  defaultAlignment: go.Spot.Left,
                                  itemTemplate: itemTempl
                                })
                                  .bind('itemArray', 'inheritedItems')
                              )
                          )
                      );
                
                    // define the Link template, representing a relationship
                    myDiagram.linkTemplate = new go.Link({ // the whole link panel
                      selectionAdorned: true,
                      layerName: 'Background',
                      reshapable: true,
                      routing: go.Routing.AvoidsNodes,
                      corner: 5,
                      curve: go.Curve.JumpOver
                    })
                      .add(
                        new go.Shape({ // the link shape
                          stroke: '#f7f9fc',
                          strokeWidth: 3
                        })
                          .theme('stroke', 'link'),
                        new go.TextBlock({ // the "from" label
                          textAlign: 'center',
                          font: 'bold 14px sans-serif',
                          stroke: 'black',
                          segmentIndex: 0,
                          segmentOffset: new go.Point(NaN, NaN),
                          segmentOrientation: go.Orientation.Upright
                        })
                          .bind('text')
                          .theme('stroke', 'text'),
                        new go.TextBlock({ // the "to" label
                          textAlign: 'center',
                          font: 'bold 14px sans-serif',
                          stroke: 'black',
                          segmentIndex: -1,
                          segmentOffset: new go.Point(NaN, NaN),
                          segmentOrientation: go.Orientation.Upright
                        })
                          .bind('text', 'toText')
                          .theme('stroke', 'text')
                        );
                
                    // create the model for the E-R diagram
                
                    const nodeDataArray = ['''+nodeDataArray+'''];
                    
                    const linkDataArray = ['''+linkDataArray+'''];
                  
                    myDiagram.model = new go.GraphLinksModel({
                      copiesArrays: true,
                      copiesArrayObjects: true,
                      nodeDataArray: nodeDataArray,
                      linkDataArray: linkDataArray
                    });
                  }
                
                  const changeTheme = () => {
                    const myDiagram = go.Diagram.fromDiv('myDiagramDiv');
                    if (myDiagram) {
                      myDiagram.themeManager.currentTheme = document.getElementById('theme').value;
                    }
                  };
                
                  window.addEventListener('DOMContentLoaded', init);
                </script>
                
                <div id="sample">
                  <div id="myDiagramDiv" style="background-color: white; border: solid 1px black; width: 100%; height: 700px"></div>
                  Theme:
                  <select id="theme" onchange="changeTheme()">
                    <option value="system">System</option>
                    <option value="light">Light</option>
                    <option value="dark">Dark</option>
                  </select>
                </div>
                 </div>
                
                <h2 id="Columns">Columns</h2>
                <p>The following table contains a deep dive into the columns of the table that we have seen before at the diagram.</p>
                
                '''+colss_html.replace('\\n',' ')+'''
                
                <h2 id="Measures">Measures</h2>
                <p>Finally we have a detailed list of measures with descriptions and expressions.</p>
                
                '''+mea_html.replace('\\n',' ')+'''
                
                <p class="backlink"><a href="https://www.ladataweb.com.ar/contacto.html?id=suscribirse">Automatic Document developed by LaDataWeb</a></p>
                
                
                </body></html>
                '''
            print("Saving document...")
            if doc_type == 'file':
                with open(path, "w") as file:
                    file.write(html_doc)
                return "File saved."
            else:   
                return html_doc
        except Exception as ex:
            print("Error: ", ex, "\nThe is an error reading tables from the semantic model. Make sure you have checked the API limitations of the request at the description of the method." , "\nThere was an error generating the file. Please consider this is a preview feature. If you are not running a limitation, help us sending feedback on the specific dataset description you couldn't generate at https://www.ladataweb.com.ar/contacto.html")
            
    def create_doc_by_table_dataset_in_group(self, workspace_id, dataset_id, doc_type='text', path=None ):   
        """Create an html doc of a semantic model
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL                
        doc_type: str
            It can be file or string text
        path: str
            Path to store the html file like C:/Folder/SemanticModelDocument.html 
        ### Limitations
        ----
            API can't get info from Semantic models in direct lake and direct query.
            Service Principal can't query a semantic model with RLS by API
        ### Returns
        ----
        Returns a string of text of an html code to paste on a file or the literal file in the path specified
        """
        if 1==1:
            return "The request was limitated by Microsoft. Power Bi Rest API can't query INFO.DAX Functions for now. We are sorry about this."

        try:
            # Get Dataset details
            print("Getting Semantic Model Details...")
            dset = self.get_dataset_in_group(workspace_id, dataset_id)
            dsource = self.get_datasources_in_group(workspace_id, dataset_id)
            # Get Tables
            print("Getting Tables...")
            tabless = self.get_tables_from_dataset_in_group(workspace_id, dataset_id)
            df = utils.to_pandas(tabless['results'][0]['tables'][0], "rows")
            #tabless_html = pd.DataFrame.to_html(df).replace('class="dataframe"', 'class="styled-table"')
            # Get Columns
            print("Getting Columns...")
            colss = self.get_columns_from_dataset_in_group(workspace_id, dataset_id)
            df_col = utils.to_pandas(colss['results'][0]['tables'][0], "rows")
            df_col = df_col[~df_col["[ItemName]"].str.contains("RowNumber", na=False) ]
            df_cols_selected = df_col[["[Name]","[ItemType]", "[ItemName]","[DataType]", "[Expression]"]]
            # delete line colss_html = pd.DataFrame.to_html(df_col[["[Name]","[ItemType]", "[ItemName]","[DataType]", "[Expression]"]]).replace('class="dataframe"', 'class="styled-table"')            
            # Build tables dict for diagram
            print("Getting Relationships...")
            query='''
            DEFINE
                VAR _tablas_from = SELECTCOLUMNS(INFO.TABLES(), "FromTableID", [ID], "FromName", [Name])
                VAR _tablas_to = SELECTCOLUMNS(INFO.TABLES(), "ToTableID", [ID], "ToName", [Name])
                VAR _rels = SELECTCOLUMNS(INFO.RELATIONSHIPS(), "FromTableID", [FromTableID], "ToTableID", [ToTableID], "FromCardinality", [FromCardinality], "ToCardinality", [ToCardinality], "FromColumnID", [FromColumnID], "ToColumnID", [ToColumnID] )
                VAR _ready_rels1 = SELECTCOLUMNS(NATURALINNERJOIN(_rels, _tablas_from), "FromTableID", [FromTableID], "FromName", [FromName], "ToTableID", [ToTableID], "FromCardinality", [FromCardinality], "ToCardinality", [ToCardinality], "FromColumnID", [FromColumnID], "ToColumnID", [ToColumnID] )
                VAR _ready_rels2 = SELECTCOLUMNS(NATURALINNERJOIN(_ready_rels1, _tablas_to), "FromTableID", [FromTableID], "FromName", [FromName], "ToTableID", [ToTableID], "ToName", [ToName], "FromCardinality", [FromCardinality], "ToCardinality", [ToCardinality], "FromColumnID", [FromColumnID], "ToColumnID", [ToColumnID] )
            EVALUATE 
                _ready_rels2
            '''
            rel = self.execute_queries_in_group(workspace_id, dataset_id, query=query)
            df_rel = utils.to_pandas(rel['results'][0]['tables'][0], "rows")
            key_columns = list(set(df_rel["[FromColumnID]"].tolist() + df_rel["[ToColumnID]"].tolist()))
            # Get Partitions
            print("Getting Partitions...")
            querypq='''EVALUATE INFO.PARTITIONS()'''
            pq = self.execute_queries_in_group(workspace_id, dataset_id, query=querypq)
            df_pq = utils.to_pandas(pq['results'][0]['tables'][0], "rows")
            df_loop = pd.merge(df, df_pq, how='left', left_on="[ID]", right_on="[TableID]", suffixes=('', '_y'))[["[ID]","[Name]", "[IsHidden]" ,"[QueryDefinition]"]]                    
            print("Building Diagram...")
            # Generating a matrix for adjusting diagram positions
            allin = []
            dic = {}
            columnas=[]
            raiz = math.sqrt(len(df))
            x = int(raiz)
            y = int(raiz)
            if x*y < len(df):
                x=x+1
            else:
                pass
            x_count=0
            y_count=0
            
            for i, row in df.iterrows():
                if y_count == y:
                    x_count= x_count+1
                    y_count=0
                else:
                    y_count= y_count+1
                #print("i es ",str(i),"(", str(par*100) , ", " , str(impar*100) + ")")
                dic["key"] = row["[Name]"]
                dic["location"] = "new go.Point(" + str(x_count*400) + ", " + str(y_count*100) + ")"
                for j, wor in df_col[df_col['[Name]'] == row["[Name]"]].iterrows():
                    if wor["[ItemName]"]!=None:
                        #if "RowNumber" not in wor["[ItemName]"]:
                        if wor["[ItemID]"] in key_columns:
                            columnas.append({"name":wor["[ItemName]"], 'iskey': 'true', 'figure': 'Decision', 'color': 'purple'})                
                        else:
                            columnas.append({"name":wor["[ItemName]"], 'iskey': 'false', 'figure': 'Circle', 'color': 'blue'})            
                dic["items"]=columnas
                dic["inheritedItems"]=[]
                allin.append(dic)
                dic = {}
                columnas=[]
				
			# Clean Table
            nodeDataArray = ','.join(map(str,allin))
            nodeDataArray = nodeDataArray.replace("'key'","key")
            nodeDataArray = nodeDataArray.replace("'name'","name")
            nodeDataArray = nodeDataArray.replace("'new","new")
            nodeDataArray = nodeDataArray.replace("0)'","0)")
            nodeDataArray = nodeDataArray.replace("'item'","item")
            nodeDataArray = nodeDataArray.replace("'iskey'","iskey")
            nodeDataArray = nodeDataArray.replace("'figure'","figure")
            nodeDataArray = nodeDataArray.replace("'color'","color")
            nodeDataArray = nodeDataArray.replace("'true'","true")
            nodeDataArray = nodeDataArray.replace("'false'","false")
            # Build relationships dict for diagram                        
            relations = []
            for i, row in df_rel.iterrows():
                fromy = 1
                tomy = 1
                if row["[FromCardinality]"]== 2:
                    fromy="*"
                if row["[ToCardinality]"]== 2:
                    tomy="*"
                relations.append({ "from": row["[FromName]"], "to": row["[ToName]"], "text": fromy, "toText": tomy })
            # Clean Relationships
            linkDataArray = ','.join(map(str,relations))
            linkDataArray = linkDataArray.replace("'from'","from")
            linkDataArray = linkDataArray.replace("'to'","to")
            linkDataArray = linkDataArray.replace("'text'","text")
            linkDataArray = linkDataArray.replace("'toText'","toText")
            # Get Measures
            print("Getting Measures...")
            mea = self.get_measures_from_dataset_in_group(workspace_id, dataset_id)
            df_mea = utils.to_pandas(mea['results'][0]['tables'][0], "rows")[["[Name]","[ItemType]", "[ItemName]", "[Description]", "[DataType]", "[Expression]"]]
            #mea_html = pd.DataFrame.to_html(df_mea).replace('class="dataframe"', 'class="styled-table"')
            
            print("Creating document...")
            # Create Document Tables
            html_long=""
            list_tables=""
            for i, row in df_loop.iterrows():
                list_tables = list_tables + '<li><a href="#'+ row["[Name]"] +'">'+ row["[Name]"] +'</a></li>'
                html_long = html_long + '''
                <h3 id="'''+ row["[Name]"] +'''">Table '''+ row["[Name]"] +''' </h3>
                <p>The table has the hidden property equals to '''+ str(row["[IsHidden]"]) +''' and it is built with the following query definition</p>
                <div id="accordion">
                  <div class="card">
                    <div class="card-header" id="headingOne">
                      <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapse'''+ str(row["[ID]"]) +'''" aria-expanded="true" aria-controls="collapse'''+ str(row["[ID]"]) +'''">
                          Query Definition
                        </button>
                      </h5>
                    </div>
            
                    <div id="collapse'''+ str(row["[ID]"]) +'''" class="collapse" aria-labelledby="headingOne" data-parent="#accordion">
                      <div class="card-body">
                        <pre class="language-js"><code class="language-js">
'''+ row["[QueryDefinition]"]  +'''
                        </code></pre>  
                      </div>
                    </div>
                  </div>
                 </div>
                <br>
                <h4>Table schema definition</h4>
                '''+ pd.DataFrame.to_html(df_cols_selected[df_cols_selected["[Name]"]==row["[Name]"]]).replace('class="dataframe"', 'class="styled-table"').replace('\\n',' ')
                
                if len(df_mea[df_mea["[Name]"]==row["[Name]"]]) == 0:
                    html_long = html_long + "<br><p>This table doesn't contains measures.</p>"
                else:
                    html_long = html_long + '''<h4>Table measures </h4>
                    '''+ pd.DataFrame.to_html(df_mea[df_mea["[Name]"]==row["[Name]"]]).replace('class="dataframe"', 'class="styled-table"').replace('\\n',' ')
            
            # Create Document
            fina_html='''
                <html lang="en"><head>
                <title>Semantic Model Document with SimplePBI</title>
                <meta name="description" content="This document was autogenerated with SimplePBI, the python library for Power Bi Rest API developed by ibarrau." />
                <meta name="generator" content="http://www.ladataweb.com.ar/">
                <meta name="author" content="ibarrau">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
                <link rel="stylesheet" href="http://web.simmons.edu/~grovesd/comm244/css/notes.css" media="screen">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-3DEZ6EPPHR&amp;cx=c&amp;_slc=1"></script><script async="" src="https://www.google-analytics.com/analytics.js"></script><script src="http://web.simmons.edu/~grovesd/comm244/js/prism.js"></script><style type="text/css" id="operaUserStyle"></style>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                <script src="https://unpkg.com/gojs@3.0.10/release/go.js"></script>
                <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet" />
                <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
                <style>
                    .styled-table { 
                        margin: 25px 0;
                        border-collapse: collapse;
                        font-size: 0.9em;
                        font-family: sans-serif;
                        min-width: 400px;
                        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
                    }
                    .styled-table thead tr {
                        background-color: #F3A977;
                        color: #ffffff;
                        text-align: left;
                    }
                    .styled-table th,
                    .styled-table td {
                        padding: 12px 15px;
                    }
                    .styled-table tbody tr {
                        border-bottom: 1px solid #dddddd;
                    }
                
                    .styled-table tbody tr:nth-of-type(even) {
                        background-color: #f3f3f3;
                    }
                
                    .styled-table tbody tr:last-of-type {
                        border-bottom: 2px solid #F3A977;
                    }
                    .styled-table tbody tr.active-row {
                        font-weight: bold;
                        color: #009879;
                    }
                </style>
                </head>
                
                <body>
                <!-- Button on top like "back"> <p class="backlink"><a href="../../week3">Back to Week 3 page »</a></p> -->
                <br>
                <h1>Semantic Model '''+dset['name']+''' documentation</h1>
                <br>
                <p>The semantic model was configured by '''+ dset['configuredBy'] +'''. The target storage mode is '''+ dset['targetStorageMode'] +'''. Its refresh setting is set to '''+ str(dset['isRefreshable']) +'''. The configuration for RLS is '''+str(dset['isEffectiveIdentityRolesRequired'])+'''. It was created the date '''+dset['createdDate']+'''.</p>
                <p>The sources types involved are '''+', '.join([item['datasourceType'] for item in dsource['value']])+'''.
                <p>The document is built detailing table by table. For each table you will find its query definition, schema and measures.</p>
                <ul>
                    '''+list_tables+'''
                </ul>
                <h2 id="Diagram">Model Diagram</h2>
                
                <p>In addition you can see this data model interactive diagram. You can move tables, scroll or ctrl + wheel in order to adjust the view.</p>
                
                <div id="allSampleContent" class="p-4 w-full">
                          
                <script src="https://unpkg.com/create-gojs-kit@3.0.10/dist/extensions/Figures.js"></script>
                <script src="https://unpkg.com/create-gojs-kit@3.0.10/dist/extensions/Themes.js"></script>
                <script id="code">
                  function init() { 
                    myDiagram = new go.Diagram('myDiagramDiv', {
                      allowDelete: false,
                      allowCopy: false,
                      layout: new go.ForceDirectedLayout({ isInitial: false }),
                      'undoManager.isEnabled': true,
                      // use "Modern" themes from extensions/Themes
                      'themeManager.themeMap': new go.Map([
                        { key: 'light', value: Modern },
                        { key: 'dark', value: ModernDark }
                      ]),
                      'themeManager.changesDivBackground': true,
                      'themeManager.currentTheme': document.getElementById('theme').value
                    });
                
                    myDiagram.themeManager.set('light', {
                      colors: {
                        primary: '#f7f9fc',
                        green: '#62bd8e',
                        blue: '#3999bf',
                        purple: '#7f36b0',
                        red: '#c41000'
                      }
                    });
                    myDiagram.themeManager.set('dark', {
                      colors: {
                        primary: '#4a4a4a',
                        green: '#429e6f',
                        blue: '#3f9fc6',
                        purple: '#9951c9',
                        red: '#ff4d3d'
                      }
                    });
                
                    // the template for each attribute in a node's array of item data
                    const itemTempl = new go.Panel('Horizontal', { margin: new go.Margin(2, 0) })
                      .add(
                        new go.Shape({
                          desiredSize: new go.Size(15, 15),
                          strokeWidth: 0,
                          margin: new go.Margin(0, 5, 0, 0)
                        })
                          .bind('figure')
                          .themeData('fill', 'color'),
                        new go.TextBlock({
                          font: '14px sans-serif',
                          stroke: 'black'
                        })
                          .bind('text', 'name')
                          .bind('font', 'iskey', (k) => (k ? 'italic 14px sans-serif' : '14px sans-serif'))
                          .theme('stroke', 'text')
                      );
                
                    // define the Node template, representing an entity
                    myDiagram.nodeTemplate = new go.Node('Auto', { // the whole node panel
                      selectionAdorned: true,
                      resizable: true,
                      layoutConditions: go.LayoutConditions.Standard & ~go.LayoutConditions.NodeSized,
                      fromSpot: go.Spot.LeftRightSides,
                      toSpot: go.Spot.LeftRightSides
                    })
                      .bindTwoWay('location')
                      // whenever the PanelExpanderButton changes the visible property of the "LIST" panel,
                      // clear out any desiredSize set by the ResizingTool.
                      .bindObject('desiredSize', 'visible', (v) => new go.Size(NaN, NaN), undefined, 'LIST')
                      .add(
                        // define the node's outer shape, which will surround the Table
                        new go.Shape('RoundedRectangle', {
                          stroke: '#e8f1ff',
                          strokeWidth: 3
                        })
                          .theme('fill', 'primary'),
                        new go.Panel('Table', {
                          margin: 8,
                          stretch: go.Stretch.Fill
                        })
                          .addRowDefinition(0, { sizing: go.Sizing.None })
                          .add(
                            // the table header
                            new go.TextBlock({
                              row: 0,
                              alignment: go.Spot.Center,
                              margin: new go.Margin(0, 24, 0, 2), // leave room for Button
                              font: 'bold 18px sans-serif'
                            })
                              .bind('text', 'key')
                              .theme('stroke', 'text'),
                            // the collapse/expand button
                            go.GraphObject.build('PanelExpanderButton', {
                              row: 0,
                              alignment: go.Spot.TopRight
                            },'LIST') // the name of the element whose visibility this button toggles
                              .theme('ButtonIcon.stroke', 'text'),
                            new go.Panel('Table', {
                              name: 'LIST',
                              row: 1,
                              alignment: go.Spot.TopLeft
                            })
                              .add(
                                new go.TextBlock('Attributes', {
                                  row: 0,
                                  alignment: go.Spot.Left,
                                  margin: new go.Margin(3, 24, 3, 2),
                                  font: 'bold 15px sans-serif'
                                })
                                  .theme('stroke', 'text'),
                                go.GraphObject.build('PanelExpanderButton', {
                                  row: 0,
                                  alignment: go.Spot.Right
                                }, 'NonInherited')
                                  .theme('ButtonIcon.stroke', 'text'),
                                new go.Panel('Vertical', {
                                  row: 1,
                                  visible: false,
                                  name: 'NonInherited',
                                  alignment: go.Spot.TopLeft,
                                  defaultAlignment: go.Spot.Left,
                                  itemTemplate: itemTempl
                                })
                                  .bind('itemArray', 'items'),
                                new go.TextBlock('Inherited Attributes', {
                                  row: 2,
                                  visible: false,
                                  alignment: go.Spot.Left,
                                  margin: new go.Margin(3, 24, 3, 2), // leave room for Button
                                  font: 'bold 15px sans-serif'
                                })
                                  .bind('visible', 'inheritedItems', (arr) => Array.isArray(arr) && arr.length > 0)
                                  .theme('stroke', 'text'),
                                go.GraphObject.build('PanelExpanderButton', {
                                  row: 2,
                                  alignment: go.Spot.Right
                                }, 'Inherited')
                                  .bind('visible', 'inheritedItems', (arr) => Array.isArray(arr) && arr.length > 0)
                                  .theme('ButtonIcon.stroke', 'text'),
                                new go.Panel('Vertical', {
                                  row: 3,
                                  name: 'Inherited',
                                  alignment: go.Spot.TopLeft,
                                  defaultAlignment: go.Spot.Left,
                                  itemTemplate: itemTempl
                                })
                                  .bind('itemArray', 'inheritedItems')
                              )
                          )
                      );
                
                    // define the Link template, representing a relationship
                    myDiagram.linkTemplate = new go.Link({ // the whole link panel
                      selectionAdorned: true,
                      layerName: 'Background',
                      reshapable: true,
                      routing: go.Routing.AvoidsNodes,
                      corner: 5,
                      curve: go.Curve.JumpOver
                    })
                      .add(
                        new go.Shape({ // the link shape
                          stroke: '#f7f9fc',
                          strokeWidth: 3
                        })
                          .theme('stroke', 'link'),
                        new go.TextBlock({ // the "from" label
                          textAlign: 'center',
                          font: 'bold 14px sans-serif',
                          stroke: 'black',
                          segmentIndex: 0,
                          segmentOffset: new go.Point(NaN, NaN),
                          segmentOrientation: go.Orientation.Upright
                        })
                          .bind('text')
                          .theme('stroke', 'text'),
                        new go.TextBlock({ // the "to" label
                          textAlign: 'center',
                          font: 'bold 14px sans-serif',
                          stroke: 'black',
                          segmentIndex: -1,
                          segmentOffset: new go.Point(NaN, NaN),
                          segmentOrientation: go.Orientation.Upright
                        })
                          .bind('text', 'toText')
                          .theme('stroke', 'text')
                        );
                
                    // create the model for the E-R diagram
                
                    const nodeDataArray = ['''+nodeDataArray+'''];
                    
                    const linkDataArray = ['''+linkDataArray+'''];
                  
                    myDiagram.model = new go.GraphLinksModel({
                      copiesArrays: true,
                      copiesArrayObjects: true,
                      nodeDataArray: nodeDataArray,
                      linkDataArray: linkDataArray
                    });
                  }
                
                  const changeTheme = () => {
                    const myDiagram = go.Diagram.fromDiv('myDiagramDiv');
                    if (myDiagram) {
                      myDiagram.themeManager.currentTheme = document.getElementById('theme').value;
                    }
                  };
                
                  window.addEventListener('DOMContentLoaded', init);
                </script>
                
                <div id="sample">
                  <div id="myDiagramDiv" style="background-color: white; border: solid 1px black; width: 100%; height: 700px"></div>
                  Theme:
                  <select id="theme" onchange="changeTheme()">
                    <option value="system">System</option>
                    <option value="light">Light</option>
                    <option value="dark">Dark</option>
                  </select>
                </div>
                 </div>
                
                <h2 id="Tables">Tables</h2>
                <p>Here you can find the list of tables in the data model.</p>
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                
                '''+html_long+'''
                
                
                                
                <p class="backlink"><a href="https://www.ladataweb.com.ar/contacto.html?id=suscribirse">Automatic Document developed by LaDataWeb</a></p>
                
                
                </body></html>
                '''
            print("Saving document...")
            if doc_type == 'file':
                with open(path, "w") as file:
                    file.write(fina_html)
                return "File saved."
            else:   
                return fina_html
        except Exception as ex:            
            print("Error: ", ex, "\nThe is an error reading tables from the semantic model. Make sure you have checked the API limitations of the request at the description of the method." , "\nThere was an error generating the file. Please consider this is a preview feature. If you are not running a limitation, help us sending feedback on the specific dataset description you couldn't generate at https://www.ladataweb.com.ar/contacto.html")