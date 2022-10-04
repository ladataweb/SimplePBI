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
from simplepbi import utils
import pandas as pd

class Dashboards():
    """Simple library to use the Power BI api and obtain dashboards from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request admin API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
    
    def get_dashboard(self, dashboard_id):
        """Returns the specified dashboard from My workspace.
        ### Parameters
        ----
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a dashboard in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/dashboards/{}".format(dashboard_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_dashboard_in_group(self, workspace_id, dashboard_id):
        """Returns the specified dashboard from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a dashboard in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dashboards/{}".format(workspace_id, dashboard_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_dashboards(self):
        """Returns a list of dashboards from My workspace.
        ### Parameters
        ----
        None
        ### Returns
        ----
        Dict:
            A dictionary containing all the dashboards in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/dashboards"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_dashboards_in_group(self, workspace_id):
        """Returns a list of dashboards from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the dashboards in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dashboards".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def get_tile(self, dashboard_id, tile_id):
        """Returns the specified tile within the specified dashboard from My workspace.
        Supported tiles include datasets and live tiles that contain an entire report page.
        ### Parameters
        ----
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        tile_id: str uuid
            The tile id
        ### Returns
        ----
        Dict:
            A dictionary containing a tile in dashboard from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/dashboards/{}/tiles/{}".format(dashboard_id, tile_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_tile_in_group(self, workspace_id, dashboard_id, tile_id):
        """Returns the specified tile within the specified dashboard from the specified workspace.
        Supported tiles include datasets and live tiles that contain an entire report page.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        tile_id: str
            The tile id
        ### Returns
        ----
        Dict:
            A dictionary containing a tile in a dashboard from the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dashboards/{}/tiles/{}".format(workspace_id, dashboard_id, tile_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_tiles(self, dashboard_id):
        """Returns a list of tiles within the specified dashboard from My workspace.
        Supported tiles include datasets and live tiles that contain an entire report page.
        ### Parameters
        ----
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the tiles in a dashboard from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/dashboards/{}/tiles".format(dashboard_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_tiles_in_group(self, workspace_id, dashboard_id):
        """Returns a list of tiles within the specified dashboard from the specified workspace.
        Supported tiles include datasets and live tiles that contain an entire report page.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the tiles in a dashboard from a workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dashboards/{}/tiles".format(workspace_id, dashboard_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

           
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
            
    def clone_tile_in_dashboard_in_group(self, workspace_id, dashboard_id, tile_id, target_dashboard_id, target_dataset_id = None, target_report_id = None, target_workspace_id = None):
        """Clones the specified tile from the specified workspace.
        When a tile is cloned to another workspace and bound to another report and dataset, it's cloned as is with its underlying query containing the original report filters.
        If the target report ID and target dataset are missing, errors can occur.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL   
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
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/dashboards/{}/tiles/{}/Clone".format(workspace_id, dashboard_id, tile_id)
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

    def add_dashboard_in_group(self, workspace_id, workspace_name):
        """Creates a new empty dashboard in the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Request Body
        ----
        workspace_name: str 
            The name of the new dashboard
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/dashboards".format(workspace_id)
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
        