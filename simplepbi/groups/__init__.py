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

class Groups():
    """Simple library to use the Power BI api and obtain groups from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request admin API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
        
    def add_user_group(self, workspace_id, groupUserAccessRight, emailAddress, displayName=None, graphId=None, identifier=None, principalType=None):
        """Grants the specified user the specified permissions to the specified workspace.
        When user permissions to a workspace have been recently updated, the new permissions might not be immediately available through API calls. To refresh user permissions, use the Refresh User Permissions API call.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Request Body
        ----
        groupUserAccessRight: GroupUserAccessRight
            Access rights user has for the workspace (Permission level: Admin, Contributor, Member, Viewer or None). This is mandatory
        emailAddress: str
            Email address of the user. This is mandatory.
        displayName: str
            Display name of the principal
        graphId: str
            Identifier of the principal in Microsoft Graph. Only available for admin APIs
        identifier: str
            Object ID of the principal
        principalType: principalType
            The principal type (App, Group, User or None)
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/users".format(workspace_id)
            body = {
                "groupUserAccessRight": groupUserAccessRight, 
                "emailAddress": emailAddress 
            }
            if displayName != None:
                body["diplayName"]=displayName
            if graphId != None:
                body["graphId"] = graphId
            if identifier != None:
                body["identifier"] = identifier
            if principalType != None:
                body["principalType"] = principalType
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def get_groups(self):
        """Returns a list of workspaces the user has access to.
        When user permissions to a workspace have been recently updated, the new permissions might not be immediately available through API calls. To refresh user permissions, use the Refresh User Permissions API call.
        ### Parameters
        ----
        None
        ### Returns
        ----
        Dict:
            A dictionary containing the groups of the user.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_groups_users(self, workspace_id):
        """Returns a list of users that have access to the specified workspace.
        When user permissions to a workspace have been recently updated, the new permissions might not be immediately available through API calls. As a result, this API call might return an HTTP 401 error when a user has permissions to a workspace. To refresh user permissions, use the Refresh User Permissions API call.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi Workspace id. You can take it from PBI Service URL.
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/users".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def delete_group_preview(self, workspace_id):
        """Deletes the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi group id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}".format(workspace_id)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def delete_user_in_group(self, workspace_id, user):
        """Deletes the specified user permissions from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi group id. You can take it from PBI Service URL
        user: str
            The email address of the user or object ID of the service principal to delete.
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/users/{}".format(workspace_id, user)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def create_group_preview(self, name, workspaceV2=None):
        """Creates a new workspace.
        ### Parameters
        ----
        workspaceV2: bool
            Preview feature: Create a workspace V2. The only supported value is true.
        ### Request Body
        ----
        name: str
            The name of the newly created group.
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups"
            if workspaceV2 != None:
                url = url + "?workspaceV2={}".format(workspaceV2)
            body = {
                "name": name
            }                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
            
''' REQUEST not working
    def update_user_group_preview(self, workspace_id, groupUserAccessRight, emailAddress, displayName=None, graphId=None, identifier=None, principalType=None):
        """Grants the specified user the specified permissions to the specified workspace.
        ***This request is IN PREVIEW, it can contain fails yet.***
        When user permissions to a workspace have been recently updated, the new permissions might not be immediately available through API calls. To refresh user permissions, use the Refresh User Permissions API call.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Request Body
        ----
        groupUserAccessRight: GroupUserAccessRight
            Access rights user has for the workspace (Permission level: Admin, Contributor, Member, Viewer or None). This is mandatory
        emailAddress: str
            Email address of the user. This is mandatory.
        displayName: str
            Display name of the principal
        graphId: str
            Identifier of the principal in Microsoft Graph. Only available for admin APIs
        identifier: str
            Object ID of the principal
        principalType: principalType
            The principal type (App, Group, User or None). This is mandatory
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/users".format(workspace_id)
            body = {
                "groupUserAccessRight": groupUserAccessRight, 
                "emailAddress": emailAddress,
                "principalType": principalType
            }
            if displayName != None:
                body["diplayName"]=displayName
            if graphId != None:
                body["graphId"] = graphId
            if identifier != None:
                body["identifier"] = identifier
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.put(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
'''    