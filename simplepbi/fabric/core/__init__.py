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
import os
import base64

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
            
    def get_item(self, workspace_id, item_id):
        """Returns the specified item from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        ### Returns
        ----
        Dict:
            A dictionary containing a item in the workspace.
        ### Limitations
        ----
        This API is supported for a number of item types, find the supported item types here.
        https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/item-management-overview
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
            The workspace id. You can take it from Fabric URL
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
                       
    def delete_item(self, workspace_id, item_id):
        """Deletes the specified item from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
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
            
    def create_item(self, workspace_id, displayName, itemType, description=None, parts=None):
        """Creates an item in the specified workspace. Preview request, soon we'll add 'definition' parameter
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        displayName: str
            The item display name. The display name must follow naming rules according to item type.
        itemType: str
            The item type. Example: Dashboard, DataPipeline, Datamart, Eventstream, KQLDataConnection, KQLDatabase, KQLQueryset, Lakehouse, MLExperiment, MLModel, MountedWarehouse, Notebook, PaginatedReport, Report, SQLEndpoint, SemanticModel, SparkJobDefinition
        description: str
            The item description. Max length is 256 characters.
        ### Returns
        ----
        Response object from requests library. 201 or 202 OK
        ### Limitations
        ----
        To create a non-PowerBI Fabric item the workspace must be on a supported Fabric capacity type. For more information see Microsoft Fabric license types.
To create a PowerBI item, the user must have the appropritate license. For more information see Microsoft Fabric license types.
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items".format(workspace_id)
            body = {
                "displayName": displayName,
                "type": itemType
            }
            if description != None:
                body["description"]=description
            if parts != None:
                body["definition"]={ "Parts": parts }
            headers={'Content-Type': 'application/json; charset=utf-8', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            if res.status_code==202:
                print("Request accepted, item provisioning in progress. Please wait. Operation id: ", res.headers['x-ms-operation-id'])
                # Get operation state
                LongRunningOperations(self.token).get_operation_state(res.headers['x-ms-operation-id'])                
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_item_definition(self, workspace_id, item_id):
        """Returns the specified item definition.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL        
        ### Returns
        ----
        Response object from requests library. 200 OK        
        ### Limitations
        ----
        This API is blocked for an item with an encrypted sensitivity label.
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{workspaceId}/items/{}/getDefinition".format(workspace_id, item_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_item(self, workspace_id, item_id, displayName=None, description=None):
        """Updates the properties of the specified item.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        displayName: str
            The item display name. The display name must follow naming rules according to item type.
        description: str
            The item description. Max length is 256 characters.
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}".format(workspace_id, item_id)
            body = {}
            if displayName != None:
                body["displayName"]=displayName
            if description != None:
                body["description"]=description
            if body == {}:
                raise Exception("Please specify a display name or description to update item.")
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.patch(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_item_definition(self, workspace_id, item_id, parts, format=None):
        """Overrides the definition for the specified item.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        parts: ItemDefinitionPart[]
            A list of definition parts. part, payload and payloadtype description. Read API Docs for more details.
        format: str 
            	The format of the item definition.
        
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/updateDefinition".format(workspace_id, item_id)
            body = {
                "definition": {
                    "Parts": parts
                }
            }
            if format != None:
                body["format"]=format
            headers={'Content-Type': 'application/json; charset=utf-8', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()            
            if res.status_code==202:
                print("Request accepted, item provisioning in progress. Please wait. Operation id: ", res.headers['x-ms-operation-id'])
                # Get operation state
                LongRunningOperations(self.token).get_operation_state(res.headers['x-ms-operation-id'])                
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def simple_deploy_semantic_model(self, workspace_id, item_path):
        """Deploys the semantic model for the specified item.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_path: str 
            The semantic model path until [name].SemanticModel folder like C:/Users/user/Desktop/[name].SemanticModel
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        parts = []

        item_name = item_path.split("/")[-1].split(".")[0]
        if item_name == "":
            raise Exception("Make sure the path doesn't en in / or \\ at the end.")
        else:
            print("Item name: ", item_name)

        # Iterate through the files in the item_path
        for root, dirs, files in os.walk(item_path):
            if os.path.basename(root) == ".pbi":
                continue
            for file in files:
                # Skip files with the name "item.*.json"
                if file.startswith("item.") and file.endswith(".json"):
                    continue
                if file == "cache.abf":
                    continue

                # Get the file path relative to the project folder
                file_path = os.path.relpath(os.path.join(root, file), item_path).replace("\\","/")

                # Read the file contents
                with open(os.path.join(root, file), "rb") as f:
                    file_contents = f.read()

                # Base64-encode the file contents
                encoded_contents = base64.b64encode(file_contents).decode("utf-8")

                # Add the file to the Parts array
                parts.append({
                    "Path": file_path,
                    "Payload": encoded_contents,
                    "PayloadType": "InlineBase64"
                })

        try:
            # Get list of items
            it = self.list_items(workspace_id)
            id = [i['id'] for i in it['value'] if i['displayName']==item_name and i['type']=="SemanticModel" ]
            if id == []:
                # Create item
                res = self.create_item(workspace_id, item_name, "SemanticModel", None, parts)
            else:
                # Update item definition
                print("Updating semantic model id {} in workspace id {}".format(id[0], workspace_id))
                res = self.update_item_definition(workspace_id, id[0], parts)            
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def simple_deploy_report(self, report_workspace_id, semantic_model_workspace_id, item_path):
        """Deploys the semantic model for the specified item.
        #### Parameters
        ----
        report_workspace_id: str uuid
            The workspace id of the destination of the report deployment. You can take it from Fabric URL
        item_path: str 
            The semantic model path until [name].Report folder like C:/Users/user/Desktop/[name].Report
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        parts = []

        item_name = item_path.split("/")[-1].split(".")[0]
        if item_name == "":
            raise Exception("Make sure the path doesn't en in / or \\ at the end.")
        else:
            print("Item name: ", item_name)

        # Iterate through the files in the item_path
        for root, dirs, files in os.walk(item_path):
            # Skip folders with the name ".pbi"
            if os.path.basename(root) == ".pbi":
                continue

            for file in files:
                # Skip files with the name "item.*.json"
                if file.startswith("item.") and file.endswith(".json"):
                    continue
                if file == "cache.abf":
                    continue
                if file.endswith(".pbir"):
                    # Load the JSON file
                    with open(item_path +'/definition.pbir', 'r') as f:
                        pbir_json = json.load(f)
                        
                    # Remove the "byPath" item
                    semantic_model_name = pbir_json['datasetReference']['byPath']['path'].split("/")[-1].split(".")[0]                    
                    print("Looking for id of semantic model {} in workspace id {} related to the report".format(semantic_model_name, semantic_model_workspace_id))
                    try:
                        it = self.list_items(semantic_model_workspace_id)
                        semantic_model_id = [i['id'] for i in it['value'] if i['displayName']==semantic_model_name and i['type']=="SemanticModel" ]
                        if semantic_model_id == []:
                            raise Exception("Semantic Model {} does not exist in the specified workspace.".format(semantic_model_name))
                    except Exception as e:
                        print("Error: ", e)
                        
                    del pbir_json['datasetReference']['byPath']
                    
                    # Add a new JSON object to the "byConnection" property
                    pbir_json['datasetReference']['byConnection'] = {
                        "connectionString": None,
                        "pbiServiceModelId": None,
                        "pbiModelVirtualServerName": "sobe_wowvirtualserver",
                        "pbiModelDatabaseName": semantic_model_id[0],
                        "name": "EntityDataSource",
                        "connectionType": "pbiServiceXmlaStyleLive"
                    }
                    # Convert the PBIR JSON object to a string
                    pbir_json_str = json.dumps(pbir_json)
                    
                    # Convert the string to UTF-8 bytes
                    file_contents = pbir_json_str.encode('utf-8')
                else:            
                    # Read the file contents
                    with open(os.path.join(root, file), "rb") as f:
                        file_contents = f.read()
                
                # Get the file path relative to the project folder
                file_path = os.path.relpath(os.path.join(root, file), item_path).replace("\\","/")
            
                # Base64-encode the file contents
                encoded_contents = base64.b64encode(file_contents).decode("utf-8")

                # Add the file to the Parts array
                parts.append({
                    "Path": file_path,
                    "Payload": encoded_contents,
                    "PayloadType": "InlineBase64"
                })

        try:
            # Get list of items
            it = self.list_items(report_workspace_id)
            id = [i['id'] for i in it['value'] if i['displayName']==item_name and i['type']=="Report" ]
            if id == []:
                # Create item
                res = self.create_item(report_workspace_id, item_name, "Report", None, parts)
            else:
                # Update item definition
                print("Updating report id {} in workspace id {}".format(id[0], report_workspace_id))
                res = self.update_item_definition(report_workspace_id, id[0], parts)            
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                
       
class Git():
    """Simple library to use the  api and obtain items from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric item API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token
            
    def get_git_connection(self, workspace_id):
        """Returns git connection details for the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        ### Returns
        ----
        Dict:
            A dictionary containing a item in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/git/connection".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_git_status(self, workspace_id):
        """Returns the Git status of items in the workspace, that can be committed to Git.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        ### Returns
        ----
        Dict:
            A dictionary containing a item in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/git/status".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def commit_to_git(self, workspace_id, mode, comment, workspaceHead, items=None):
        """Commits the changes made in the workspace to the connected remote branch.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        mode: string
            The mode for the commit operation.
        comment: string
            	Caller-free comment for this commit. Maximum length is 300 characters. If no comment is provided by the caller, use the default Git provider comment.
        workspaceHead: str 
            	Full SHA hash that the workspace is synced to. The hash can be retrieved from the Git Status API.
        items: itemsIdentifier[]
            Specific items to commit. This is relevant only for Selective commit mode. The items can be retrieved from the Git Status API.
            Each item it's { "logicalId": str uuid, "objectId": str uud }. You can use one of them or both if you have them.
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/git/commitToGit".format(workspace_id)
            body = {
                "mode": mode,
                "workspaceHead": workspaceHead,
                "comment": comment
            }
            if items != None:
                body["items"]=items
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_from_git(self, workspace_id, item_id, remoteCommitHash, conflictResolution, allowOverrideItems, workspaceHead):
        """Updates the workspace with commits pushed to the connected branch.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        remoteCommitHash: string
            	Remote full SHA commit hash.
        conflictResolution: string
            	Conflict resolution to be used in the update from Git operation. If items are in conflict and a conflict resolution is not specified, the update operation will not start. Example:
            {"ConflictResolutionPolicy": PreferRemote or PreferWorkspace, "ConflictResolutionType": "Workspace"}
        options: options
            Automatically written by simplepbi. Options to be used in the update from Git operation. For now just overrideitems
        allowOverrideItems: bool
            User consent to override incoming items during the update from Git process. When incoming items are present and the allow override items is not specified or is provided as false, the update operation will not start. Default value is false.
        workspace_head: str 
            	Full SHA hash that the workspace is synced to. The hash can be retrieved from the Git Status API.
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/git/updateFromGit".format(workspace_id, item_id)
            body = {
                "workspaceHead": workspaceHead,
                "remoteCommitHash": remoteCommitHash,
                "conflictResolution": conflictResolution,
                "options":{
                    "allowOverrideItems": allowOverrideItems
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

    # Connect to git repo
    def connect_git_repo(self, workspace_id, organization, project, repository, branch, directory_name, git_provider_type):
        """Connects the workspace to an Azure DevOps repository.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        organization: string
            The Azure DevOps organization name.
        project: string
            The Azure DevOps project name.
        repository: string
            The Azure DevOps repository name.
        branch: string
            The Azure DevOps branch name.
        directory_name: string
            The Azure DevOps directory name.
        git_provider_type: string
            The Git provider type. Example: AzureDevOps
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/git/connect".format(workspace_id)
            body = {
                "gitProviderDetails": {
                    "organization": organization,
                    "project": project,
                    "repository": repository,
                    "branch": branch,
                    "directoryName": directory_name,
                    "gitProviderType": git_provider_type
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

    # Disconnect from git repo
    def disconnect_git_repo(self, workspace_id):
        """Disconnects the workspace from an Azure DevOps repository.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/git/disconnect".format(workspace_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                    
            
class Scheduler():

    """Simple library to use the api and obtain job scheduler from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric job scheduler API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token
        
    def run_on_demand_item_job(self, workspace_id, item_id, jobType):
        """Run on-demand item job instance.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        jobType: string
            The job type, for now just "DefaultJob"
        executionData: str 
            	Execution data for the job. Preview parameter, a working progress from the API      
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/jobs/instances?jobType={}".format(workspace_id, item_id, jobType)
            body = {
                "executionData": {}
            }
            if format != None:
                body["format"]=format
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Get Item Job Instance
    def get_item_job_instance(self, workspace_id, item_id, job_instance_id):
        """Returns the specified job instance for the specified item.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        job_instance_id: str uuid
            The job instance id.
        ### Returns
        ----
        Dict:
            A dictionary containing a job instance in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/jobs/instances/{}".format(workspace_id, item_id, job_instance_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Cancel Item Job Instance
    def cancel_item_job_instance(self, workspace_id, item_id, job_instance_id):
        """Cancels the specified job instance for the specified item.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        job_instance_id: str uuid
            The job instance id.
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/jobs/instances/{}".format(workspace_id, item_id, job_instance_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
class Workspaces():
    """Simple library to use the api and obtain workspaces from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric core workspaces API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token

    # Add Workspace Role Assignment
    def add_workspace_role_assignment(self, workspace_id, principal_id, principal_type, role):
        """Adds a role assignment to the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        principal_id: str uuid
            The principal id.
        principal_type: string
            The principal type. { "User", "Group", "ServicePrincipal", "ServicePrincipalProfile" }
        role: string
            The role. Workspace role, like { "Member", "Admin", "Contributor", "Viewer"}
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/roleAssignments".format(workspace_id)
            body = {
                "principal": {
                    "id": principal_id,
                    "type": principal_type,
                },
                "role": role
            }
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Assign Workspace to Capacity
    def assign_workspace_to_capacity(self, workspace_id, capacity_id):
        """Assigns the specified workspace to the specified capacity.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        capacity_id: str uuid
            The capacity id.
        ### Returns
        ----
        Response object from requests library. 202 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/assignToCapacity".format(workspace_id)
            body = {
                "capacityId": capacity_id
            }
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Create Workspace
    def create_workspace(self, displayName, capacity_id=None, description=None):
        """Creates a workspace.
        #### Parameters
        ----
        displayName: string
            The workspace display name. The display name must follow naming rules according to item type.
        capacity_id: str uuid
            The capacity id.
        description: string
            The workspace description. Max length is 256 characters.
        ### Returns
        ----
        Response object from requests library. 201 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces"
            body = {
                "displayName": displayName
            }
            if capacity_id != None:
                body["capacityId"]=capacity_id
            if description != None:
                body["description"]=description
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Delete Workspace
    def delete_workspace(self, workspace_id):
        """Deletes the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}".format(workspace_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.delete(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Delete Workspace Role Assignment by principal id
    def delete_workspace_role_assignment_by_principal_id(self, workspace_id, principal_id):
        """Deletes the specified role assignment for the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        principal_id: str uuid
            The principal id.
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/roleAssignments/{}".format(workspace_id, principal_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.delete(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Get Workspace
    def get_workspace(self, workspace_id):
        """Returns the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        ### Returns
        ----
        Dict:
            A dictionary containing a workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # List Workspaces by workspace role getting all paginated results from continuationToken in a single dictionary or pandas dataframe
    def list_workspaces(self, roles, return_pandas=False):
        """Returns a list of workspaces for the specified role.
        #### Parameters
        ----
        roles: string
            The role. Workspace role, like { "Member", "Admin", "Contributor", "Viewer"}
        ### Returns
        ----
        Dict:
            A dictionary containing all the workspaces.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces?role={}".format(roles)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            data = res.json()
            while 'continuationToken' in data and data['continuationToken'] != None:
                url = "https://api.fabric.microsoft.com/v1/workspaces?role={}&continuationToken={}".format(roles, data['continuationToken'])
                res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
                res.raise_for_status()
                data.update(res.json())
                data.pop('continuationToken')
            if return_pandas:
                return pd.DataFrame(data)
            else:
                return data
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
        
    # Unassign Workspace from Capacity
    def unassign_workspace_from_capacity(self, workspace_id):
        """Unassigns the specified workspace from the capacity.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/unassignFromCapacity".format(workspace_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Update Workspace
    def update_workspace(self, workspace_id, displayName=None, description=None):
        """Updates the properties of the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        displayName: string
            The workspace display name. The display name must follow naming rules according to item type.
        description: string
            The workspace description. Max length is 256 characters.
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}".format(workspace_id)
            body = {}
            if displayName != None:
                body["displayName"]=displayName
            if description != None:
                body["description"]=description
            if body == {}:
                raise Exception("Please specify a display name or description to update workspace.")
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.patch(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Update Workspace Role Assignment
    def update_workspace_role_assignment(self, workspace_id, principal_id, role):
        """Updates the specified role assignment for the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        principal_id: str uuid
            The principal id.
        role: string
            The role. Workspace role, like { "Member", "Admin", "Contributor", "Viewer"}
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/roleAssignments/{}".format(workspace_id, principal_id)
            body = {
                "role": role
            }
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.patch(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

class Onelake():
    """Simple library to use the onelake api and obtain items from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request onelake API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token
    
    # Create shortcut
    def create_shortcut(self, workspace_id, item_id, name, path, target, shortcut_conflict_policy=None):
        """Creates a shortcut in the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        name: string
            The shortcut name.
        path: string
            The shortcut path.
        target: string
            The shortcut target.
        shortcut_conflict_policy: string
            The shortcut conflict policy. { "Abort", "GenerateUniqueName" }
        ### Returns
        ----
        Response object from requests library. 201 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/shortcuts".format(workspace_id, item_id)
            if shortcut_conflict_policy != None:                
                url = url + "?shortcutConflictPolicy={}".format(shortcut_conflict_policy)
            body = {
                "name": name,
                "path": path,
                "target": target
            }            
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Delete Shortcut
    def delete_shortcut(self, workspace_id, item_id, shortcut_path, shortcut_name):
        """Deletes the specified shortcut from the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        shortcut_path: string
            The shortcut path.
        shortcut_name: string
            The shortcut name.
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        
        try: 
            url= "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/shortcuts/{}/{}".format(workspace_id, item_id, shortcut_path, shortcut_name)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}            
            res = requests.delete(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Get Shortcut
    def get_shortcut(self, workspace_id, item_id, shortcut_path, shortcut_name):
        """Returns the specified shortcut from the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        shortcut_path: string
            The shortcut path.
        shortcut_name: string
            The shortcut name.
        ### Returns
        ----
        Dict:
            A dictionary containing a shortcut in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/shortcuts/{}/{}".format(workspace_id, item_id, shortcut_path, shortcut_name)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # List Data Access Roles in workspace in item getting all paginated results from continuationToken in a single dictionary or pandas dataframe
    def list_data_access_roles(self, workspace_id, item_id, return_pandas=False):
        """Returns a list of data access roles for the specified item in the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from Fabric URL
        item_id: str uuid
            The item id. You can take it from Fabric URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the data access roles in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/dataAccessRoles".format(workspace_id, item_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            data = res.json()
            while 'continuationToken' in data and data['continuationToken'] != None:
                url = "https://api.fabric.microsoft.com/v1/workspaces/{}/items/{}/dataAccessRoles?continuationToken={}".format(workspace_id, item_id, data['continuationToken'])
                res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
                res.raise_for_status()
                data.update(res.json())
                data.pop('continuationToken')
            if return_pandas:
                return pd.DataFrame(data)
            else:
                return data
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

class LongRunningOperations():
    """Simple library to use the Long Running Operations api and obtain operation status from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request operations API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token
    def get_operation_state(self, operation_id):
        """Returns the current state of the long running operation
        #### Parameters
        ----
        operation_id: str uuid
            The operation id from the header of a run operation.
        ### Returns
        ----
        Dict:
            A dictionary containing the state of the operation
        """
        headers = {'Content-Type': 'application/json; charset=utf-8', "Authorization": "Bearer {}".format(self.token)}
        res = requests.get("https://api.fabric.microsoft.com/v1/operations/{}".format(operation_id), headers=headers)
        return res.text
    
    def get_operation_result(self, operation_id):
        """Returns the result of the long running operation
        #### Parameters
        ----
        operation_id: str uuid
            The operation id from the header of a run operation.
        ### Returns
        ----
        Dict:
            A dictionary containing the state of the operation
        """
        headers = {'Content-Type': 'application/json; charset=utf-8', "Authorization": "Bearer {}".format(self.token)}
        res = requests.get("https://api.fabric.microsoft.com/v1/operations/{}/result".format(operation_id), headers=headers)
        return res.text