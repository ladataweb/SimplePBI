r'''.
           @@@@@@@@@@
       @@@@..........@@@@
    @@@         .        @@@
  @@.           .         . @@
 @  .     _     .         .   @
@........| |...................@    *********************************************
@      . | |   _____  .        @
@      . | |  |  __ \ .        @    La Data Web
@      . | |__| |  | |.   ***  @
@........|____| |  | |...*   *.@    Copyright © 2025 Ignacio Barrau
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
from simplepbi.fabric.core import LongRunningOperations
class Report():
    """Simple library to use the api and obtain reports item from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric reports item API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token

    def get_report(self, workspace_id, report_id):
        """Returns properties of the specified report.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a report in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/reports/{}".format(workspace_id, report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def list_reports(self, workspace_id):
        """Returns a list of reports in the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the reports in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/reports".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def delete_report(self, workspace_id, report_id):
        """Deletes the specified report from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The report id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/reports/{}".format(workspace_id, report_id)
            headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)    
    def get_report_definition(self, workspace_id, report_id):
        """Returns the definition of the specified report.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing the definition of the report.
        """
        try:
            op = LongRunningOperations(self.token)
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/reports/{}/getDefinition".format(workspace_id, report_id)
            res = requests.post(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            opid = res.headers["x-ms-operation-id"]
            status="Running"
            while status == "Running":
                try:                    
                    ope = op.get_operation_state(opid)
                    status = json.loads(ope)["status"]                    
                except Exception as e:
                    print("Error while checking operation status: ", e)
                    break
            model = op.get_operation_result(opid)
            print("Operation completed with status: ", status)
            return json.loads(model)
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    