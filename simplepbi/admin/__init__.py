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
    
    def get_datasets(self):
        """Returns a list of datasets for the organization..
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasets in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/datasets"
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_datasets_in_group(self, workspace_id):
        """Returns a list of datasets from the specified workspace.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasets in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/datasets".format(workspace_id)
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
        
    def get_reports(self):
        """Returns a list of reports for the organization.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        ### Returns
        ----
        Dict:
            A dictionary containing all the reports in the tenant.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/reports"
            response = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            return response
        except requests.exceptions.HTTPError as ex:
            print(ex)
        except requests.exceptions.RequestException as e:
            print(e)
            
    def get_reports_in_group(self, workspace_id):
        """Returns a list of reports from the specified workspace.
        ### Parameters
        ----
        self.token: str
            The Bearer Token to authenticate with Power Bi Rest API requests.
        workspace_id:
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the reports in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/admin/groups/{}/reports".format(workspace_id)
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
        dataset_id:
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

    def get_activity_events():
        """Dummy description
        """
    