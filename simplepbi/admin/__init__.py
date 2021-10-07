import json
import requests
import token

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
    
    def get_datasets(self, filter=None, skip=None, top=None)):
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
            return response
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
            return response
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
            return response
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
            return response
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
            return response
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
            return response
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
            return response
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
            return response
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_groups(self, top=None, expand=None, filter=None, skip=None):
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
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups?"
            if expand != None:
                url = url + "$expand={}".format(expand)
            if filter != None:
                url = url + "&$filter={}".format(filter)
            if top != None:
                url = url + "&$top={}".format(top)
            if skip != None:
                url = url + "&$skip={}".format(skip)                
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response
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
            return response
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
            return response
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)

    def get_activity_events():
        """Dummy description
        """
    