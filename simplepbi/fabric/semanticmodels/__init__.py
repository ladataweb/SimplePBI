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
import re
import base64
class SemanticModels():
    """Simple library to use the api and obtain semantic models item from it.
    """

    def __init__(self, token):
        """Create a simplePBI object to request fabric semantic models item API
        Args:
            token: String
                Bearer Token to use the Rest API
        """
        self.token = token

    # Get semantic model in Workspace
    def get_semantic_model(self, workspace_id, semantic_model_id):
        """Returns properties of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing a semantic model in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/semanticModels/{}".format(workspace_id, semantic_model_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # List semantic models in Workspace
    def list_semantic_models(self, workspace_id):
        """Returns a list of semantic models in the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        ### Returns
        ----
        Dict:
            A dictionary containing all the semantic models in the workspace.
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/semanticModels".format(workspace_id)
            res = requests.get(url, headers={'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)})
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)

    # Delete semantic model in Workspace
    def delete_semantic_model(self, workspace_id, semantic_model_id):
        """Deletes the specified semantic model from the specified workspace.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        Response object from requests library. 200 OK
        """
        try:
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/semanticModels/{}".format(workspace_id, semantic_model_id)
            headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}
            res = requests.delete(url, headers=headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as ex:
            print("HTTP Error: ", ex, "\nText: ", ex.response.text)
        except requests.exceptions.RequestException as e:
            print("Request exception: ", e)
    # Create semantic model in Workspace
    
    def get_semantic_model_definition(self, workspace_id, semantic_model_id, format=None):
        """Returns the definition of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        format: str
            The format of the semantic model definition. Can be 'TMDL' or 'TMSL'.
        ### Returns
        ----
        Dict:
            A dictionary containing the definition of the semantic model.
        """
        try:
            op = LongRunningOperations(self.token)
            url = "https://api.fabric.microsoft.com/v1/workspaces/{}/semanticModels/{}/getDefinition".format(workspace_id, semantic_model_id)
            if format != None:
                url += "?format={}".format(format)
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

    def list_roles_from_semantic_model(self, workspace_id, semantic_model_id):
        """Returns the roles of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        DataFrame:
            A list containing the roles of the semantic model.
        """
        try:
            model = self.get_semantic_model_definition(workspace_id, semantic_model_id,"TMDL")
            for i in model["definition"]["parts"]:
                if "model.tmdl" in i["path"]:
                    metad = i["payload"]
            decoded_contents = base64.b64decode(metad.encode("utf-8"))
            decoded_str = decoded_contents.decode("utf-8")
            roles = [role.strip().strip("'\"") for role in re.findall(r'^\s*ref role (.+)$', decoded_str, re.MULTILINE)]
            if roles == []:
                print("No roles found in the semantic model.")
            return roles
        except Exception as e:
            print("Error while getting roles: ", e)
    def list_tables_from_semantic_model(self, workspace_id, semantic_model_id):
        """Returns the tables of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        DataFrame:
            A list containing the tables of the semantic model.
        """
        try:
            model = self.get_semantic_model_definition(workspace_id, semantic_model_id,"TMDL")
            for i in model["definition"]["parts"]:
                if "model.tmdl" in i["path"]:
                    metad = i["payload"]
            decoded_contents = base64.b64decode(metad.encode("utf-8"))
            decoded_str = decoded_contents.decode("utf-8")
            tablas = [tabla.strip().strip("'\"") for tabla in re.findall(r'^\s*ref table (.+)$', decoded_str, re.MULTILINE)]
            if tablas == []:
                print("No tables found in the semantic model.")
            return tablas
        except Exception as e:
            print("Error while getting tables: ", e)
    
    def get_tables_schema_from_semantic_model(self, workspace_id, semantic_model_id):
        """Returns the tables schema of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        DataFrame:
            A pandas DataFrame containing the tables of the semantic model.
        """
        try:
            model = self.get_semantic_model_definition(workspace_id, semantic_model_id, "TMDL")
            tables = [base64.b64decode(i["payload"].encode("utf-8")).decode("utf-8") for i in model["definition"]["parts"] if "tables" in i["path"]]
            # Append all tables into a single string
            decoded_str = "\n".join(tables)
            return utils.parse_tmdl_structure(decoded_str)
        except Exception as e:
            print("Error while getting tables: ", e)

    def get_tables_partitions_from_semantic_model(self, workspace_id, semantic_model_id):
        """Returns the tables partitions of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        DataFrame:
            A pandas DataFrame containing the tables of the semantic model.
        """
        try:
            model = self.get_semantic_model_definition(workspace_id, semantic_model_id, "TMDL")
            tables = [base64.b64decode(i["payload"].encode("utf-8")).decode("utf-8") for i in model["definition"]["parts"] if "tables" in i["path"]]
            # Append all tables into a single string
            decoded_str = "\n".join(tables)             
            # Find all tables and their partitions with M code
            table_blocks = re.findall(
                r'table\s+([^\s]+)(.*?)partition\s+\1-[\w-]+.*?=\s*m\s+.*?source\s*=\s*(let\s+.*?in\s+.*?)(?=\n\t*annotation|\n\s*$)',
                decoded_str,
                flags=re.DOTALL,
            )

            # Build list of dicts
            records = []
            for table_name, _, m_code in table_blocks:
                records.append({
                    "table_name": table_name.strip(),
                    "m_code": m_code.strip()
                })
            df = pd.DataFrame(records)
            df.rename(columns={"table_name": "table", "m_code": "query_definition"}, inplace=True)
            return df
        except Exception as e:
            print("Error while getting tables: ", e)
    
    def get_relationships_from_semantic_model(self, workspace_id, semantic_model_id):
        """Returns the relationships of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        DataFrame:
            A pandas DataFrame containing the relationships of the semantic model.
        """
        try:
            model = self.get_semantic_model_definition(workspace_id, semantic_model_id, "TMDL")
            for i in model["definition"]["parts"]:
                if "relationships.tmdl" in i["path"]:
                    relations = i["payload"]
            relationships = base64.b64decode(relations.encode("utf-8")).decode("utf-8")
            return utils.extract_relationships(relationships)
        except Exception as e:
            print("Error while getting relationships: ", e)

    def get_semantic_model_bim(self, workspace_id, semantic_model_id):
        """Returns the model.bim of the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        ### Returns
        ----
        DataFrame:
            A pandas DataFrame containing the bim of the semantic model.
        """
        try:
            model = self.get_semantic_model_definition(workspace_id, semantic_model_id, "TMSL")
            for i in model["definition"]["parts"]:
                if "model.bim" in i["path"]:
                    datamodel = i["payload"]
            decoded_contents = base64.b64decode(datamodel.encode("utf-8"))            
            return json.loads(decoded_contents)
        except Exception as e:
            print("Error while getting bim file: ", e)

    def create_html_semantic_model_documentation(self, workspace_id, semantic_model_id, output_html_path):
        """Generates an HTML documentation for the specified semantic model.
        ### Parameters
        ----
        workspace_id: str uuid
            The workspace id. You can take it from PBI Service URL
        semantic_model_id: str uuid
            The semantic model id. You can take it from PBI Service URL
        output_html_path: str
            The path where the HTML documentation will be saved.
            E.g: C:\\Users\\user\\Desktop\\semantic_model_documentation.html
        ### Returns
        ----
        None
        """
        try:
            print("Getting semantic model info...")
            bim = self.get_semantic_model_bim(workspace_id, semantic_model_id)            
            print("Generating file...")
            utils.generate_bim_documentation(json.dumps(bim), output_html_path)            
            print("Documentation generated successfully at: ", output_html_path)
        except Exception as e:
            print("Error while generating HTML documentation: ", e)