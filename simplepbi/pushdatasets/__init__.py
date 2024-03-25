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

class PushDatasets():
    """Simple library to use the Power BI api and obtain datasets from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request admin API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
    
    def get_dataset_tables(self, dataset_id):
        """Returns a list of tables within the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing tables from a dataset in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/datasets/{}/tables".format(dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_dataset_tables_in_group(self, workspace_id, dataset_id):
        """Returns a list of tables within the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing tables from a dataset in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/tables".format(workspace_id, dataset_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
      
    def delete_dataset_tablerows(self, dataset_id, table_name):
        """Deletes all rows from the specified table within the specified dataset from My workspace.
        ### Parameters
        ----
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        table_name: str
            The table name
        ### Returns
        ----
        Response object from requests library. 201 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/tables/{}/rows".format(dataset_id, table_name)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def delete_dataset_tablerows_in_group(self, workspace_id, dataset_id, table_name):
        """Deletes all rows from the specified table within the specified dataset from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi Workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        table_name: str
            The table name
        ### Returns
        ----
        Response object from requests library. 201 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/tables/{}/rows".format(workspace_id, dataset_id, table_name)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
 
            
    def post_dataset_preview(self, DefaultRetentionPolicy, name, tables, relationships=None):
        """Creates a new Streaming Dataset on My workspace. It's only for push datasets
        ### Parameters
        ----    
        DefaultRetentionPolicy: str
            The default retention policy. It can be basicFIFO or None
        ### Request Body
        ----
        name: str
            The dataset name
        tables: list dict
            The dataset tables. Example
            [{
              "name": "Product",
              "columns": [
                {
                  "name": "ProductID",
                  "dataType": "Int64"
                },
                {
                  "name": "Name",
                  "dataType": "string"
                }
                ]
             }]
        defaultMode: str
            The dataset mode or type. It is forced as PushStreaming only for now.
        relationshops:
            The dataset relationships. Please read the docs before using this parameter
        ### Returns
        ----
        Response object from requests library. 201 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets?defaultRetentionPolicy={}".format(DefaultRetentionPolicy)
            body = {
                "name": name,
                "tables": tables,
                "defaultMode": "PushStreaming"
            }
            if relationships != None:
                body["relationships"]=relationships
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def post_dataset_in_group_preview(self, DefaultRetentionPolicy, workspace_id, name, tables, relationships=None):
        """Creates a new Streaming Dataset in the specified workspace. It's only for Push datasets
        ### Parameters
        ----    
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL 
        DefaultRetentionPolicy: str
            The default retention policy. It can be basicFIFO or None
        ### Request Body
        ----
        name: str
            The dataset name
        tables: list dict
            The dataset tables. Example
            [{
              "name": "Product",
              "columns": [
                {
                  "name": "ProductID",
                  "dataType": "Int64"
                },
                {
                  "name": "Name",
                  "dataType": "string"
                }
                ]
             }]
        defaultMode: str
            The dataset mode or type. It is forced as PushStreaming only for now.
        relationshops:
            The dataset relationships. Please read the docs before using this parameter
        ### Returns
        ----
        Response object from requests library. 201 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets?defaultRetentionPolicy={}".format(workspace_id, DefaultRetentionPolicy)
            body = {
                "name": name,
                "tables": tables,
                "defaultMode": "PushStreaming"
            }
            if relationships != None:
                body["relationships"]=relationships
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def post_rows_table_dataset(self, dataset_id, table_name, rows):
        """Adds new data rows to the specified table within the specified dataset from My workspace.
        This API call only supports push datasets.
        ### Parameters
        ----    
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        table_name: str
            The table name
        ### Request Body
        ----
        rows: object[]
            An array of data rows pushed to a dataset table. Each element is a collection of properties represented using key-value format. Example:
            [{
              "ProductID": 1,
              "Name": "Adjustable Race",
              "Category": "Components",
              "IsCompete": true,
              "ManufacturedOn": "07/30/2014"
            },
            {
              "ProductID": 2,
              "Name": "LL Crankarm",
              "Category": "Components",
              "IsCompete": true,
              "ManufacturedOn": "07/30/2014"
            }
            }]        
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/tables/{}/rows".format(dataset_id, table_name)
            body = {
                "rows": rows
            }
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def post_rows_table_dataset_in_group(self, workspace_id, dataset_id, table_name, rows):
        """Adds new data rows to the specified table within the specified dataset from the specified workspace.
        This API call only supports push datasets.
        ### Parameters
        ----    
        workspace_id: str uuid
            The Power Bi Workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        table_name: str
            The table name
        ### Request Body
        ----
        rows: object[]
            An array of data rows pushed to a dataset table. Each element is a collection of properties represented using key-value format. Example:
            [{
              "ProductID": 1,
              "Name": "Adjustable Race",
              "Category": "Components",
              "IsCompete": true,
              "ManufacturedOn": "07/30/2014"
            },
            {
              "ProductID": 2,
              "Name": "LL Crankarm",
              "Category": "Components",
              "IsCompete": true,
              "ManufacturedOn": "07/30/2014"
            }
            }] 
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/tables/{}/rows".format(workspace_id, dataset_id, table_name)
            body = {
                "rows": rows
            }
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def put_table_preview(self, dataset_id, table_name, columns, description, isHidden, measures=None, rows=None, source=None):
        """Updates the metadata and schema for the specified table within the specified dataset from My workspace.
        This request is in PREVIEW. It doesn't have measures, rows and sources parameters available'
        This API call only supports push datasets.
        ### Parameters
        ----    
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        table_name: str
            The table name
        ### Request Body
        ----
        description: str
            The table description
        isHidden: bool
            Optional. Whether this dataset table is hidden
        name: str
            The table name
        columns: list dict
            	The column schema for this table
            The dataset tables. Example            
              "columns": [
                {
                  "name": "ProductID",
                  "dataType": "Int64"
                },
                {
                  "name": "Name",
                  "dataType": "string"
                }
                ]            
        ### Returns
        ----
        Response object from requests library. 201 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/datasets/{}/tables/{}".format(dataset_id, table_name)
            body = {
                "name": table_name,
                "description": description,
                "isHidden": isHidden,
                "columns": columns
            }                
            '''
            if measures != None:
                body["measures"]=measures
            if rows != None:
                body["rows"]=rows
            if source != None:
                body["source"]=source
            '''
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.put(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def put_table_in_group_preview(self, workspace_id, dataset_id, table_name, columns, description, isHidden, measures=None, rows=None, source=None):
        """Updates the metadata and schema for the specified table within the specified dataset from the specified workspace.
        This request is in PREVIEW. It doesn't have measures, rows and sources parameters available'
        This API call only supports push datasets.
        ### Parameters
        ----    
        workspace_id: str uuid
            The Power Bi Workspace id. You can take it from PBI Service URL
        dataset_id: str uuid
            The Power Bi Dataset id. You can take it from PBI Service URL
        table_name: str
            The table name
        ### Request Body
        ----
        tables: list dict
            The dataset tables. Example
            [{
              "name": "Product",
              "columns": [
                {
                  "name": "ProductID",
                  "dataType": "Int64"
                },
                {
                  "name": "Name",
                  "dataType": "string"
                }
                ]
             }]
        ### Returns
        ----
        Response object from requests library. 201 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/datasets/{}/tables/{}".format(workspace_id, dataset_id, table_name)
            body = {
                "name": table_name ,
                "description": description,
                "isHidden": isHidden,
                "columns": columns
            }                
            '''
            if measures != None:
                body["measures"]=measures
            if rows != None:
                body["rows"]=rows
            if source != None:
                body["source"]=source
            '''
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.put(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)