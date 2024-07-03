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
    """Simple library to use the  api and obtain admin requests from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric admin API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token
            
    def get_item(self, workspace_id, item_id, type):
        """Returns the specified item from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        item_id: str uuid
            The item id. You can take it from PBI Service URL
        type: str 
            The type of the item. When querying for the following types, this parameter is required: { Report, Dashboard, SemanticModel, App, Dataflow }
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
            url = "https://api.fabric.microsoft.com/v1/admin/workspaces/{}/items/{}?type={}".format(workspace_id, item_id, type)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                      
    # List Items by workspace, capacity, type and status getting all paginated results from continuationToken in a single dictionary or pandas dataframe
    def list_items(self, workspace_id=None, capacity_id=None, type=None, status=None, return_pandas=False):
        """Returns a list of items for the specified workspace, capacity, type, and status.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        capacity_id: str uuid
            The capacity id.
        type: str
            The type of the item. When querying for the following types, this parameter is required: { Report, Dashboard, SemanticModel, App, Dataflow }
        status: str
            The status of the item. { "Active", "Deleted" }
        ### Returns
        ----
        Dict:
            A dictionary containing all the items.
        ### Limitations
        ----
        This API is supported for a number of item types, find the supported item types here.
        https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/item-management-overview
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/items"
            if workspace_id != None:
                url += "?workspaceId={}".format(workspace_id)
            if capacity_id != None:
                url += "&capacityId={}".format(capacity_id)
            if type != None:
                url += "&type={}".format(type)
            if status != None:
                url += "&status={}".format(status)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            data = res.json()
            while 'continuationToken' in data:
                url = "https://api.fabric.microsoft.com/v1/admin/items?continuationToken={}".format(data['continuationToken'])
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

    # Get List item Access Details by workspace and item of users
    def list_item_access_details(self, workspace_id, item_id, type=None):
        """Returns a list of users (including groups and service principals) and lists their workspace roles.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        item_id: str uuid
            The item id. You can take it from PBI Service URL
        type: str
            The type of the item. When querying for the following types, this parameter is required: { Report, Dashboard, SemanticModel, App, Dataflow }
        ### Returns
        ----
        Dict:
            A dictionary containing all the users who have access to the item.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/workspaces/{}/items/{}/users".format(workspace_id, item_id)
            if type != None:
                url += "?type={}".format(type)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
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

    # Get Workspace
    def get_workspace(self, workspace_id):
        """Returns the specified workspace.
        #### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/workspaces/{}".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # List Workspaces by workspace role getting all paginated results from continuationToken in a single dictionary or pandas dataframe
    def list_workspaces(self, capacity_id=None, name=None, state=None, type=None, return_pandas=False):
        """Returns a list of workspaces
        ### Parameters
        ----
        capacity_id: str uuid
            The capacity id.
        name: str
            The name of the workspace.
        state: str
            The state of the workspace. { "Active", "Deleted" }
        type: str
            The type of the workspace. { "MyWorkspace", "WorkspaceV2" }
        ### Returns
        ----
        Dict:
            A dictionary containing all the workspaces.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/workspaces"
            if capacity_id != None:
                url += "?capacityId={}".format(capacity_id)
            if name != None:
                url += "&name={}".format(name)
            if state != None:
                url += "&state={}".format(state)
            if type != None:
                url += "&type={}".format(type)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            data = res.json()
            while 'continuationToken' in data:
                url = "https://api.fabric.microsoft.com/v1/admin/workspaces?continuationToken={}".format(data['continuationToken'])
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

    # List Workspace Access Details by workspace of users
    def list_workspace_access_details(self, workspace_id):
        """Returns a list of users (including groups and service principals) and lists their workspace roles.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the users who have access to the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/workspaces/{}/users".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

class Users():
    """Simple library to use the api and obtain users from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric users API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token
        
    # List Access Entities by user and type getting all paginated results from continuationToken in a single dictionary or pandas dataframe
    def list_access_entities(self, user_id, type=None, return_pandas=False):
        """Returns a list of access entities for the specified user.
        ### Parameters
        ----
        user_id: str uuid
            The user id.
        type: str
            The type of the access entity. { "Report", "Datamart", "Lakehouse", "Dataflow", "Dashboard", "SemanticModel", "Notebook", etc }
        ### Returns
        ----
        Dict:
            A dictionary containing all the access entities.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/users/{}/access".format(user_id)
            if type != None:
                url += "?type={}".format(type)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            data = res.json()
            while 'continuationToken' in data:
                url = "https://api.fabric.microsoft.com/v1/admin/users/{}/access?continuationToken={}".format(user_id, data['continuationToken'])
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

class Domains():
    """Simple library to use the api and obtain domains from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request domains API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token

    # Assign Domain's workspaces by capacity
    def assign_domains_workspaces(self, domain_id, capacities_id):
        """Assigns the specified domain to the specified capacity.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        capacities_id: str uuid[]
            List of capacities ids
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}/assignWorkspacesByCapacities".format(domain_id)
            body = {
                "capacitiesIds": capacities_id
            }
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Assign Domain Workspaces By list of Id
    def assign_domain_workspaces(self, domain_id, workspaces_id):
        """Assigns the specified domain to the specified workspaces.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        workspaces_id: str uuid[]
            List of workspaces id
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}/assignWorkspaces".format(domain_id)
            body = {
                "workspacesIds": workspaces_id
            }
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Assign Domain Workspaces By Principals
    def assign_domain_workspaces_principals(self, domain_id, principals):
        """Assigns the specified domain to the specified principals.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        principals: str[]
            The principals have two items: { "id": "string", "type": "string"}
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}/assignWorkspacesByPrincipals".format(domain_id)
            body = {
                "principals": principals
            }
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Create Domain
    def create_domain(self, display_name, description=None, parent_domain_id=None): 
        """Creates a domain.
        ### Parameters
        ----
        display_name: str
            The domain display name. The display name cannot contain more than 40 characters.
        description: str
            The domain description. The description cannot contain more than 256 characters.
        parent_domain_id: str uuid
            The domain parent object ID.
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains"
            body = {
                "displayName": display_name
            }
            if description != None:
                body["description"] = description
            if parent_domain_id != None:
                body["parentDomainId"] = parent_domain_id
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}, data=json.dumps(body))
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Delete Domain
    def delete_domain(self, domain_id):
        """Deletes the specified domain.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}".format(domain_id)
            res = requests.delete(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Get Domain
    def get_domain(self, domain_id):
        """Returns the specified domain.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        ### Returns
        ----
        Dict:
            A dictionary containing the domain.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}".format(domain_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # List Domain Workspaces
    def list_domain_workspaces(self, domain_id):
        """Returns a list of workspaces for the specified domain.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        ### Returns
        ----
        Dict:
            A dictionary containing all the workspaces.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}/workspaces".format(domain_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # List Domains 
    def list_domains(self, non_empty_only=None):
        """Returns a list of domains.
        ### Parameters
        ----
        non_empty_only: bool
            When true, only return domains that have at least one workspace that has an item in it. Default: false.
        ### Returns
        ----
        Dict:
            A dictionary containing all the domains.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains"
            if non_empty_only != None:
                url += "?nonEmptyOnly={}".format(non_empty_only)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Unassign Domain's workspaces by id
    def unassign_domain_workspaces(self, domain_id, workspaces_id):
        """Unassigns the specified domain from the specified workspaces.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        workspaces_id: str uuid[]
            List of workspaces id
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}/unassignWorkspaces".format(domain_id)
            body = {
                "workspacesIds": workspaces_id
            }
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Unassign All Domain workspaces
    def unassign_all_domain_workspaces(self, domain_id):
        """Unassigns the specified domain from all workspaces.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}/unassignAllWorkspaces".format(domain_id)
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Update Domain
    def update_domain(self, domain_id, contributors_scope, display_name, description=None):
        """Updates the specified domain.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        contributors_scope: str
            The domain contributors scope. { "AdminsOnly", "AllTenant", "SpecificUsersAndGroups" }
        display_name: str
            The domain display name. The display name cannot contain more than 40 characters.
        description: str
            The domain description. The description cannot contain more than 256 characters.
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}".format(domain_id)
            body = {
                "contributorsScope": contributors_scope,
                "displayName": display_name
            }
            if description != None:
                body["description"] = description
            res = requests.patch(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}, data=json.dumps(body))
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Role Assignments bulk principals assign in domain
    def role_assignments_bulk_assign(self, domain_id, role, principals):
        """Assigns the specified role to the specified principals in the specified domain.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        role: str
            The role to assign to the principals.
        principals: str[]
            The principals have two items: [{"id": "string", "type": "string"}]. Type can be { "User", "Group", "ServicePrincipal" }
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}/roleAssignments/bulkAssign".format(domain_id)
            body = {
                "role": role,
                "principals": principals
            }
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}, data=json.dumps(body))
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Role Assignments bulk principals unassign in domain
    def role_assignments_bulk_unassign(self, domain_id, role, principals):
        """Unassigns the specified role from the specified principals in the specified domain.
        ### Parameters
        ----
        domain_id: str uuid
            The domain id.
        role: str
            The role to unassign from the principals.
        principals: str[]
            The principals have two items: [{"id": "string", "type": "string"}]. Type can be { "User", "Group", "ServicePrincipal" }
        ### Returns
        ----
            A successful response.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/admin/domains/{}/roleAssignments/bulkUnassign".format(domain_id)
            body = {
                "role": role,
                "principals": principals
            }
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}, data=json.dumps(body))
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
