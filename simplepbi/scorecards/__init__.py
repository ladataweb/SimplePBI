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
@........|____| |  | |...*   *.@    Copyright © 2022 Ignacio Barrau
@   .       . | |__| |. *     *@
@   .       . |_____/ . *     *@    *********************************************
@   .       .         . *     *@
@   .       .         . *******@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''

import json
import requests

class Scorecards():
    """Simple library to use the Power BI api and obtain scorecards from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request scorecards API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token    
            
    def get_scorecard_in_group(self, workspace_id, scorecard_id, expand=None):
        """Returns the specified scorecard from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        scorecard_id: str uuid
            The Power Bi scorecard id.
        expand: str
            Accepts a comma-separated list of data types, which will be expanded inline in the response. Supports { goals, goalValues, aggregations, and notes }
        ### Returns
        ----
        Dict:
            A dictionary containing a scorecard in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/scorecards({})".format(workspace_id, scorecard_id)
            if expand != None:
                url = url + "?$expand={}".format(expand)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_scorecards_in_group(self, workspace_id, top=None):
        """Returns a list of scorecards from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        top: int
            Returns only the first n results. This parameter is mandatory and must be in the range of 1-5000.
        ### Returns
        ----
        Dict:
            A dictionary containing all the scorecards in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/scorecards".format(workspace_id)            
            if top != None:
                url = url + "?$top={}".format(top)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_scorecard_by_report(self, workspace_id, report_id, expand=None):
        """Reads a scorecard associated with an internal report ID.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        report_id: str uuid
            The ID of the internal report associated with the scorecard
        expand: str
            Accepts a comma-separated list of data types, which will be expanded inline in the response. Supports { goals, goalValues, and aggregations }
        ### Returns
        ----
        Dict:
            A dictionary containing a scorecard in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/scorecards/GetScorecardByReportId(reportId={})".format(workspace_id, report_id)
            if expand != None:
                url = url + "?$expand={}".format(expand)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def post_scorecard(self, workspace_id, name, description=None, sensitivityLabelId=None):
        """Creates a new scorecard.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Request Body
        ----
        name: str
            The scorecard name
        description: str
            Optional. The scorecard description.
        sensitivityLabelId: str
            Optional. The GUID of a sensitivity label. If you don't want to select a sensitivity label, use a null or empty GUID (00000000-0000-0000-0000-000000000000). If default labels are enabled and/or enforced, they will be applied on the scorecard and dataset.
        ### Returns
        ----
        Dict:
            Response 200. A dict with a new report id.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/scorecards".format(workspace_id)
            body = {"name": name}
            if description != None:
                body["description"]=description
            if sensitivityLabelId != None:
                body["sensitivityLabelId"]=sensitivityLabelId
                
            headers = {'Content-Type': 'multipart/form-data', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers=headers)
            res.raise_for_status()
            
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def delete_scorecard_in_group(self, workspace_id, scorecard_id):
        """Deletes a scorecard by its ID.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        scorecard_id: str uuid
            The Power Bi scorecard id.
        ### Returns
        ----
        Dict:
            A dictionary containing a scorecard in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/scorecards({})".format(workspace_id, scorecard_id)
            res = requests.delete(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

'''
    def move_goals_preview(self, workspace_id, scorecard_id, goalToMove, newNext=None, newParent=None, newPrevious=None):
        """Moves goals within the scorecard. Changes their ranks and parents.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        scorecard_id: str uuid
            The unique identifier of the scorecard
        ### Request Body
        ----
        goalToMove: dict { currentParentId:"str uuid", goalId:"str uuid" }
            The rank validation information for the goal to be moved. The caller provides validation information to confirm that they know the existing position of a goal within the hierarchy of goals.
        newNext: str
            Optional. The rank validation information for the new next-sibling of the goal to be moved. The caller provides validation information to confirm that they know the existing position of a goal within the hierarchy of goals.
        newParent: str
            Optional. The rank validation information for the new previous-sibling of the goal to be moved. The caller provides validation information to confirm that they know the existing position of a goal within the hierarchy of goals.
        newPrevious: str
            
        ### Returns
        ----
        Dict:
            Response 204. 
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/scorecards({})/MoveGoals()".format(workspace_id, scorecard_id)
            body = {"goalToMove": goalToMove}
            if newNext != None:
                body["newNext"]=newNext
            if newParent != None:
                body["newParent"]=newParent
            if newPrevious != None:
                body["newPrevious"]=newPrevious
                
            headers = {'Content-Type': 'multipart/form-data', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers=headers)
            res.raise_for_status()
            
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def patch_goals_preview(self, workspace_id, scorecard_id, goalToMove, newNext=None, newParent=None, newPrevious=None):
        """Updates a scorecard by its ID
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        scorecard_id: str uuid
            The unique identifier of the scorecard
        ### Request Body
        ----
        columnSettings: ScorecardColumnSetting[]	
            The display settings for columns on a scorecard
        createdTime: str
            The UTC time at creation
        datasetId: str
            The ID of the dataset associated with the scorecard
        description: str
            The scorecard description
        goals	Goal[]	The scorecard goals
        groupId: str
            The ID of the workspace
        id: str
            The scorecard ID
        lastModifiedTime: str
            The UTC time at last modification
        name: str
            The scorecard name
        permissions: ScorecardPermission	
            The scorecard permissions
        provisioningStatus: str
            Provisioning status of the scorecard. Supported { Initialized	, Completed, Failed, Deprovisioning, Deleted	 }
        reportId: str
            The ID of the internal report associated with the scorecard            
        ### Returns
        ----
        Dict:
            Response 200. 
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/scorecards({})".format(workspace_id, scorecard_id)
            body = {"goalToMove": goalToMove}
            if newNext != None:
                body["newNext"]=newNext
            if newParent != None:
                body["newParent"]=newParent
            if newPrevious != None:
                body["newPrevious"]=newPrevious
            if newNext != None:
                body["newNext"]=newNext
            if newParent != None:
                body["newParent"]=newParent
            if newPrevious != None:
                body["newPrevious"]=newPrevious
                
            headers = {'Content-Type': 'multipart/form-data', "Authorization": "Bearer {}".format(self.token)}
            res = requests.patch(url, data = json.dumps(body), headers=headers)
            res.raise_for_status()
            
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
'''