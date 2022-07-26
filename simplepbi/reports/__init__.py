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
from requests_toolbelt.multipart.encoder import MultipartEncoder
import io

class Reports():
    """Simple library to use the Power BI api and obtain reports from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request admin API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
    
    def get_report(self, report_id):
        """Returns the specified report from My workspace.
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a report in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/reports/{}".format(report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_report_in_group(self, workspace_id, report_id):
        """Returns the specified report from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a report in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}".format(workspace_id, report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_reports(self):
        """Returns a list of reports from My workspace.
        ### Parameters
        ----
        None
        ### Returns
        ----
        Dict:
            A dictionary containing all the reports in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/reports"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_reports_in_group(self, workspace_id):
        """Returns a list of reports from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the reports in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def get_page(self, report_id, page_name):
        """Returns the specified page within the specified report from "My Workspace".
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        page_name: str
            The Page Name in the URL
        ### Returns
        ----
        Dict:
            A dictionary containing a page in My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/reports/{}/pages/{}".format(report_id, page_name)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_page_in_group(self, workspace_id, report_id, page_name):
        """Returns the specified page within the specified report from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        page_name: str
            The Page Name in the URL 
        ### Returns
        ----
        Dict:
            A dictionary containing a page in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/pages/{}".format(workspace_id, report_id, page_name)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_pages(self, report_id):
        """Returns a list of pages within the specified report from "My Workspace".
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the pages in a reports from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/reports/{}/pages".format(report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_pages_in_group(self, workspace_id, report_id):
        """Returns a list of pages within the specified report from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the pages in a report from a workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/pages".format(workspace_id, report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def get_datasources(self, report_id):
        """Returns a list of data sources for the specified report from My workspace.
        GetReportDatasources is supported only for RDL reports.
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the report from My workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/reports/{}/datasources".format(report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_datasources_in_group(self, workspace_id, report_id):
        """Returns a list of data sources for the specified report from the specified workspace
        GetReportDatasources is supported only for RDL reports
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the report from the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/datasources".format(workspace_id, report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
          
    def export_report(self, report_id):
        """Exports the specified report from "My Workspace" to a .pbix file.
        Note: As a workaround for fixing timeout issues, you can set preferClientRouting to true.
        Large files are downloaded to a temporary blob. Their URL is returned in the response and stored in the locally downloaded PBIX file.
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        filename_path: str
            Path of the local machine to save the file. Example: C:\Temp\file.pbix
        ### Returns
        ----
        Dict:
            Response 200 OK with a File.
        ### Restrictions
        ----
        Export of a report with Power BI service live connection after calling rebind report is not supported. Refer to Download a report from the Power BI service to Power BI Desktop for requirements and limitations.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/reports/{}/Export".format(report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def export_report_in_group(self, workspace_id, report_id):
        """Exports the specified report from the specified workspace to a .pbix file.
        Note: As a workaround for fixing timeout issues, you can set preferClientRouting to true.
        Large files are downloaded to a temporary blob. Their URL is returned in the response and stored in the locally downloaded PBIX file.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            Response 200 OK with a File.
        ### Restrictions
        ----
        Export of a report with Power BI service live connection after calling rebind report is not supported. Refer to Download a report from the Power BI service to Power BI Desktop for requirements and limitations.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/Export".format(workspace_id, report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def simple_export_report(self, report_id, filename_path):
        """Exports the specified report from "My Workspace" to a .pbix file.
        Note: As a workaround for fixing timeout issues, you can set preferClientRouting to true.
        Large files are downloaded to a temporary blob. Their URL is returned in the response and stored in the locally downloaded PBIX file.
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        filename_path: str
            Path of the local machine to save the file. Example: C:\Temp\file.pbix
        ### Returns
        ----
        Dict:
            Response 200 OK with a File.
        ### Restrictions
        ----
        Export of a report with Power BI service live connection after calling rebind report is not supported. Refer to Download a report from the Power BI service to Power BI Desktop for requirements and limitations.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/reports/{}/Export".format(report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            open(filename_path, 'wb').write(res.content)
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def simple_export_report_in_group(self, workspace_id, report_id, filename_path):
        """Exports the specified report from the specified workspace to a .pbix file.
        Note: As a workaround for fixing timeout issues, you can set preferClientRouting to true.
        Large files are downloaded to a temporary blob. Their URL is returned in the response and stored in the locally downloaded PBIX file.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        filename_path: str
            Path of the local machine to save the file. Example: C:\Temp\file.pbix
        ### Returns
        ----
        Dict:
            Response 200 OK with a File.
        ### Restrictions
        ----
        Export of a report with Power BI service live connection after calling rebind report is not supported. Refer to Download a report from the Power BI service to Power BI Desktop for requirements and limitations.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/Export".format(workspace_id, report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            open(filename_path, 'wb').write(res.content)
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def simple_export_file(self, report_id, fileFormat, filename_path, includeHiddenPages=False):
        """Exports the specified report from "My Workspace" to a .pbix file.
        Note: As a workaround for fixing timeout issues, you can set preferClientRouting to true.
        Large files are downloaded to a temporary blob. Their URL is returned in the response and stored in the locally downloaded PBIX file.
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        filename_path: str
            Path of the local machine to save the file. Example: C:\Temp\file.pbix
        ### Returns
        ----
        Dict:
            Response 200 OK with a File.
        ### Restrictions
        ----
        Export of a report with Power BI service live connection after calling rebind report is not supported. Refer to Download a report from the Power BI service to Power BI Desktop for requirements and limitations.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/reports/{}/ExportTo".format(report_id)
            body= {
                "format": fileFormat,
                "powerBIReportConfiguration": {
                    "settings": {
                        "includeHiddenPages":includeHiddenPages
                        }
                    }
                }
            res = requests.post(url, data = json.dumps(body), headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            open(filename_path, 'wb').write(res.content)
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
           
    def simple_export_file_in_group(self, workspace_id, report_id, fileFormat, filename_path, includeHiddenPages=False):
        """Exports the specified report from the specified workspace to a .pbix file.
        Note: As a workaround for fixing timeout issues, you can set preferClientRouting to true.
        Large files are downloaded to a temporary blob. Their URL is returned in the response and stored in the locally downloaded PBIX file.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        filename_path: str
            Path of the local machine to save the file. Example: C:\Temp\file.pbix
        ### Returns
        ----
        Dict:
            Response 200 OK with a File.
        ### Restrictions
        ----
        Export of a report with Power BI service live connection after calling rebind report is not supported. Refer to Download a report from the Power BI service to Power BI Desktop for requirements and limitations.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/ExportTo".format(workspace_id, report_id)
            body= {
                "format": fileFormat,
                "powerBIReportConfiguration": {
                    "settings": {
                        "includeHiddenPages":includeHiddenPages
                        }
                    }
                }
            res = requests.post(url, data = json.dumps(body), headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(auth_token)})
            res.raise_for_status()
            open(filename_path, 'wb').write(res.content)
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
          
    def take_over_report_in_group_preview(self, workspace_id, report_id):
        """Transfers ownership over the specified PAGINATED REPORT to the current authorized user.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Request Body
        ----
        None
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/Default.TakeOver".format(workspace_id, report_id)
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                    
    def delete_report(self, report_id):
        """Deletes the specified report from My workspace.
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/reports/{}".format(report_id)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def delete_report_in_group(self, workspace_id, report_id):
        """Deletes the specified report from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL   
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}".format(workspace_id, report_id)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
           
    def clone_report(self, report_id, name, target_dataset_id=None, target_workspace_id=None):
        """Clones the specified report from "My Workspace".
        If after cloning the report and its dataset reside in two different upgraded workspaces or "My Workspace", a shared dataset will be created in the report's workspace.
        Reports with live connection will lose the live connection when cloning, and will have a direct binding to the target dataset.
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Request Body
        ----
        name: str
            The new report name
        target_dataset_id: str uuid
            (Optional) Parameter for specifying the target associated dataset ID. If not provided, the new report will be associated with the same dataset as the source report.
        target_workspace_id: str uuid
            (Optional) Parameter for specifying the target workspace ID. An empty GUID (00000000-0000-0000-0000-000000000000) indicates My workspace. If this parameter isn't provided, the new report will be cloned within the same workspace as the source report.
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/reports/{}/Clone".format(report_id)
            body = {
                "name": name
            }
            if target_dataset_id != None:
                body["targetModelId"]=target_dataset_id
            if target_workspace_id != None:
                body["targetWorkspaceId"] = target_workspace_id
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def clone_report_in_group(self, workspace_id, report_id, name, target_dataset_id=None, target_workspace_id=None):
        """Clones the specified report from the specified workspace.
        If after cloning the report and its dataset reside in two different upgraded workspaces or "My Workspace", a shared dataset will be created in the report's workspace.
        Reports with live connection will lose the live connection when cloning, and will have a direct binding to the target dataset.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL   
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Request Body
        ----
        name: str
            The new report name
        target_dataset_id: str uuid
            (Optional) Parameter for specifying the target associated dataset ID. If not provided, the new report will be associated with the same dataset as the source report.
        target_workspace_id: str uuid
            (Optional) Parameter for specifying the target workspace ID. An empty GUID (00000000-0000-0000-0000-000000000000) indicates My workspace. If this parameter isn't provided, the new report will be cloned within the same workspace as the source report.
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/Clone".format(workspace_id, report_id)
            body = {
                "name": name
            }
            if target_dataset_id != None:
                body["targetModelId"]=target_dataset_id
            if target_workspace_id != None:
                body["targetWorkspaceId"] = target_workspace_id
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def rebind_report_preview(self, report_id, dataset_id):
        """Rebinds the specified report from "My Workspace" to the requested dataset.
        If the dataset resides in a different upgraded workspace, a shared dataset will be created in "My Workspace".
        Reports with live connection will lose the live connection when rebinding, and will have a direct binding to the target dataset.
        ### Parameters
        ----       
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Request Body
        ----
        dataset_id: str uuid
            The Power Bi dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/reports/{}/Rebind".format(report_id)
            body = {
                "datasetId": dataset_id
            }
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def rebind_report_in_group_preview(self, workspace_id, report_id, dataset_id):
        """Rebinds the specified report from the specified workspace to the requested dataset.
        If the dataset resides in a different upgraded workspace or in "My Workspace", a shared dataset will be created in the report's workspace.
        Reports with live connection will lose the live connection when rebinding, and will have a direct binding to the target dataset
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Request Body
        ----
        dataset_id: str uuid
            The Power Bi dataset id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/Rebind".format(workspace_id, report_id)
            body = {
                "datasetId": dataset_id
            }
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def simple_copy_reports_between_groups(self, workspace_id_origin, report_id, workspace_id_destination, datasetDisplayName=None, nameConflict="CreateOrOverwrite", overrideModelLabel=None, overrideReportLabel=None):
        """Download and upload a power bi report from one workspace to another. Pbix must have a size lower than 1gb
        ### Parameters
        ----
        workspace_id origin and destination: str uuid
            The Power Bi workspace id from origin and from destination. You can take it from PBI Service URL
        report_id: str uud
            The Power Bi report id to migrate. You can take it from PBI Service URL
        datasetDisplayName: str 
            The display name of the dataset should include file extension
        nameConflict: str
            Specifies what to do if a dataset with the same name already exists. The default value is Ignore. You can also use CreateOrOverwrite,GenerateUniqueName or Overwrite
        overrideModelLabel: str
            Determines whether to override the existing label on a model when republishing a Power BI .pbix file. The service default value is true.
        overrideReportLabel: str
            Whether to override the existing label on a report when republishing a Power BI .pbix file. The service default value is true.            
        ### Returns
        ----
        Dict:
            Response 200. A dict with a new report id.
        ### Restrictions
        ----
        Export of a report with Power BI service live connection after calling rebind report is not supported. Refer to Download a report from the Power BI service to Power BI Desktop for requirements and limitations.
        
        """
        try:
            if datasetDisplayName == None:
                datasetDisplayName = self.get_report_in_group(workspace_id_origin, report_id)['name']+".pbix"            
            # Export report url
            exported_file = self.export_report_in_group(workspace_id_origin, report_id)
            # Import report url
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/imports?datasetDisplayName={}".format(workspace_id_destination, datasetDisplayName)
            if nameConflict != None:
                	url = url + "&nameConflict={}".format(str(nameConflict))
            if overrideModelLabel != None:
                	url = url + "&overrideModelLabel={}".format(str(overrideModelLabel))
            if overrideReportLabel != None:
                	url = url + "&overrideReportLabel={}".format(str(overrideReportLabel))
            # Set the file to the correct format 
            nube = io.BytesIO(exported_file.content)
            # None here means we skip the filename and file content is important 
            files = {'value': (None, nube, 'multipart/form-data')}
            # The MultipartEncoder is posted as data, don't use files=...!
            mp_encoder = MultipartEncoder(fields=files)
            # The MultipartEncoder provides the content-type header with the boundary:
            headers = {'Content-Type': 'multipart/form-data', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = mp_encoder, headers=headers)
            res.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
