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
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
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
            
            
    def get_activity_events():
        """Dummy description
        """
    