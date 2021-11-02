import json
import requests
#from simplepbi import utils
#from datetime import date, timedelta
#import pandas as pd

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
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a dataset in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}".format(dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_dataset_in_group(self, workspace_id, dataset_id):
        """Returns the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a dataset in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}".format(workspace_id, dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
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
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_datasets_in_group(self, workspace_id):
        """Returns a list of datasets from the specified workspace.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasets in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets".format(workspace_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)

    def get_datasources(self, dataset_id):
        """Returns a list of data sources for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the dataset from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/datasources".format(dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_datasources_in_group(self, workspace_id, dataset_id):
        """Returns a list of data sources for the specified dataset from the specified workspace
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the dataset from the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/datasources".format(workspace_id, dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_dataset_to_dataflows_links_in_group(self, workspace_id):
        """Returns a list of upstream dataflows for datasets from the specified workspace.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all upstream dataflows in the dataset from a workspace
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/upstreamDataflows".format(workspace_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)

    def get_direct_query_refresh_schedule(self, dataset_id):
        """Returns the refresh schedule for a specified DirectQuery or LiveConnection dataset from My workspace.
        ### Parameters
        ----
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing the direct query refresh schedule in a dataset from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/directQueryRefreshSchedule".format(dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_direct_query_refresh_schedule_in_group(self, workspace_id, dataset_id):
        """Returns the refresh schedule for a specified DirectQuery or LiveConnection dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing the direct query refresh schedule in a dataset from a workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/directQueryRefreshSchedule".format(workspace_id, dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_gateway_datasources(self, dataset_id):
        """This API is deprecated, use Get Datasources instead.
        ### Parameters
        ----
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        """
        print("This API is deprecated, use Get Datasources instead.")
    def get_gateway_datasources_in_group(self, dataset_id):
        """This API is deprecated, use Get Datasources In Group instead.
        ### Parameters
        ----
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        """
        print("This API is deprecated, use Get Datasources In Group instead.")
        
    def get_parameters(self, dataset_id):
        """Returns a list of parameters for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the parameters in the dataset from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/parameters".format(dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_parameters_in_group(self, workspace_id, dataset_id):
        """Returns a list of parameters for the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the parameters in the dataset from workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/parameters".format(workspace_id, dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
    
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
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_refresh_history_in_group(self, workspace_id, dataset_id, top=None):
        """Returns the refresh history for the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id:
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
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_refresh_schedule(self, dataset_id):
        """Returns the refresh schedule for the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a refresh schedule in a dataset from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/refreshSchedule".format(dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_refresh_schedule_in_group(self, workspace_id, dataset_id):
        """Returns the refresh schedule for the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a refresh schedule in a dataset from workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/refreshSchedule".format(workspace_id, dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def refresh_dataset(self, dataset_id, notifyOption):
        """Triggers a refresh for the specified dataset from My workspace.
        For Shared capacities, a maximum of eight requests per day, which includes refreshes executed using a scheduled refresh.
        ### Parameters
        ----    
        dataset_id:
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
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def refresh_dataset_in_group(self, workspace_id, dataset_id, notifyOption):
        """Triggers a refresh for the specified dataset from the specified workspace.
        For Shared capacities, a maximum of eight requests per day, which includes refreshes executed using a scheduled refresh.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id:
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
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def take_over_dataset_in_group(self, workspace_id, dataset_id):
        """Transfers ownership over the specified dataset to the current authorized user.
        ### Parameters
        ----
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataset_id:
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
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def discover_gateways(self, dataset_id):
        """Returns a list of gateways that the specified dataset from My workspace can be bound to.
        This API call is only relevant to datasets that have at least one on-premises connection. For datasets with cloud-only connections, this API call returns an empty list.
        ### Parameters
        ----
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a list of gateways from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/Default.DiscoverGateways".format(dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def discover_gateways_in_group(self, workspace_id, dataset_id):
        """Returns a list of gateways that the specified dataset from the specified workspace can be bound to.
        This API call is only relevant to datasets that have at least one on-premises connection. For datasets with cloud-only connections, this API call returns an empty list.
        ### Parameters
        ----
        workspace_id:
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
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)