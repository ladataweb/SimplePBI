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

class Capacities():
    """Simple library to use the Power BI api and obtain capacities from it. The user must have administrator rights or assign permissions on the capacity.
    """

    def __init__(self, token):
        """Create a simplePBI object to request capacities API. The user must have administrator rights or assign permissions on the capacity.
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
            
    def get_capacities(self):
        """Returns a list of capacities that the user has access to.
        ### Parameters
        ----
        None
        ### Returns
        ----
        Dict:
            A dictionary containing all the capacities in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/capacities"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_refreshable_capacity(self, capacity_id, refreshable_id, expand=None):
        """Returns the specified refreshable for the specified capacity that the user has access to.
        Power BI retains a seven-day refresh history for each dataset, up to a maximum of sixty refreshes.
        ### Parameters
        ----
        capacity_id:
            The Power Bi capacity id. You can take it from PBI Service URL
        refreshable_id
            The Power Bi refreshable id in the capacity.
        expand: int
            Expands related entities inline, receives a comma-separated list of data types. Supported: capacities and groups
        ### Returns
        ----
        Dict:
            A dictionary containing all the refreshables in the capacity.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/capacities/{}/refreshables/{}?".format(capacity_id, refreshable_id)
            if expand != None:
                url = url + "$expand={}".format(expand)
            res = requests.get(url, headers={'Content-Type': 'capacitielication/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_refreshables_capacity(self, capacity_id, top, expand=None, filter=None, skip=None):
        """Returns a list of users that have access to the specified capacitie (Preview).
        ### Parameters
        ----
        capacity_id:
            The Power Bi capacitie id. You can take it from PBI Service URL
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        expand: string
            Expands related entities inline, receives a comma-separated list of data types. Supported: users, reports, dashboards, datasets, dataflows, workbooks
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the capacity.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/capacities/{}/refreshables?$top={}".format(capacity_id, top) 
            if expand != None:
                url = url + "&$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)
            if skip != None:
                url = url + "&$skip={}".format(skip) 
            res = requests.get(url, headers={'Content-Type': 'capacitielication/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_refreshables(self, top, expand=None, filter=None, skip=None):
        """Returns a list of refreshables for the organization.
        ### Parameters
        ----
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        expand: string
            Expands related entities inline, receives a comma-separated list of data types. Supported: users, reports, refreshables, datasets, dataflows, workbooks
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the refreshables in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/capacities/refreshables?$top={}".format(top)
            if expand != None:
                url = url + "&$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)            
            if skip != None:
                url = url + "&$skip={}".format(skip)  
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_workload(self, capacity_id, workloadName):
        """Returns the current state of a workload. If the workload is enabled, the percentage of maximum memory that the workload can consume is also returned.
        Workload APIs aren't relevant for Embedded Gen2 capacities.
        ### Parameters
        ----
        capacity_id: str uuid
            The capacity id
        workloadName: str
            The name of the workload
        ### Returns
        ----
        Dict:
            A dictionary containing all the capacities in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/capacities/{}/Workloads/{}".format(capacity_id, workloadName)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_workloads(self, capacity_id):
        """Returns the current state of the specified capacity workloads. If a workload is enabled, the percentage of maximum memory that the workload can consume is also returned.
        ### Parameters
        ----
        capacity_id: str uuid
            The capacity id
        ### Returns
        ----
        Dict:
            A dictionary containing all the capacities in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/capacities/{}/Workloads".format(capacity_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def assign_myworkspaces_to_capacity(self, tagetCapacityObjectId):
        """Assigns My workspace to the specified capacity. To unassign My workspace from a capacity, provide an empty GUID (00000000-0000-0000-0000-000000000000) as the capacityId. This requires Admin rights or permissions on the capacity.
        ### Parameters
        ----
        ### Request Body
        ----
        targetCapacityObjectId: str uuid
            The premium capacity ID
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/AssignToCapacity"
            body ={
                "capacityId":tagetCapacityObjectId
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def assign_to_capacity(self, tagetCapacityObjectId, workspacesToAssign):
        """Assigns the specified workspace to the specified capacity. To unassign My workspace from a capacity, provide an empty GUID (00000000-0000-0000-0000-000000000000) as the capacityId. This requires Admin rights or permissions on the capacity.
        ### Parameters
        ----
        ### Request Body
        ----
        targetCapacityObjectId: str uuid
            The premium capacity ID
        workspacesToAssign: str uuid
            List of the workspace IDs to be migrated to premium capacity
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/AssignToCapacity".format(workspacesToAssign)
            body ={
                "capacityId":tagetCapacityObjectId
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_capacity_assignment_status(self):
        """Gets the status of the My workspace assignment-to-capacity operation.
        ### Parameters
        ----
        None
        ### Returns
        ----
        Dict:
            A dictionary containing all the CapacityAssignmentStatus in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/CapacityAssignmentStatus"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_capacity_assignment_status_in_group(self, workspace_id):
        """Gets the status of the assignment-to-capacity operation for the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the CapacityAssignmentStatus in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/CapacityAssignmentStatus".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def patch_workload_preview(self, capacityId, workloadName, state, maxMemoryPercentageSetByUser=None ):    
        """Changes the state of a specific workload to Enabled or Disabled. When enabling a workload, specify the percentage of maximum memory that the workload can consume.
        *** THIS REQUEST IS IN PREVIEW IN SIMPLEPBI ***
        ### Parameters
        ----
        capacityId: str uud
            The capacity ID.
        workloadName: str
            The name of the workload
        ### Request Body
        ----
        state: str
            The capacity workload state. E.g { "Enabled, Disabled, Unsupported" }
        maxMemoryPercentageSetByUser: int
            The percentage of the maximum memory that a workload can consume (set by the user)
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/capacities/{}/Workloads/{}".format(capacityId, workloadName)
            body = {
                "state": state
            }            
            if maxMemoryPercentageSetByUser != None:
                body["maxMemoryPercentageSetByUser"]=maxMemoryPercentageSetByUser
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)