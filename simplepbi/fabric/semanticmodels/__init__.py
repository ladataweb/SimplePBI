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
@........|____| |  | |...*   *.@    Copyright © 2025 Ignacio Barrau
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

class SemanticModels():
    """Simple library to use the api and obtain semantic models item from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric semantic models item API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token

    # Get semantic model in Workspace
    def get_semantic_model(self, workspace_id, semantic_model_id):
        """Returns properties of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a semantic model in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/semanticModels/{}".format(workspace_id, semantic_model_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # List semantic models in Workspace
    def list_semantic_models(self, workspace_id):
        """Returns a list of semantic models in the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the semantic models in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/semanticModels".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Delete semantic model in Workspace
    def delete_semantic_model(self, workspace_id, semantic_model_id):
        """Deletes the specified semantic model from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/semanticModels/{}".format(workspace_id, semantic_model_id)
            headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
    # Create semantic model in Workspace
    
    