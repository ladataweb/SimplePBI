# SimplePBI

This is a simple library that makes it easy to use the Power Bi Admin API. One day SimplePBI will contain all the categories in the Power Bi Rest API (Admin, datasets, reports, etc).
Each category is an Object. This means we need to initialize an object to start using its methods. In order to create them we need the Bearer token that can be obtain from a Token Object. 
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

Datasets_In_Groups = get_datasets_in_group(workspace_id)
```

The library get requests will return a response object .json() that python reads it as a Dict.