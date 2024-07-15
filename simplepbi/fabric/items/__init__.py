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

class Items():
    """Simple library to use the  api and obtain items from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric item API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token
            
    def get_item_in_group(self, workspace_id, item_id):
        """Returns the specified item from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        item_id: str uuid
            The item id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a item in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}".format(workspace_id, item_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                      
    def list_items(self, workspace_id):
        """Returns a list of items from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the items in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/items".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                       
    def delete_item_in_group(self, workspace_id, item_id):
        """Deletes the specified item from the specified workspace.
        ### Parameters
        ----
        item_id: str uuid
            The item id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}".format(workspace_id, item_id)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
       