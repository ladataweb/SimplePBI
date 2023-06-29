# Azure Pause Resume Resources

This section will define specific use for the Library. It shows how to Pause and Resume your Azure resource in order to let you improve your pay as you go license.
The class will have it's own token and login that is restricted to use Service Principal only.
In order to let the Service Principal take adventage of this requests you must first add the add it to the IAM (access control) of the resource(AAS, Fabric or Embedded)

## Auth Azure Resource API 
```python
from simplepbi import azpause
azure = azpause.Azpause(TENANT_ID, client_id, client_secret)
```
This code will create an Azpause object. The object itself contains the params and authentication to request resources. You can find the requests as methods inside the object like it's shown next.

## Resume and Pause resource
```python
azure.resume_resource(subscriptionId, resourceGroupName, resourceType, resourceName)
pause_resource(subscriptionId, resourceGroupName, resourceType, resourceName)
```
This request returns a dict with 202 if the request was correct. You can get your values from your Azure Portal.
Be sure to use the specific word for resourceType. You can use "FABRIC", "PBI" or "AAS" depending if you want to request Fabric, Power Bi Embedded or Azure Analysis Services