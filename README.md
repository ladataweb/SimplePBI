# SimplePBI

This is a simple library that makes it easy to use the Power Bi REST API. One day SimplePBI will contain all the categories in the API (Admin, datasets, reports, etc).
Feel free to check the doc to get a deeper understanding of a specific request: https://docs.microsoft.com/en-us/rest/api/power-bi/
<br>We are doing our best to make this library useful for the community. This project is not a remunerable job for us. It's a public community project. Please be patient if you submit an issue and it's not fixed right away. It's a way to express our passion of sharing knowledge.
<br>Each category is an Object. This means we need to initialize an object to start using its methods. In order to create them we need the Bearer token that can be obtain from a Token Object. 
Let's see how we can create an Admin Object to try the requests in that category.

```python
# Import library
from simplepbi import token
from simplepbi import admin
```

We always need to import token object to create the object to run requests. Then we can pick the object of the Power Bi Rest API category we need. For instance "admin".
The token can be created in two ways, the regular authentication and the service principal one. It depends which one you pick to complete the request. 
These are the necessary arguments to get a token:
- tenant_id (you can get it from subscription resource in azure portal or ask for it to the IT department)
- app_client_id (your app_id/client_id from the App registered in Azure with permissions to Power Bi Service)
- username (professional email account in Azure AD)
- password (professional password)
- app_secret_key (secret key generated for the client id)
- use_service_principal (True to athenticate with Service Principal and False to continue with user credentials)


*NOTE: if you want to use service principal, be sure to have your tenant ready for that.
<br>Register app example: https://blog.ladataweb.com.ar/post/188045227735/get-access-token
<br>Service Principal permissions for admin api: https://docs.microsoft.com/en-us/power-bi/admin/read-only-apis-service-principal-authentication*


```python
# Creating objects

#Regular Login
tok = token.Token(tenant_id, app_client_id, username, password, None, use_service_principal=False)

#Service Principal
tok = token.Token(tenant_id, app_client_id, None, None, app_secret_key, use_service_principal=True)

ad = admin.Admin(tok.token)
```

As you can see the Token object contains a token attribute with the Bearer used by Azure to run rest methods. That attribute will be user to create the category objects like admin.
Once we create our Object like admin, we can start using the requests adding the correct parameters if they are needed.

```python
# Getting objects

All_Datasets = ad.get_datasets()

Datasets_In_Groups = ad.get_datasets_in_group(workspace_id)
```

The library get requests will return a response object .json() that python reads it as a Dict.

## Preview methods
There are some methods in the classes that still need more testing. Those will have a "preview" at the end of the name. Please let us know if something goes wrong with those.

## Current Categories
Right now the library is consuming endpoints from: 
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Admin_details.txt" target="_blank">Admin</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Groups_details.txt" target="_blank">Groups</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Datasets_details.txt" target="_blank">Datasets</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Dataflows_details.txt" target="_blank">Dataflows</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Reports_details.txt" target="_blank">Reports</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Dashboards_details.txt" target="_blank">Dashboards</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Apps_details.txt" target="_blank">Apps</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Imports_details.txt" target="_blank">Imports</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Gateways_details.txt" target="_blank">Gateways</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Capacities_details.txt" target="_blank">Capacities</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Pipelines_details.txt" target="_blank">Pipelines (Preview)</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Scorecards_details.txt" target="_blank">Scorecards (Preview)</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Az_Pause_Resume_details.txt" target="_blank">Azure Pause and Resume resource (Preview)</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Push_Datasets_details.txt" target="_blank">Push Datasets</a>

## Complex requests
If you want to get a deeper look on complex __Admin__ methods and unique methods. 
<a href="https://github.com/ladataweb/SimplePBI/blob/main/Admin_complex.md" target="_blank">Check this doc</a>

## Azure Pause Resume Resources
We have added a new feature to include some Azure Resource API Manager. The new "azpause" class will let you Pause or Resume Azure tabular or capacity resources. With SimplePBI you can pause and resume Fabric, Power Bi Embedded or Azure Analysis Services resources.
<a href="https://github.com/ladataweb/SimplePBI/blob/main/AzPauseResume.md" target="_blank">Check this doc</a>

## Additional content
There an aditional library Utils for transformations. It is used to help some requests returning different values.
The most useful method in the Utils class might be to_pandas. You can use the method to convert simple dicts to pandas. It needs the dict and the key father of a list of dicts in the response. The usual get responses are using "value" as the key.
We are also adding new methods with the requests to help get new actions. Examples:

### Example of our amazing unique requests
- get_orphan_dataflows_preview: get dataflows without dataset
- simple_import_pbix: makes publishing a pbix file easier
- simple_import_pbix_as_parameter: import a pbix from api response content
- simple_import_pbix_folder_in_group_preview: post a all pbix files in a local folder
- simple_import_from_devops: import a pbix from azure devops repo
- simple_import_from_github: import a pbix from azure github repo
- simple_copy_reports_between_groups: copy report from workspace to a workspace
- enhanced_refresh_dataset_in_group: a special request feature that not only eliminates the need for synchronous client connections to perform a refresh, but also unlocks enterprise-grade refresh capabilities.
- get_activity_events_preview (already iterating): makes the get activity events specified by date easier
- get_user_artifact_access_preview (already iterating): makes the get user artifact access easier
- get_widely shared_artifacts_published_to_web (already iterating): makes geting the published to web repos info easier
- get_tables_from_dataset_in_group: get the tables names and other data columns in the semantic model from specific workspace 
- get_measures_from_dataset_in_group: get the measures names and other data columns in the semantic model from specific workspace 
- get_columns_from_dataset_in_group: get the columns names and other data columns in the semantic model from specific workspace 
- get_tables_from_dataset_in_group: get the roles names and other data columns in the semantic model from specific workspace. The request only works with User and Passworkd credentials. Service Principal won't work due to API limitations.
- get_dataset_roles_in_group: get all the roles from a single dataset in a specific workspace
- get_datasets_roles_in_groups: get all the roles from all datasets in a list of workspaces
- create_doc_by_content_dataset_in_group: generate an html code file or text with a document of semantic model in a workspace organized by content
- create_doc_by_table_dataset_in_group: generate an html code file or text with a document of semantic model in a workspace organized by tables

## Small categories
Small categories like Dataflow Storage Accounts and Available Features were moved to Groups and Admin.

# Missing endpoints
We are still developing the library. The following endpoints from admin are still missing
### Admin 
- Set and Remove LabelsAsAdmin
### Groups
- Update group User
### Reports
- Export To File (full request, there is a smaller simpler one)
- Get Export To File Status (regular and in groups)
- Get File Of Export To File (regular and in groups)
- Update Datasources (rdl files regular and in groups)
- Update Report Content (regular and in groups)
### Imports
- Create Temporary Upload Location
- Create Temporary Upload Location In Group
- Post Import (for xlsx, json and rdl)
- Post Import In Group (for xlsx, json and rdl)
### Gateways 
- Create Datasource (looks like there is a bug on the API)
- Update Datasource 
- Delete Datasource 
### Scorecards (preview)
- Patch By Id 
- Move Goals
### Embed Token
- All requests 
### Goals (preview)
- All requests

# Next Steps (planned items)
- Creating new awesome ideas.
- Keep completing missing endpoints category.
- Analyzing how to include embeding and Fabric requests.


