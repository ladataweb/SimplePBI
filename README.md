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

## Complex requests
If you want to get a deeper look on complex __Admin__ methods. 
<a href="https://github.com/ladataweb/SimplePBI/blob/main/Admin_complex.md" target="_blank">Check this doc</a>

## Current Categories
Right now the library is consuming endpoints from: 
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Admin_details.txt" target="_blank">Admin</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Groups_details.txt" target="_blank">Groups</a>
- <a href="https://github.com/ladataweb/SimplePBI/blob/main/Datasets_details.txt" target="_blank">Datasets</a>

## Missing endpoints
We are still developing the library. The following endpoints from admin are still missing
### Admin 
- Set and Remove LabelsAsAdmin
### Groups
- Update group User
### Datasets
- Bind to gateway (regular and in group)
- Set all datasets connections (regular and in group)
- Update datasources (regular and in group)
- Update Direct Query Refresh Schedule (regular and in group)

## Preview methods
There are some methods in the classes that still need more testing. Those will have a "preview" at the end of the name. Please let us know if something goes wrong with those.



