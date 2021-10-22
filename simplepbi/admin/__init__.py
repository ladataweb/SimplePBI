import json
import requests
from simplepbi import utils
from datetime import date, timedelta
import pandas as pd

class Admin():
    """Simple library to use the Power BI api and obtain datasets from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request admin API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
    
    def get_datasets(self, filter=None, skip=None, top=None):
        """Returns a list of datasets for the organization..
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasets in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/datasets?"
            if filter != None:
                url = url + "$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip) 
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_datasets_in_group(self, workspace_id, expand=None, filter=None, skip=None, top=None):
        """Returns a list of datasets from the specified workspace.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        expand: string
            Expands related entities inline, receives a comma-separated list of data types. Supported: users, reports, dashboards, datasets, dataflows, workbooks
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasets in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/datasets?".format(workspace_id)
            if expand != None:
                url = url + "$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)
            if skip != None:
                url = url + "&$skip={}".format(skip)   
            if top != None:
                url = url + "&$top={}".format(top)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_dataset_users(self, dataset_id):
        """Returns a list of users that have access to the specified dataset (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the dataset.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/datasets/{}/users".format(dataset)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_datasources(self, dataset_id):
        """Returns a list of datasources for the specified dataset.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        dataset_id:
            The Power Bi Dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the dataset.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/datasets/{}/datasources".format(dataset_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_dataset_to_dataflows_links_in_group(self, workspace_id):
        """Returns a list of upstream dataflows for datasets from the specified workspace.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the dataset.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/datasets/upstreamDataflows".format(workspace_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
        
    def get_reports(self, filter=None, skip=None, top=None):
        """Returns a list of reports for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the reports in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/reports?"
            if filter != None:
                url = url + "$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip)  
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_reports_in_group(self, workspace_id, filter=None, skip=None, top=None):
        """Returns a list of reports from the specified workspace.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the reports in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/reports?".format(workspace_id)
            if filter != None:
                url = url + "$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip) 
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_reports_users(self, report_id):
        """Returns a list of users that have access to the specified report (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        report_id:
            The Power Bi Report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the report.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/reports/{}/users".format(report_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_groups(self, top, expand=None, filter=None, skip=None):
        """Returns a workspace for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
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
            A dictionary containing all the workspaces in the organization.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups?$top={}".format(top)
            if expand != None:
                url = url + "&$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)
            if skip != None:
                url = url + "&$skip={}".format(skip)                
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_group(self, group_id, expand=None):
        """Returns a workspace for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        group_id: str
            The Power Bi Workspace id. You can take it from PBI Service URL
        expand: string
            Expands related entities inline, receives a comma-separated list of data types. Supported: users, reports, dashboards, datasets, dataflows, workbooks
        ### Returns
        ----
        Dict:
            A dictionary containing all the workspaces in the organization.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}".format(group_id)
            if expand != None:
                url = url + "?$expand={}".format(expand)              
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_groups_users(self, group_id):
        """Returns a list of users that have access to the specified workspace. This is a preview API call.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        group_id: str
            The Power Bi Workspace id. You can take it from PBI Service URL.
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/users".format(group_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def restore_deleted_group(self, workspace_id, emailAddress, name=None):
        """Restores a deleted workspace.
        This API call only supports restoring workspaces in the new workspace experience.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Request Body
        ----
        groupUserAccessRight: GroupUserAccessRight
            Access rights user has for the workspace (Permission level: Admin, Contributor, Member, Viewer or None). This is mandatory
        emailAddress: str
            Email address of the user. This is mandatory.
        name: str
            The name of the group to be restored.
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/restore".format(workspace_id)
            body = {
                "emailAddress": emailAddress 
            }
            if name != None:
                body["name"]=displayName            
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)

    def get_dashboards(self, expand=None, filter=None, skip=None, top=None):
        """Returns a list of dashboards for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        expand: string
            Expands related entities inline, receives a comma-separated list of data types. Supported: users, reports, dashboards, datasets, dataflows, workbooks
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. 
        ### Returns
        ----
        Dict:
            A dictionary containing all the dashboards in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/dashboards?"
            if expand != None:
                url = url + "$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip)  
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_dashboards_in_group(self, workspace_id, filter=None, skip=None, top=None):
        """Returns a list of dashboards from the specified workspace.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the dashboards in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/dashboards?".format(workspace_id)
            if filter != None:
                url = url + "$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip) 
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_dashboards_users(self, dashboard_id):
        """Returns a list of users that have access to the specified dashboard (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        dashboard_id:
            The Power Bi dashboard id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the dashboard.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/dashboards/{}/users".format(dashboard_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
           
    def get_tiles(self, dashboard_id):
        """Returns a list of tiles within the specified dashboard.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        dashboard_id:
            The Power Bi dashboard id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the tiles in the dashboard.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/dashboards/{}/tiles".format(dashboard_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
    
    def get_dataflows(self, filter=None, skip=None, top=None):
        """Returns a list of dataflows for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the dataflows in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/dataflows?"
            if filter != None:
                url = url + "$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip)  
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_dataflows_in_group(self, workspace_id, filter=None, skip=None, top=None):
        """Returns a list of dataflows from the specified workspace.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the dataflows in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/dataflows?".format(workspace_id)
            if filter != None:
                url = url + "$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip) 
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_dataflows_users(self, dataflow_id):
        """Returns a list of users that have access to the specified dataflow (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        dataflow_id:
            The Power Bi dataflow id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the dataflow.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/dataflows/{}/users".format(dataflow_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
        
    def get_dataflow_datasources(self, dataflow_id):
        """Returns a list of datasources for the specified dataflow.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        dataflow_id:
            The Power Bi Dataflow id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the dataflow.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/dataflows/{}/datasources".format(dataflow_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_upstream_dataflows_in_group(self, workspace_id, dataflow_id):
        """Returns a list of upstream dataflows for the specified dataflow.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        dataflow_id:
            The Power Bi Dataflow id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the dataflows in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/dataflows/{}/upstreamDataflows".format(workspace_id, dataflow_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)    
            
    def export_dataflow(self, dataflow_id):
        """Exports the definition for the specified dataflow to a JSON file.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        dataflow_id:
            The Power Bi Dataflow id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the metadata built in the dataflow.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/dataflows/{}/export".format(dataflow_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_apps(self, top=None):
        """Returns a list of apps for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the apps in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/apps?"
            if top != None:
                url = url + "$top={}".format(top)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_apps_users(self, app_id):
        """Returns a list of users that have access to the specified app (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        app_id:
            The Power Bi app id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the app.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/apps/{}/users".format(app_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_capacities(self, expand=None):
        """Returns a list of capacities for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        expand: int
            Expands related entities inline
        ### Returns
        ----
        Dict:
            A dictionary containing all the capacities in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/capacities?"
            if expand != None:
                url = url + "$expand={}".format(expand)
            response = requests.get(url, headers={'Content-Type': 'capacitielication/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_capacities_users(self, capacity_id):
        """Returns a list of users that have access to the specified capacitie (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        capacity_id:
            The Power Bi capacity id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the capacity.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/capacities/{}/users".format(capacity_id)
            response = requests.get(url, headers={'Content-Type': 'capacitielication/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_refreshable_capacity(self, capacity_id, refreshable_id, expand=None):
        """Returns a list of users that have access to the specified capacitie (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
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
            url = "https://api.powerbi.com/v1.0/myorg/admin/capacities/{}/refreshables/{}?".format(capacity_id, refreshable_id)
            if expand != None:
                url = url + "$expand={}".format(expand)
            response = requests.get(url, headers={'Content-Type': 'capacitielication/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_refreshables_capacity(self, capacity_id, top, expand=None, filter=None, skip=None):
        """Returns a list of users that have access to the specified capacitie (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
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
            url = "https://api.powerbi.com/v1.0/myorg/admin/capacities/{}/refreshables?$top={}".format(capacity_id, top) 
            if expand != None:
                url = url + "&$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)
            if skip != None:
                url = url + "&$skip={}".format(skip) 
            response = requests.get(url, headers={'Content-Type': 'capacitielication/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
           
    def get_user_artifact_access_preview(auth_token, userGraphId, return_pandas=True):
        '''Returns a list of artifacts that the given user have access to (Preview).
        *** THIS REQUEST IS IN PREVIEW IN SIMPLEPBI ***
        
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        userGraphId: str uuid
            The graph ID of user
        return_pandas: bool
            Flag to specify if you want to return a dict response or a pandas dataframe of events. By default pandas
        ### Returns
        ----
        Pandas dataframe concatenating iterations unless you change return_pandas to false, then it changes to dict
        '''        
        columnas = ['artifactId', 'displayName', 'artifactType', 'accessRight']
        df_total = pd.DataFrame(columns=columnas)
        dict_total = {'ArtifactAccessEntities': [] }
        url = "https://api.powerbi.com/v1.0/myorg/admin/users/{}/artifactAccess".format(userGraphId)
        headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(auth_token)}
        ban = True   
        contar = 0    
        try:
            while(ban):        
                response = requests.get(url, headers=headers)
                if return_pandas:
                    js = json.dumps(response.json()["ArtifactAccessEntities"])
                    df = pd.read_json(js)
                    df_total = df_total.append(df, sort=True, ignore_index=True)
                    print(df_total.head())
                else:
                    if response.json()["ArtifactAccessEntities"]:
                        append_value(dict_total, "ArtifactAccessEntities", response.json()["ArtifactAccessEntities"])
                        print(dict_total)
                print(response.status_code)
                contar = contar +1
                print(contar)            
                if "continuationUri" not in response.json():
                    ban=False
                else:
                    url = response.json()["continuationUri"]                   
                    print(response.json()["continuationUri"])    
            if return_pandas:
                print(df_total.tail())
                return df_total
            else:
                print(dict_total)
                return dict_total
        except requests.exceptions.Timeout:
            print("ERROR: The request method has exceeded the Timeout")
        except requests.exceptions.TooManyRedirects:
            print("ERROR: Bad URL try a different one")
        except requests.exceptions.RequestException as e:
            print("Catastrophic error.")
            raise SystemExit(e)
        except Exception as ex:
            print("ERROR: ", ex)
            
    def get_unused_artifacts(self, workspace_id):
        """Returns a list of artifacts from the specified workspace with last used date.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the artifacts in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/unused".format(workspace_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)        
            
    def get_pipelines(self, expand=None, filter=None, skip=None, top=None):
        """Returns a list of pipelines for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        expand: string
            Expands related entities inline, receives a comma-separated list of data types. Supported: users, reports, pipelines, datasets, dataflows, workbooks
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the pipelines in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/pipelines?"
            if expand != None:
                url = url + "$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip)  
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
			
    def get_pipelines_users(self, pipeline_id):
        """Returns a list of users that have access to the specified pipeline (Preview).
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        pipeline_id:
            The Power Bi pipeline id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the users in the pipeline.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/pipelines/{}/users".format(pipeline_id)
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)    
        
    def get_imports(self, expand=None, filter=None, skip=None, top=None):
        """Returns a list of imports for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        expand: string
            Expands related entities inline, receives a comma-separated list of data types. Supported: users, reports, imports, datasets, dataflows, workbooks
        filter: string
            Filters the results based on a boolean condition
        skip: int 
            Skips the first n results. Use with top to fetch results beyond the first 5000.
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the imports in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/imports?"
            if expand != None:
                url = url + "$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip)  
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
    
    def get_refreshables(self, expand=None, filter=None, skip=None, top=None):
        """Returns a list of refreshables for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
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
            url = "https://api.powerbi.com/v1.0/myorg/admin/refreshables?$top={}".format(top)
            if expand != None:
                url = url + "&$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)            
            if skip != None:
                url = url + "&$skip={}".format(skip)  
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
        
    def get_encryption_keys(self, expand=None, filter=None, skip=None, top=None):
        """Returns the encryption keys for the tenant.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        ### Returns
        ----
        Dict:
            A dictionary containing all the refreshables in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/tenantKeys"
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response.json()
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def add_encryption_key_preview(self, activate, isDefault, keyVaultKeyIdentifier, name):
        """Adds an encryption key for Power BI workspaces assigned to a capacity.
        *** THIS REQUEST IS IN PREVIEW IN SIMPLEPBI ***
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        ### Request Body
        ----
        All the keys are requested for the body
        activate: bool
            Indicates to activate any inactivated capacities to use this key for its encryption.
        isDefault: bool
            Whether an encryption key is the default key for the entire tenant. Any newly created capacity inherits the default key.
        keyVaultKeyIdentifier: str
            The URI that uniquely specifies an encryption key in Azure Key Vault.
        name:
            The name of the encryption key        
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/tenantKeys"
            body = {
                "activate": activate, 
                "isDefault": isDefault,
                "keyVaultKeyIdentifier":keyVaultKeyIdentifier,
                "name":name
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def rotate_encryption_key_preview(self, tenantKeyId, keyVaultKeyIdentifier):
        """Adds an encryption key for Power BI workspaces assigned to a capacity.
        *** THIS REQUEST IS IN PREVIEW IN SIMPLEPBI ***
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        tenantKeyId: str uuid
            The tenant key ID
        ### Request Body
        ----        
        keyVaultKeyIdentifier: str
            The URI that uniquely specifies an encryption key in Azure Key Vault.
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/tenantKeys/{}/Default.Rotate".format(tenantKeyId)
            body = {
                "keyVaultKeyIdentifier":keyVaultKeyIdentifier
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
    
    def add_user_to_group(self, workspace_id, groupUserAccessRight, emailAddress, displayName=None, graphId=None, identifier=None, principalType=None):
        """Grants user permissions to the specified workspace.
        This API call only supports updating workspaces in the new workspace experience and adding a user principle.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
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
            url= "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/users".format(workspace_id)
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
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def delete_user_from_group(self, workspace_id, user):
        """Removes user permissions from the specified workspace.
        This API call only supports updating workspaces in the new workspace experience and adding a user principle.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        user: str
            The user principal name (UPN) of the user to remove (usually the user's email).
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/users/{}".format(workspace_id, user)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def update_group_preview(self, workspace_id, capacityId=None, dashboards=None, dataflowStorageId=None, dataflows=None, datasets=None, description=None, isOnDedicatedCapacity=None, isReadOnly=None, name=None, pipelineId=None, reports=None, state=None, typee=None, users=None, workbooks=None):    
        """Updates the properties of the specified workspace.
        *** THIS REQUEST IS IN PREVIEW IN SIMPLEPBI ***
        This API call call only updates workspaces in the new workspace experience. Only the name and description can be updated. The name must be unique inside an organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Request Body
        ----
        id: string
            The workspace ID
        capacityId: string
            The capacity ID
        dashboards: str[]
            List of the dashboards ids that belong to the group. Available only for admin API calls.
        dataflowStorageId: string
            The Power BI dataflow storage account ID
        dataflows: str[]
            List of the dataflows ids that belong to the group. Available only for admin API calls.
        datasets: str[]
            List of the datasets ids that belong to the group. Available only for admin API calls.
        description: string
            The group description. Available only for admin API calls.
        isOnDedicatedCapacity: bool
            Is the group on dedicated capacity
        isReadOnly: bool
            Is the group read only
        name: string
            The group name
        pipelineId: string
            The deployment pipeline ID that the workspace is assigned to. Available only for workspaces in the new workspace experience and only for admin API calls.
        reports: str[]
            List of the reports ids that belong to the group. Available only for admin API calls.
        state: string
            The group state. Available only for admin API calls.
        typee: string
            The type of group. Available only for admin API calls.
        users: GroupUser[]
            List of the users that belong to the group, and their access rights. This value will be empty. It will be removed from the payload response in an upcoming release. To retrieve user information on an artifact, please consider using the Get Group User APIs, or the PostWorkspaceInfo API with the getArtifactUser parameter.
        workbooks: str[]
            List of the workbooks ids that belong to the group. Available only for admin API calls.
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/groups/{}".format(workspace_id)
            body = {
                "id": workspace_id
            }
            
            if capacityId != None:
                body["capacityId"]=capacityId
            if dashboards != None:
                body["dashboards"] = dashboards
            if dataflowStorageId != None:
                body["dataflowStorageId"] = dataflowStorageId
            if dataflows != None:
                body["dataflows"] = dataflows
            if datasets != None:
                body["datasets"]=datasets
            if description != None:
                body["description"] = description
            if isOnDedicatedCapacity != None:
                body["isOnDedicatedCapacity"] = isOnDedicatedCapacity
            if isReadOnly != None:
                body["isReadOnly"] = isReadOnly
            if name != None:
                body["name"]=name
            if pipelineId != None:
                body["pipelineId"] = pipelineId
            if reports != None:
                body["reports"] = reports
            if state != None:
                body["state"] = state
            if typee != None:
                body["type"] = typee
            if users != None:
                body["users"] = users
            if workbooks != None:
                body["workbooks"] = workbooks
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def update_user_in_pipeline(self, pipeline_id, identifier, principalType, accessRight):
        """Grants user permissions to a specified deployment pipeline.
        
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        pipeline_id:
            The Power Bi Deployment Pipeline id. You can take it from PBI Service URL
        ### Request Body
        ----
        identifier: str
            For Principal type 'User' provide UPN , otherwise provide Object ID of the principal. This is mandatory
        principalType: principalType
            The principal type (App, Group, User or None). This is mandatory.
        accessRight: GroupUserAccessRight
            accessRequired - Access rights a user has for the deployment pipeline. (Permission level: Admin). This is mandatory
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/pipelines/{}/users".format(pipeline_id)
            body = {
                "identifier": identifier ,
                "principalType": principalType ,
                "accessRight": accessRight
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def delete_user_from_pipeline(self, pipeline_id, identifier):
        """Removes user permissions from a specified deployment pipeline.
        
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        pipeline_id: str uuid
            The deployment pipeline ID
        identifier: str
            For Principal type 'User' provide UPN , otherwise provide Object ID of the principal
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/pipelines/{}/users/{}".format(pipeline_id, identifier)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def assign_workspaces_to_capacity_preview(self, tagetCapacityObjectId, workspacesToAssign):
        """Assigns the specified workspaces to the specified Premium capacity.
        *** THIS REQUEST IS IN PREVIEW IN SIMPLEPBI ***
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        ### Request Body
        ----
        capacityMigrationAssignments: Assignment contract for migrating workspaces to premium capacity as tenant admin
        
        targetCapacityObjectId: str
            The premium capacity ID
        workspacesToAssign: str[]
            List of the workspace IDs to be migrated to premium capacity
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/capacities/AssignWorkspaces"
            body ={
                "tagetCapacityObjectId":tagetCapacityObjectId,
                "workspacesToAssign":workspacesToAssign
            }
            body_option2 ={
                "capacityMigrationAssignments":[{
                    "tagetCapacityObjectId":tagetCapacityObjectId,
                    "workspacesToAssign":workspacesToAssign
                }]
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def unassign_workspaces_from_capacity_preview(self, workspacesToAssign):
        """Unassigns the specified workspaces from capacity.
        *** THIS REQUEST IS IN PREVIEW IN SIMPLEPBI ***
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        ### Request Body
        ----        
        workspacesToAssign: str[]
            List of the workspace IDs to be migrated to premium capacity
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/admin/capacities/UnassignWorkspaces"
            body ={
                "workspacesToAssign":workspacesToAssign
            }
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.post(url, data = json.dumps(body), headers = headers)
            return res
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
                                                                                         
    def get_activity_events_preview(self, activity_date=None, return_pandas=True):
        '''Returns a dict of pandas dataframe of audit activity events for a tenant.
        *** THIS REQUEST IS IN PREVIEW IN SIMPLEPBI ***
        The continuation token is automtaically used to get all the results in the date.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        activity_date: str "yyyy-mm-dd"
            The Single date to get events from the whole day.
            If the date is not specify it will return yesterday events by default.
        return_pandas: bool
            Flag to specify if you want to return a dict response or a pandas dataframe of events.
        ### Returns
        ----
        Pandas dataframe concatenating iterations unless you change return_pandas to false, then it changes to dict
        '''        
        columnas = ['Id', 'RecordType', 'CreationTime', 'Operation', 'OrganizationId',
           'UserType', 'UserKey', 'Workload', 'UserId', 'ClientIP', 'UserAgent',
           'Activity', 'ItemName', 'WorkSpaceName', 'DatasetName', 'WorkspaceId',
           'ObjectId', 'DatasetId', 'DataConnectivityMode', 'IsSuccess',
           'RequestId', 'ActivityId', 'TableName', 'LastRefreshTime']
        df_total = pd.DataFrame(columns=columnas)
        dict_total = {'activityEventEntities': [] }
        if activity_date == None:
            activity_date = date.today()- timedelta(days=1)
        else:
            date(int(activity_date.split("-")[0]),int(activity_date.split("-")[1]),int(activity_date.split("-")[2]))
        start = activity_date.strftime("'%Y-%m-%dT%H:%M:00.000Z'")
        end = activity_date.strftime("'%Y-%m-%dT23:59:59.000Z'")
        url = "https://api.powerbi.com/v1.0/myorg/admin/activityevents?startDateTime={}&endDateTime={}".format(start, end)
        ban = True   
        contar = 0    
        try:
            while(ban):        
                response = requests.get(url,
                    headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
                    )
                if return_pandas:
                    js = json.dumps(response.json()["activityEventEntities"])
                    df = pd.read_json(js)
                    #print(df.head())
                    df_total = df_total.append(df, sort=True, ignore_index=True)
                    #print(df_total.head())
                else:
                    if response.json()["activityEventEntities"]:                
                        append_value(dict_total, "activityEventEntities", response.json()["activityEventEntities"][0])
                    
                print(response.status_code)
                contar = contar +1
                print(contar)            
                print(response.json()["continuationUri"])
                
                if response.json()["continuationUri"] == None:
                    ban=False
                url = response.json()["continuationUri"]   
            if return_pandas:
                return df_total
            else:
                return dict_total
        except requests.exceptions.Timeout:
            print("ERROR: The request method has exceeded the Timeout")
        except requests.exceptions.TooManyRedirects:
            print("ERROR: Bad URL try a different one")
        except requests.exceptions.RequestException as e:
            print("Catastrophic error.")
            raise SystemExit(e)
        except Exception as ex:
            print(ex)