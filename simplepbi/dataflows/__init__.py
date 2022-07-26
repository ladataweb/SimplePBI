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

class Dataflows():
    """Simple library to use the Power BI api and obtain dataflows from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request admin API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        """
        self.token = token
               
    def get_dataflow_in_group(self, workspace_id, dataflow_id):
        """Returns a single dataflow from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataflow_id: str uuid
            The Power Bi dataflow id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a dataflow in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}".format(workspace_id, dataflow_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
                    
    def get_dataflows_in_group(self, workspace_id):
        """Returns a list of all dataflows from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the dataflows in the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

            
    def get_datasources_in_group(self, workspace_id, dataflow_id):
        """Returns a list of datasources for the specified dataflow.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataflow_id: str uuid
            The Power Bi dataflow id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the datasources in the dataflow from the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}/datasources".format(workspace_id, dataflow_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

            
    def get_upstream_dataflow_in_group(self, workspace_id, dataflow_id):
        """Returns a list of upstream dataflows for dataflows from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all upstream dataflows in the dataflow from a workspace
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}/upstreamDataflows".format(workspace_id, dataflow_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

                      
    def refresh_dataflow_in_group(self, workspace_id, dataflow_id, notifyOption, processType=None):
        """Triggers a refresh for the specified dataflow. The only supported mail notification options are either in case of failure, or none. MailOnCompletion is not supported.

        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataflow_id: str uuid
            The Power Bi dataflow id. You can take it from PBI Service URL
        processType: str uuid
            Type of refresh process to use.
        ### Request Body
        ----
        notifyOption: NotifyOption str
            Mail notification options (success and/or failure, or none). Options: { MailOnCompletion, MailOnFailure, NoNotification }
        ### Returns
        ----
        Response object from requests library. 202 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}/refreshes".format(workspace_id, dataflow_id)
            if processType != None:
                url = url + "?processType={" + processType + "}"
            body = {
                "notifyOption": notifyOption 
            }               
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, data = json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

                        
    def delete_dataflow_in_group(self, workspace_id, dataflow_id):
        """Deletes the specified dataflow from the specified workspace.
        ### Parameters
        ----
        dataflow_id: str uuid
            The Power Bi dataflow id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}".format(workspace_id, dataflow_id)   
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

                        
    def update_refresh_schedule_in_group_preview(self, workspace_id, dataflow_id, NotifyOption=None, days=None, enabled=None, localTimeZoneId=None, times=None):
        """Creates or updates the specified dataflow refresh schedule configuration.    
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataflow_id: str uuid
            The Power Bi dataflow id. You can take it from PBI Service URL
        ### Request Body
        ----
        NotifyOption: ShceduleNotifyOption str
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
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}/refreshSchedule".format(workspace_id, dataflow_id)
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

            
    def update_dataflow_preview(self, workspace_id, dataflow_id, allowNativeQueries=None, computeEngineBehavior=None, description=None, name=None):
        """Update dataflow properties, capabilities and settings.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataflow_id: str uuid
            The Power Bi dataflow id. You can take it from PBI Service URL
        ### Request Body
        ----
        allowNativeQueries: bool
            Allow native queries
        computeEngineBehavior: str 
            Compute Engine Behavior. Examples: "computeOptimized", "computeOn" or "computeDisabled"
        description: str
            New description for the dataflow
        name: str
            New name for the dataflow
        ### Returns
        ----
        Response object from requests library. 200 OK
        ### Limitations
        ----
        The limit on the number of time slots per day depends on whether a Premium or Shared capacity is used.
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}/refreshSchedule".format(workspace_id, dataflow_id)
            body = {                
            }
            
            if allowNativeQueries != None:
                body["allowNativeQueries"] = allowNativeQueries
            if computeEngineBehavior != None:
                body["computeEngineBehavior"] = computeEngineBehavior
            if description != None:
                body["description"] = description
            if name != None:
                body["name"] = name
                
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            
            res = requests.patch(url, json.dumps(body), headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

            
    def get_dataflow_transaction_in_group(self, workspace_id, dataflow_id):
        """Returns a list of transactions for the specified dataflow.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL
        dataflow_id: str uuid
            The Power Bi dataflow id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the transactions in the dataflow from the workspace.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}/transactions".format(workspace_id, dataflow_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

            
    def cancel_dataflow_transaction_in_group_preview(self, workspace_id, dataflow_id, transaction_id):
        """Attempts to Cancel the specified transactions.
        ### Parameters
        ----
        workspace_id: str uuid
            The Power Bi workspace id. You can take it from PBI Service URL        
        dataflow_id: str uuid
            The Power Bi dataflow id. You can take it from PBI Service URL
        transaction_id: str uuid
            The transaction id. You can get it from get_dataflow_transaction_in_group
        ### Returns
        ----
        Response object from requests library. 202 OK
        
        """
        try: 
            url= "https://api.powerbi.com/v1.0/myorg/groups/{}/dataflows/{}/transactions/{}/cancel".format(workspace_id, dataflow_id, transaction_id)
            if url != None:
                url = url + "?processType={" + processType + "}"           
            headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.post(url, headers = headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
