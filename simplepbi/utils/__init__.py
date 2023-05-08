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
import pandas as pd

'''
class Utils():
    """Simple library class."""
    
    def __init__(self):
        """Class with useful methods."""
    '''
    
def append_value(dict_obj, key, value):
    '''
    Parameters
    ----------
    dict_obj : dict
        dictionary object to append values.
    key : str
        Key name of the dictonary that will append a value.
    value : any
        Value to append in the key of the dictionary.

    Returns
    -------
    None. It is applied to the dict in the parameter
    '''
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
            # Append the value in list
            dict_obj[key].append(value)
        else:
            # As key is not in dict,
            # so, add key-value pair
            dict_obj[key] = value
    
def to_pandas(response_dict, father_node):
    '''
    Parameters
    ----------
    response_dict : dict
        response from methods.
    father_node : TYPE
        Dict Key involving the list [] of items. Example for get_dashboards, the key of the response is "value"
        {
          "value": [
            {
              "id": "69ffaa6c-b36d-4d01-96f5-1ed67c64d4af",
              "displayName": "SalesMarketing",
              "embedUrl": "https://app.powerbi.com/dashboardEmbed?dashboardId=69ffaa6c-b36d-4d01-96f5-1ed67c64d4af&groupId=f089354e-8366-4e18-aea3-4cb4a3a50b48",
              "isReadOnly": false
            }
          ]
        }

    Returns
    -------
    df : Pandas DataFrame
        Returns the dict response converted in a Pandas DataFrame.
    '''
    js = json.dumps(response_dict[father_node])
    df = pd.read_json(js)
    return df 

def get_artifact_from_scan_preview(scan_result, artifact):
    """Get a table of an specific artifact
    ### Parameters
    ----
    scan_result: dict
        The scan result response from get_scan_result_preview
    artifact: str
        The type of artifact. Types: 'reports', 'dashboards', 'datasets', 'dataflows', 'users'
    ### Returns
    ----
    str:
        Returns the status of the scan. Succeeded means you are ready to request scans.
    """
    df_total = pd.DataFrame()
    try:        
        for group in scan_result["workspaces"]:
            df = pd.read_json(json.dumps(group[artifact]))
            df["workspaceId"] = group["id"]
            df_total = pd.concat([df_total, df], sort=True, ignore_index=True)
        return df_total
    except Exception as e:
        print("ERROR: ", e)