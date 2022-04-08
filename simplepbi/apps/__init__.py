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

class Apps():
    """Simple library to use the Power BI api and obtain apps from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request app API
        Args:
            token: String
                Bearer Token to use the Power Bi Rest API
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        self.token = token
        
    def get_app(self, app_id):
        """Returns the specified installed app.
        ### Parameters
        ----
        app_id: str uuid
            The Power Bi app id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing the specified installed app.
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/apps/{}".format(app_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_apps(self):
        """Returns a list of installed apps.
        ### Parameters
        ----
        None
        ### Returns
        ----
        Dict:
            A dictionary containing all the installed apps.
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/apps"
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
    
    def get_dashboard(self, app_id, dashboard_id):
        """Returns the specified dashboard from the specified app.
        ### Parameters
        ----
        app_id: str uuid
            The Power Bi app id. You can take it from PBI Service URL
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a dashboard in the specified app.
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/apps/{}/dashboards/{}".format(app_id, dashboard_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_dashboards(self, app_id):
        """Returns a list of dashboards from the specified app.
        ### Parameters
        ----
        app_id: str uuid
            The Power Bi app id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the dashboards in the specified app
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/apps/{}/dashboards".format(app_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_report(self, app_id, report_id):
        """Returns the specified report from the specified app.
        ### Parameters
        ----
        app_id: str uuid
            The Power Bi app id. You can take it from PBI Service URL
        report_id: str uuid
            The Power Bi report id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a report in the specified app.
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/apps/{}/reports/{}".format(app_id, report_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
    def get_reports(self, app_id):
        """Returns a list of reports from the specified app.
        ### Parameters
        ----
        app_id: str uuid
            The Power Bi app id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the reports in the specified app
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/apps/{}/reports".format(app_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    def get_tile(self, app_id, dashboard_id, tile_id):
        """Returns the specified tile within the specified dashboard from the specified app.
        Supported tiles include datasets and live tiles that contain an entire report page.
        ### Parameters
        ----
        app_id: str uuid
            The Power Bi app id. You can take it from PBI Service URL
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        tile_id: str uuid
            The tile id
        ### Returns
        ----
        Dict:
            A dictionary containing a tile in dashboard from the specified app.
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/apps/{appId}/dashboards/{}/tiles/{}".format(app_id, dashboard_id, tile_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
           
    def get_tiles(self, app_id, dashboard_id):
        """Returns a list of tiles within the specified dashboard from the specified app.
        ### Parameters
        ----
        app_id: str uuid
            The Power Bi app id. You can take it from PBI Service URL
        dashboard_id: str uuid
            The Power Bi dashboard id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the tiles in a dashboard from the specified app.
        ### Limitations
        ----
        Service principal authentication isn't supported.
        """
        try:
            url = "https://api.powerbi.com/v1.0/myorg/apps/{appId}/dashboards/{}/tiles".format(app_id, dashboard_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
            
