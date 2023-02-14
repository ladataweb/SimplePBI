# Admin Power Bi Rest API Requests

This section will define specific complex requests. It won't go one by one the requests explaining their definitions. You can find that when you type the code for it or in the Microsoft Docs for Power Bi Rest API.
If you need any specific detail about a limitations, permissions of your clientId or a request is returning a weird status code or error, please check microsoft documentation first. Validate that you have what you need for the request.

Complex Requests
- Get Activity Events
- Get user Artifact access 
- Scanner API 
- Get Widely Shared Artifacts Published to Web
- Orphan Dataflows

*NOTE: This is the first approach to make it easier for the user playing with the library. We try to handle iterations and responses. There are also some limitations to explain.

## Get Activity Events
```python
get_activity_events_preview(activity_date=None, return_pandas=False)
```
This request returns a dict of audit activity events for a tenant. In order to make it easier to handle it contains a parameter to specify a single DAY. The original API params would be start and end date. This method will cover the whole specified day. If there is no day specify as a parameter, it will return the activity eventos for "Yesterday". It is using the Datetime library to get yesterday.
The activities are also paginated by the original API. The request will handle the pagination automatically returning the whole day. This means that it can take a while to respond.
There is a big limitation for this method. There is a maximum of 200 requests per hour. If you are getting that reach, it will send a 429 Error. Please notify the issue so we can take a look on how to handle this (getting back to star and end params)
Finally there is an special param to adjust the response. You can check return_pandas to True if you want a complete dataframe ready to be inserted somewhere or to be analyzed. By default it is in False returning a dict in case you want to handle it by yourself.

## Get User Artifact Access
```python
get_user_artifact_access_preview(userGraphId, return_pandas=False)
```
This request returns a dict of artifacts that the given user have access to. 
The artifacts are paginated by the original API. The request will handle the pagination automatically returning the whole access list. This means that it can take a while to respond.
There is a big limitation for this method. There is a maximum of 200 requests per hour. If you are getting that reach, it will send a 429 Error. Please notify the issue so we can take a look on how to handle this.
Finally there is an special param to adjust the response. You can check return_pandas to True if you want a complete dataframe ready to be inserted somewhere or to be analyzed. By default it is in False returning a dict in case you want to handle it by yourself.

## Scanner API
This sections is dedicated to review how to get the values of Power Bi Tenant as a single big dict response. 
Be sure to read this realease notes to configure what you need to start with this: https://powerbi.microsoft.com/en-my/blog/announcing-scanner-api-admin-rest-apis-enhancements-to-include-dataset-tables-columns-measures-dax-expressions-and-mashup-queries/
Let's start with the order of the requests we have created to make it the easier we can.

### 1- Get the workspaces you want to track
```python
get_modified_workspaces_preview(excludePersonalWorkspaces=True, modifiedSince=None)
```
Gets a list of workspace IDs in the organization. Due to the fact that the next requests in the path can only handle 100 groups by request, the reponse for this first step is a list of lists. 
The response is a list of lists with 100 groups. It will automatically prepare the list o lists so you can later loop the next steps by your self.
Remember you can check the length of a list like 
```python
# Check the number of lists of 100 workspaces.
len(response)
# Print workspaces, 0 is an example of the first list of hundreads
response[0]
```

### 2- Post Workspace info
```python
post_workspace_info(workspaces, lineage=True, datasourceDetails=True, datasetSchema=True, datasetExpressions=True, getArtifactUsers=True)
```
Return a Scan ID in UUID format. Initiates a call to receive metadata for the requested list of workspaces. The workspaces param is a list of maximum 100 workspaces. You can run this request looping the list of lists from the previous response.
By default it will return all possible data. You can change to false the params in the method detail that you don't want.

### 3- Get Scan Status
```python
get_scan_status_preview(scan_id)
```
Gets the scan status for the specified scan. Before getting the whole structure for the 100 workspaces we need to ask the API to approve the scan.
This request will return the same id and a status. If the reponse for the status is "Succeeded", you can complete the scanner request in the last step. If not, then wait and try it later.

### 4- Get Scan result
```python
get_scan_result_preview(scan_id)
```
Gets the scan result for the specified scan id. This request will finally return an enormous python dictionary with all the data we requested for the 100 workspaces listed for the scan.
If you can't handle the dict check the following method.

### Aditional method to help handle 
There is an aditional section in the library that will help us handling reponses. You can get it like this:
```python
from simplepbi import utils
```
In this particular case there is a request to capture a single type of artifact in the scan result. Like "reports".
```python
get_artifact_from_scan_preview(scan_result, artifact)
```
The request will demand as param the result of the scan. The big dict is received and the method will try to capture the artifact type for you so you can Get a table of an specific artifact.
Artifacts are key components that you can check reading the scan result like "reports" or "datasets".
Utils is not an object, so you can just write:
```python
utils.get_artifact_from_scan_preview(scan_result, artifact="reports")
```

### Get Widely Shared Artifacts Published to Web
```python
get_widely_shared_artifacts_published_to_web()
```
This request returns a dict of published to web reports over the tenant. It has been made easier for you. The method contains a solution for pagination that will loop over the pages with the continuation token resulting on a big dict with all reports.

## Get Orphan Dataflows
```python
get_orphan_dataflows_preview()
```
We wanted to help getting a common requirement in Power bi Community building this new method.
It returns a list of dataflows ids in UUID format that are not connected from any dataset. We are calling those "Orphan dataflows".
The request will build everything automatically. Getting the workspace and exploring dataflows connected to datasets in order to show the ids of those that are not used.
There is a big limitation for this method. There is a maximum of 200 requests per hour. This means that if you have more than 200 workspaces created, you can't use this request. If you are getting that reach, it will send a 429 Error. Please notify the issue so we can take a look on how to handle this (getting back to star and end params)



