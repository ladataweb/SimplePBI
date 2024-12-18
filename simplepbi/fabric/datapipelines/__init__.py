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
@........|____| |  | |...*   *.@    Copyright © 2024 Ignacio Barrau
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

class DataPipelines():
    """Simple library to use the  api and obtain data pipelines item from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric data pipelines item API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token

    # Get Data Pipeline in Workspace
    def get_data_pipeline(self, workspace_id, data_pipeline_id):
        """Returns properties of the specified data pipeline.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        data_pipeline_id: str uuid
            The data pipeline id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a data pipeline in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/dataPipelines/{}".format(workspace_id, data_pipeline_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # List Data Pipelines in Workspace
    def list_data_pipelines(self, workspace_id):
        """Returns a list of data pipelines in the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the data pipelines in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/dataPipelines".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Create Data Pipeline in Workspace
    def create_data_pipeline(self, workspace_id, displayName, description=None):
        """Creates a data pipeline in the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        displayName: str
            The data pipeline display name. The display name must follow naming rules according to item type.
        description: str
            The data pipeline description. Max length is 256 characters.
        ### Returns
        ----
        Response object from requests library. 201 or 202 OK
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/dataPipelines".format(workspace_id)
            body = {
                "displayName": displayName
            }
            if description != None:
                body["description"] = description
            headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data=json.dumps(body), headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Delete Data Pipeline in Workspace
    def delete_data_pipeline(self, workspace_id, data_pipeline_id):
        """Deletes the specified data pipeline from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        data_pipeline_id: str uuid
            The data pipeline id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/dataPipelines/{}".format(workspace_id, data_pipeline_id)
            headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
        
    # Update Data Pipeline in Workspace
    def update_data_pipeline(self, workspace_id, data_pipeline_id, displayName=None, description=None):
        """Updates the specified data pipeline in the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        data_pipeline_id: str uuid
            The data pipeline id. You can take it from PBI Service URL
        displayName: str
            The data pipeline display name. The display name must follow naming rules according to item type.
        description: str
            The data pipeline description. Max length is 256 characters.
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/dataPipelines/{}".format(workspace_id, data_pipeline_id)
            body = {}
            if displayName != None:
                body["displayName"] = displayName
            if description != None:
                body["description"] = description
            headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.patch(url, data=json.dumps(body), headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)