'''             
    def update_parameters_in_group(self, workspace_id, report_id, updateDetails):
        """Updates the parameters values for the specified report from the specified workspace.
        If you're using enhanced report metadata, refresh the report to apply the new parameter values.
        If you're not using enhanced report metadata, wait 30 minutes for the update data sources operation to complete, and then refresh the report.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Request Body
        ----
        updateDetails: UpdateMashupParameterDetails [] str
            The report parameter list to update. Example:
            [
                {
                    "name": "ParameterName1",
                    "newValue": "NewDB"
                },
                {
                    "name": "ParameterName2",
                    "newValue": "5678"
                }
            ]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        reports created using the public XMLA endpoint aren't supported. To make changes to those data sources, the admin must use the Azure Analysis Services client library for Tabular Object Model.
        DirectQuery connections are only supported with enhanced report metadata.
        reports with Azure Analysis Services live connections aren't supported.
        Maximum of 100 parameters per request.
        All specified parameters must exist in the report.
        Parameters values should be of the expected type.
        The parameter list cannot be empty or include duplicate parameters.
        Parameters names are case-sensitive.
        Parameter IsRequired must have a non-empty value.
        The parameter types Any and Binary cannot be updated.
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/Default.UpdateParameters".format(workspace_id, report_id)
            body = {
                "updateDetails": updateDetails
            }               
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_refresh_schedule(self, report_id, NotifyOption=None, days=None, enabled=None, localTimeZoneId=None, times=None):
        """Updates the refresh schedule for the specified report from My workspace.
        A request that disables the refresh schedule should contain no other changes.
        At least one day must be specified. If no times are specified, then Power BI will use a default single time per day.        
        ### Parameters
        ----
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Request Body
        ----
        NotifyOption: ScheduleNotifyOption str
            Notification option at scheduled refresh termination. Example MailOnFailure or NoNotification.
        days: str []
            Days to execute the refresh. Example: ["Sunday", "Tuesday"]
        enabled: bool
            is the refresh enabled
        localTimeZoneId: str
            The ID of the timezone to use. See TimeZone Info. Example "UTC"
        times: str []
            Times to execute the refresh within each day. Example: ["07:00", "16:00"]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        The limit on the number of time slots per day depends on whether a Premium or Shared capacity is used.
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/reports/{}/refreshSchedule".format(report_id)
            body = {
                "value": {}
            }
            
            if NotifyOption != None:
                body["value"]["NotifyOption"]=NotifyOption
            if days != None:
                body["value"]["days"] = days
            if enabled != None:
                body["value"]["enabled"] = enabled
            if localTimeZoneId != None:
                body["value"]["localTimeZoneId"] = localTimeZoneId
            if times != None:
                body["value"]["times"]=times
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def update_refresh_schedule_in_group(self, workspace_id, report_id, NotifyOption=None, days=None, enabled=None, localTimeZoneId=None, times=None):
        """Updates the refresh schedule for the specified report from the specified workspace.
        A request that disables the refresh schedule should contain no other changes.
        At least one day must be specified. If no times are specified, then Power BI will use a default single time per day.       
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Request Body
        ----
        NotifyOption: ScheduleNotifyOption str
            Notification option at scheduled refresh termination. Example MailOnFailure or NoNotification.
        days: str []
            Days to execute the refresh. Example: ["Sunday", "Tuesday"]
        enabled: bool
            is the refresh enabled
        localTimeZoneId: str
            The ID of the timezone to use. See TimeZone Info. Example "UTC"
        times: str []
            Times to execute the refresh within each day. Example: ["07:00", "16:00"]
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        The limit on the number of time slots per day depends on whether a Premium or Shared capacity is used.
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/reports/{}/refreshSchedule".format(workspace_id, report_id)
            body = {
                "value": {}
            }
            
            if NotifyOption != None:
                body["value"]["NotifyOption"]=NotifyOption
            if days != None:
                body["value"]["days"] = days
            if enabled != None:
                body["value"]["enabled"] = enabled
            if localTimeZoneId != None:
                body["value"]["localTimeZoneId"] = localTimeZoneId
            if times != None:
                body["value"]["times"]=times
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            

            
'''