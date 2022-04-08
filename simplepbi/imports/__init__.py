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
from simplepbi import utils
import pandas as pd

class Imports():
    """Simple library to use the Power BI api and obtain imports from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request imports API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
    
    def get_import(self, import_id):
        """Returns the specified import from My workspace.
        ### Parameters
        ----
        import_id: str uuid
            The Power Bi import id. 
        ### Returns
        ----
        Dict:
            A dictionary containing a import in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/imports/{}".format(import_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_import_in_group(self, workspace_id, import_id):
        """Returns the specified import from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        import_id: str uuid
            The Power Bi import id.
        ### Returns
        ----
        Dict:
            A dictionary containing a import in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/imports/{}".format(workspace_id, import_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_imports(self):
        """Returns a list of imports from My workspace.
        ### Parameters
        ----
        None
        ### Returns
        ----
        Dict:
            A dictionary containing all the imports in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/imports"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_imports_in_group(self, workspace_id):
        """Returns a list of imports from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the imports in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/imports".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)



'''
Import files requests here

    def clone_tile_in_dashboard(self, dashboard_id, tile_id, target_dashboard_id, target_dataset_id = None, target_report_id = None, target_workspace_id = None):
        """Clones the specified tile from My workspace.
        When a tile is cloned to another workspace and bound to another report and dataset, it's cloned as is with its underlying query containing the original report filters.
        If the target report ID and target dataset are missing, errors can occur.
        ### Parameters
        ----
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        tile_id: str
            The tile id
        ### Request Body
        ----
        target_dashboard_id: str
            The target dashboard ID
        target_dataset_id: str uuid
            (Optional) A parameter for specifying a target model ID. When cloning a tile linked to a dataset, pass the target model ID to rebind the new tile to a different dataset.
        target_report_id: str uuid
            (Optional) A parameter for specifying a target report ID. When cloning a tile linked to a report, pass the target report ID to rebind the new tile to a different report.
        target_workspace_id: str uuid
            (Optional) A parameter for specifying a target workspace ID. An empty GUID (00000000-0000-0000-0000-000000000000) indicates 'My Workspace'. If this parameter isn't provided, the tile will be cloned within the same workspace as the source tile.
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/dashboards/{}/tiles/{}/Clone".format(dashboard_id, tile_id)
            body = {
                "targetDashboardId": target_dashboard_id
            }
            if target_report_id != None:
                body["targetReportId"]=target_report_id
            if target_dataset_id != None:
                body["targetModelId"]=target_dataset_id
            if target_workspace_id != None:
                body["targetWorkspaceId"] = target_workspace_id
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
 
            
    def add_dashboard(self, workspace_name):
        """Creates a new empty dashboard in My workspace.
        ### Parameters
        ----
        None
        ### Request Body
        ----
        workspace_name: str 
            The name of the new dashboard
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/dashboards"
            body = {
                "name": workspace_name
            }
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

'''