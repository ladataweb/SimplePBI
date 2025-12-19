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
@........|____| |  | |...*   *.@    Copyright © 2022 Ignacio Barrau
@   .       . | |__| |. *     *@
@   .       . |_____/ . *     *@    *********************************************
@   .       .         . *     *@
@   .       .         . *******@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''

import json
import pandas as pd
import io
import re
import os
import base64
from typing import Dict, Any

'''
class Utils():
    """Simple library class."""
    
    def __init__(self):
        """Class with useful methods."""
    '''
    
def append_value(dict_obj, key, value):
    '''
    Parameters
    ----------
    dict_obj : dict
        dictionary object to append values.
    key : str
        Key name of the dictonary that will append a value.
    value : any
        Value to append in the key of the dictionary.

    Returns
    -------
    None. It is applied to the dict in the parameter
    '''
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
            # Append the value in list
            dict_obj[key].append(value)
        else:
            # As key is not in dict,
            # so, add key-value pair
            dict_obj[key] = value
    
def to_pandas(response_dict, father_node):
    '''
    Parameters
    ----------
    response_dict : dict
        response from methods.
    father_node : TYPE
        Dict Key involving the list [] of items. Example for get_dashboards, the key of the response is "value"
        {
          "value": [
            {
              "id": "69ffaa6c-b36d-4d01-96f5-1ed67c64d4af",
              "displayName": "SalesMarketing",
              "embedUrl": "https://app.powerbi.com/dashboardEmbed?dashboardId=69ffaa6c-b36d-4d01-96f5-1ed67c64d4af&groupId=f089354e-8366-4e18-aea3-4cb4a3a50b48",
              "isReadOnly": false
            }
          ]
        }

    Returns
    -------
    df : Pandas DataFrame
        Returns the dict response converted in a Pandas DataFrame.
    '''
    js = json.dumps(response_dict[father_node])
    df = pd.read_json(io.StringIO(js))
    return df 

def get_artifact_from_scan_preview(scan_result, artifact):
    """Get a table of an specific artifact
    ### Parameters
    ----
    scan_result: dict
        The scan result response from get_scan_result_preview
    artifact: str
        The type of artifact. Types: 'reports', 'dashboards', 'datasets', 'dataflows', 'users'
    ### Returns
    ----
    str:
        Returns the status of the scan. Succeeded means you are ready to request scans.
    """
    df_total = pd.DataFrame()
    try:        
        for group in scan_result["workspaces"]:
            df = pd.read_json(json.dumps(group[artifact]))
            df["workspaceId"] = group["id"]
            df_total = pd.concat([df_total, df], sort=True, ignore_index=True)
        return df_total
    except Exception as e:
        print("ERROR: ", e)

def extract_relationships(relationships_text):
    """
    Parses TMDL-formatted relationship definitions into a structured DataFrame.
    ### Parameters
    ----
    relationships_text: str
        The TMDL-formatted string containing relationship definitions.
    ### Returns
    ----
    DataFrame:
        A pandas DataFrame with columns: fromTable, fromColumn, toTable, toColumn.
    """
    relationships = []
    current_from = None
    current_to = None

    lines = relationships_text.splitlines()
    for line in lines:
        line = line.strip()

        if line.startswith("fromColumn:"):
            from_full = line.split(":", 1)[1].strip()
            if '.' in from_full:
                from_table, from_column = from_full.split('.', 1)
            else:
                from_table, from_column = None, from_full

        elif line.startswith("toColumn:"):
            to_full = line.split(":", 1)[1].strip()
            if '.' in to_full:
                to_table, to_column = to_full.split('.', 1)
            else:
                to_table, to_column = None, to_full

            # Append relationship once both from and to are found
            relationships.append({
                "fromTable": from_table.strip("'\""),
                "fromColumn": from_column.strip("'\""),
                "toTable": to_table.strip("'\""),
                "toColumn": to_column.strip("'\"")
            })

    return pd.DataFrame(relationships)    

def parse_tmdl_structure(table_definition):
    """
    Parses a TMDL-format semantic model tables definition into a structured DataFrame.
    Extracts table name, field name, data type, and DAX expression.
    ### Parameters
    ----
    table_definition: str
        The TMDL-formatted string containing table definitions.
    ### Returns
    ----
    DataFrame:
        A pandas DataFrame with columns: table, name, type, data_type, expression.
    """
    current_table = None
    records = []
    lines = table_definition.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Detect table
        table_match = re.match(r'^table\s+(.+)', line)
        if table_match:
            current_table = table_match.group(1).strip()
            i += 1
            continue

        # Detect measure
        measure_match = re.match(r"^measure\s+'?([^']+)'?\s*=\s*(.*)", line)
        if measure_match:
            measure_name = measure_match.group(1).strip()
            dax_expr = measure_match.group(2).strip()

            
            # If expression starts with triple backticks
            if dax_expr.startswith("```"):
                dax_lines = []
                i += 1
                while i < len(lines):
                    next_line = lines[i].strip()
                    if next_line == "```":
                        break
                    dax_lines.append(next_line)
                    i += 1
                dax_expr = "\n".join(dax_lines)
                i += 1  # Skip closing ```
            else:
                # Collect until next metadata or definition
                while i + 1 < len(lines):
                    peek = lines[i + 1].strip()
                    if peek.startswith(("formatString", "lineageTag", "annotation", "measure", "column", "table")):
                        break
                    i += 1
                    dax_expr += " " + lines[i].strip()


            records.append({
                'table': current_table,
                'name': measure_name,
                'type': 'measure',
                'data_type': None,
                'expression': dax_expr
            })
            i += 1
            continue

        # Detect column
        column_match = re.match(r"^column\s+'?([^'=]+?)'?(?:\s*=\s*(.+))?$", line)
        if column_match:
            col_name = column_match.group(1).strip()
            expression = column_match.group(2).strip() if column_match.group(2) else None
            data_type = None

            i += 1
            # Look ahead for dataType and other metadata
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith("dataType:"):
                    data_type = next_line.replace("dataType:", "").strip()
                elif next_line.startswith(("lineageTag:", "formatString", "summarizeBy", "annotation", "dataCategory", "sourceColumn:")):
                    pass  # Ignore other metadata for now
                elif next_line.startswith(("column", "measure", "partition", "table")):
                    break
                i += 1

            records.append({
                'table': current_table,
                'name': col_name,
                'type': 'column',
                'data_type': data_type,
                'expression': expression
            })
            continue

        i += 1

    return pd.DataFrame(records)

def parse_measure(measure: Dict[str, Any]) -> str:
    """    Parses a measure definition into an HTML representation.
    ### Parameters  
    ----
    measure: dict
        A dictionary containing measure details with keys like 'name', 'expression', 'formatString', and 'description'.
    ### Returns
    ----
        str: An HTML representation of the measure.
    """
    expr = measure.get("expression", "")
    if isinstance(expr, list):
        expr = "\n".join(expr)
    return f"""
    <details class="measure-section">
      <summary>{measure.get('name')}</summary>
      <div><b>Expression:</b><pre>{expr}</pre></div>
      <div><b>Format:</b> {measure.get('formatString', '')}</div>
      <div><b>Description:</b> {measure.get('description', '')}</div>
    </details>
    """

def parse_partition(partition: Dict[str, Any]) -> str:
    """    Parses a partition definition into an HTML representation.
    ### Parameters
    ----
    partition: dict
        A dictionary containing partition details with keys like 'name', 'mode', 'queryGroup', and 'source'.
    ### Returns
    ----
        str: An HTML representation of the partition.
    """
    source = partition.get('source', {}).get('expression', '')
    if isinstance(source, list):
        source = "\n".join(source)
    return f"""
    <details class="partition-section">
      <summary>{partition.get('name')}</summary>
      <div><b>Mode:</b> {partition.get('mode', '')}</div>
      <div><b>Query Group:</b> {partition.get('queryGroup', '')}</div>
      <div><b>Source Expression:</b><pre class="language-js"><code class="language-js">{source}</code></pre></div>
    </details>
    """

def parse_role(role: Dict[str, Any]) -> str:
    """    Parses a role definition into an HTML representation.
    ### Parameters
    ----
    role: dict
        A dictionary containing role details with keys like 'name', 'modelPermission', and 'tablePermissions'.
    ### Returns
    ----
        str: An HTML representation of the role.
    """
    perms = role.get('modelPermission', '')
    table_perms = ""
    for tp in role.get("tablePermissions", []):
        if 'filterExpression' not in tp.keys():
            tp['filterExpression'] = "<em>No filter</em>"
        table_perms += f"<li>{tp['name']}: {tp['filterExpression']}</li>"
    return f"""
    <details class="role-section">
      <summary>{role.get('name')} <span class="badge">{perms}</span></summary>
      <ul>{table_perms}</ul>
    </details>
    """

def parse_columns_table(columns) -> str:
    """    Parses a list of column definitions into an HTML table.
    ### Parameters  
    ----
    columns: list
        A list of dictionaries, each representing a column with keys like 'name', 'dataType', 'formatString', and 'description'.
    ### Returns
    ----
        str: An HTML representation of the columns in a table format.   
    """
    if not columns:
        return "<em>No columns</em>"
    out = ['<table class="columns-table"><thead><tr><th>Name</th><th>Data Type</th><th>Format</th><th>Description</th></tr></thead><tbody>']
    for col in columns:
        out.append(
            f"<tr>"
            f"<td><b>{col.get('name')}</b></td>"
            f"<td>{col.get('dataType','')}</td>"
            f"<td>{col.get('formatString','')}</td>"
            f"<td>{col.get('description','')}</td>"
            f"</tr>"
        )
    out.append('</tbody></table>')
    return "\n".join(out)

def parse_table(table: Dict[str, Any]) -> str:
    """    Parses a table definition into an HTML representation.
    ### Parameters
    ----
    table: dict
        A dictionary containing table details with keys like 'name', 'columns', 'measures', and 'partitions'.
    ### Returns 
    ----
        str: An HTML representation of the table, including its columns, measures, and partitions.
    """
    columns_html = parse_columns_table(table.get("columns", []))
    measures_html = "".join([parse_measure(m) for m in table.get("measures", [])])
    partitions_html = "".join([parse_partition(p) for p in table.get("partitions", [])])
    anchor = f"table-{table.get('name').replace(' ', '_')}"
    return f"""
    <section class="table-card" id="{anchor}">
      <h2>{table.get('name')}</h2>
      <div class="table-section">
        <h3>Columns</h3>
        {columns_html}
        <details>
          <summary>Measures ({len(table.get('measures', []))})</summary>
          <div>{measures_html or "<em>No measures</em>"}</div>
        </details>
        <details>
          <summary>Partitions ({len(table.get('partitions', []))})</summary>
          <div>{partitions_html or "<em>No partitions</em>"}</div>
        </details>
      </div>
    </section>
    """

def parse_relationship(rel: Dict[str, Any]) -> str:
    """    Parses a relationship definition into an HTML representation.
    ### Parameters
    ----
    rel: dict
        A dictionary containing relationship details with keys like 'fromTable', 'fromColumn', 'toTable', 'toColumn', and 'cardinality'.
    ### Returns
    ----
        str: An HTML representation of the relationship, including the tables and columns involved, and the cardinality.
    """
    cardinality = rel.get('cardinality') or 'Unknown'
    return (f"<li><b>{rel['fromTable']}.{rel['fromColumn']}</b> "
            f"<span class='arrow'>&#8594;</span> "
            f"<b>{rel['toTable']}.{rel['toColumn']}</b> "
            f"<span class='cardinality'>[{cardinality}]</span></li>")

def parse_config(model: Dict[str, Any], bim: Dict[str, Any]) -> str:
    """    Parses the model configuration into an HTML representation.
    ### Parameters
    ----
    model: dict
        A dictionary containing model details with keys like 'culture', 'sourceQueryCulture', and 'annotations'.
    bim: dict
        A dictionary containing the entire BIM structure, which may include additional metadata.    
    ### Returns
    ----
        str: An HTML representation of the model configuration, including compatibility level, culture, and annotations.
    """
    compatibility_level = bim.get('compatibilityLevel') or model.get('compatibilityLevel', '')
    annos = model.get("annotations", [])
    annos_html = ""
    for a in annos:
        if a['name'] == "PBI_QueryOrder":
            continue  # skip long query order annotation
        annos_html += f"<li><b>{a['name']}</b>: {a['value']}</li>"
    return f"""
    <section class="config-section">
      <h2>Model Configuration</h2>
      <ul>
        <li><b>Compatibility Level:</b> {compatibility_level}</li>
        <li><b>Culture:</b> {model.get('culture', '')}</li>
        <li><b>Source Query Culture:</b> {model.get('sourceQueryCulture', '')}</li>
        {annos_html}
      </ul>
    </section>
    """

def generate_index_of_tables(tables) -> str:
    """    Generates an HTML representation of an index of tables, with links to each table's section.
    ### Parameters
    ----
    tables: list
        A list of dictionaries, each representing a table with a 'name' key.
    ### Returns
    ----
        str: An HTML representation of the index of tables, with links to each table's section.
    """
    items = []
    for t in tables:
        anchor = f"table-{t.get('name').replace(' ', '_')}"
        items.append(f'<li><a href="#{anchor}">{t.get("name")}</a></li>')
    return f"""
    <nav class="table-index">
      <h2>Tables Index</h2>
      <ul>
        {''.join(items)}
      </ul>
    </nav>
    """

def generate_cytoscape_diagram(tables, relationships):
    """    Generates an HTML representation of a data model diagram using Cytoscape.js.
    ### Parameters
    ----
    tables: list
        A list of dictionaries, each representing a table with a 'name' key.
    relationships: list
        A list of dictionaries, each representing a relationship with keys like 'fromTable', 'fromColumn', 'toTable', 'toColumn', and 'cardinality'.
    ### Returns
    ----
        str: An HTML representation of the data model diagram, including nodes for tables and edges for relationships.
    """ 
    cytoscape_nodes = []
    cytoscape_edges = []
    for t in tables:
        cytoscape_nodes.append({
            "data": {
                "id": t['name'],
                "label": t['name']
            }
        })
    for rel in relationships:
        cardinality = rel.get('cardinality') or "Unknown"
        cytoscape_edges.append({
            "data": {
                "id": f"{rel['fromTable']}__{rel['toTable']}__{rel['fromColumn']}",
                "source": rel['fromTable'],
                "target": rel['toTable'],
                "label": f"{rel['fromColumn']} → {rel['toColumn']} [{cardinality}]"
            }
        })
    js_nodes = json.dumps(cytoscape_nodes)
    js_edges = json.dumps(cytoscape_edges)
    return f"""
    <section class="diagram-section">
      <h2>Data Model Diagram</h2>
      <div id="model-diagram" style="width:100%;min-height:350px;height:470px;border:1px solid #e0e5ea;border-radius:8px;background:#fafcff;"></div>
      <script src="https://unpkg.com/cytoscape/dist/cytoscape.min.js"></script>
      <script>
        var cy = cytoscape({{
          container: document.getElementById('model-diagram'),
          elements: {{
            nodes: {js_nodes},
            edges: {js_edges}
          }},
          style: [
            {{
              selector: 'node',
              style: {{
                'label': 'data(label)',
                'background-color': '#0078d4',
                'color': '#fff',
                'font-size': '14px',
                'text-valign': 'center',
                'text-halign': 'center',
                'width': 95,
                'height': 95,
                'shape': 'round-rectangle',
                'border-width': 2,
                'border-color': '#004578',
                'text-wrap': 'ellipsis',
                'text-max-width': 80
              }}
            }},
            {{
              selector: 'edge',
              style: {{
                'curve-style': 'bezier',
                'width': 3,
                'target-arrow-shape': 'triangle',
                'target-arrow-color': '#005a9e',
                'line-color': '#79b8f3',
                'label': 'data(label)',
                'font-size': '12px',
                'color': '#444',
                'text-background-color': '#fff',
                'text-background-opacity': 1,
                'text-background-padding': '4px'
              }}
            }}
          ],
          layout: {{
            name: 'cose',
            animate: false,
            padding: 30
          }}
        }});
      </script>
      <p style="font-size:0.95em;color:#666;">(Drag nodes to rearrange. Relationships are labeled with key columns and cardinality.)</p>
    </section>
    """

def generate_bim_documentation(bim_json_text: str, output_html_path: str):
    """    Generates an HTML documentation for a Business Intelligence Model (BIM) based on its JSON representation.
    ### Parameters
    ----
    bim_json_text: str
        A string containing the JSON representation of the BIM, typically loaded from a .bim file.
    output_html_path: str
        The path where the HTML documentation will be saved.
    ### Returns
    ----
        None: The function writes the generated HTML to the specified output path.
    """
    bim = json.loads(bim_json_text)
    model = bim['model']
    tables = model.get("tables", [])
    relationships = model.get("relationships", [])
    roles = model.get("roles", [])

    config_html = parse_config(model, bim)
    diagram_html = generate_cytoscape_diagram(tables, relationships)
    relationships_html = "".join([parse_relationship(r) for r in relationships])
    # COLLAPSED BY DEFAULT
    relationships_section = f"""
    <details class="relationships-section">
      <summary><h2 style='display:inline'>Relationships</h2></summary>
      <ul>{relationships_html or "<li>No relationships</li>"}</ul>
    </details>
    """
    roles_html = "".join([parse_role(r) for r in roles])
    roles_section = f"""
    <section class="roles-section">
      <h2>Roles / RLS</h2>
      {roles_html or "<em>No roles defined</em>"}
    </section>
    """
    tables_index_html = generate_index_of_tables(tables)
    tables_html = "".join([parse_table(t) for t in tables])

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet" />
      <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
      <title>Power BI Model Documentation</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        html,body {{
          font-family: 'Segoe UI', 'Roboto', Arial, sans-serif;
          background: #f3f6fa;
          margin: 0;
          color: #222;
        }}
        body {{
          max-width: 1100px;
          margin: 0 auto;
          padding: 0 0 4em 0;
        }}
        header {{
          background: linear-gradient(90deg,#0078d4 0,#00bcf2 100%);
          color: #fff;
          padding: 2rem 1.5rem 1.2rem 1.5rem;
          margin-bottom: 2rem;
          box-shadow: 0 2px 8px #0001;
        }}
        header h1 {{
          margin: 0;
          font-size: 2.5rem;
          letter-spacing: 1px;
        }}
        .diagram-section {{
          background: #fff;
          border-radius: 8px;
          box-shadow: 0 2px 8px #0001;
          margin-bottom: 2em;
          padding: 1em 1.5em;
        }}
        .table-index {{
          background: #fff;
          border-radius: 8px;
          box-shadow: 0 1px 4px #0001;
          margin-bottom: 2em;
          padding: 1em 1.5em;
        }}
        .table-index h2 {{
          font-size: 1.3em;
          margin-top: 0;
        }}
        .table-index ul {{
          columns: 2 200px;
          padding-left: 1.2em;
          margin: 0;
        }}
        .table-index li {{
          margin-bottom: 0.3em;
        }}
        .table-index a {{
          color: #0078d4;
          text-decoration: none;
        }}
        .table-index a:hover {{
          text-decoration: underline;
        }}
        section {{
          margin-bottom: 2em;
        }}
        .config-section, .relationships-section, .roles-section {{
          background: #fff;
          border-radius: 8px;
          box-shadow: 0 2px 8px #0001;
          margin-bottom: 2em;
          padding: 1em 1.5em;
        }}
        .table-card {{
          background: #fff;
          border-radius: 8px;
          box-shadow: 0 2px 8px #0001;
          margin-bottom: 2em;
          padding: 1.5em 1.5em 1em 1.5em;
        }}
        .table-card > h2 {{
          margin: 0 0 1em 0;
          color: #0078d4;
          font-size: 1.5em;
        }}
        .table-section h3 {{
          margin-top: 0.5em;
        }}
        .columns-table {{
          width: 100%;
          border-collapse: collapse;
          margin-bottom: 1em;
          background: #f7fbfe;
          border-radius: 5px;
          overflow-x: auto;
          font-size: 0.97em;
        }}
        .columns-table th, .columns-table td {{
          border: 1px solid #e0e5ea;
          padding: 0.5em 0.7em;
          text-align: left;
          vertical-align: top;
          word-break: break-word;
        }}
        .columns-table th {{
          background: #e5f3ff;
          color: #005a9e;
        }}
        .columns-table td {{
          background: #fafdff;
        }}
        .columns-table tr:hover td {{
          background: #f0f8ff;
        }}
        .table-section details {{
          margin-bottom: 0.8em;
          background: #f7fbfe;
          border-radius: 6px;
          box-shadow: 0 1px 3px #0078d411;
        }}
        .table-section summary {{
          font-weight: 500;
          font-size: 1.1em;
          padding: 0.5em 1em 0.5em 0.5em;
          cursor: pointer;
        }}
        .measure-section > summary,
        .partition-section > summary,
        .role-section > summary {{
          font-weight: 400;
          font-size: 1em;
          padding: 0.3em 0.7em;
        }}
        .measure-section[open] > summary,
        .partition-section[open] > summary,
        .role-section[open] > summary {{
          color: #005a9e;
        }}
        pre {{
          white-space: pre-wrap;
          word-break: break-all;
          background: #f3f6fa;
          padding: 0.5em;
          border-radius: 5px;
          font-size: 0.98em;
          overflow-x: auto;
        }}
        .arrow {{
          color: #888;
          font-size: 1.2em;
          margin: 0 0.5em;
        }}
        .cardinality {{
          background: #e5f3ff;
          color: #0078d4;
          border-radius: 4px;
          font-size: 0.92em;
          padding: 0.07em 0.5em;
          margin-left: 0.2em;
        }}
        .badge {{
          display: inline-block;
          background: #e5f3ff;
          color: #0078d4;
          border-radius: 5px;
          font-size: 0.85em;
          padding: 0.15em 0.6em;
          margin-left: 0.5em;
          vertical-align: middle;
        }}
        ul {{
          padding-left: 1.5em;
        }}
        details.relationships-section > summary {{
          cursor: pointer;
        }}
        details.relationships-section[open] > summary {{
          color: #0078d4;
        }}
        @media (max-width: 600px) {{
          body, header {{
            padding-left: 0.5em;
            padding-right: 0.5em;
          }}
          .table-card, .config-section, .relationships-section, .roles-section, .diagram-section, .table-index {{
            padding-left: 0.5em;
            padding-right: 0.5em;
          }}
          .table-index ul {{
            columns: 1 150px;
          }}
        }}
      </style>
    </head>
    <body>
      <header>
        <h1>Power BI Semantic Model Documentation</h1>
      </header>
      {config_html}
      {diagram_html}
      {relationships_section}
      {roles_section}
      {tables_index_html}
      {tables_html}
    </body>
    </html>
    """

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html)

def load_bim_file_as_string(filepath: str) -> str:
    """    Loads a BIM file and returns its contents as a string.
    ### Parameters
    ----    
    filepath: str
        The path to the BIM file to be loaded.
    ### Returns
    ----
        str: The contents of the BIM file as a string.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        contents = f.read()

    # Optional: Validate it's proper JSON
    try:
        json.loads(contents)  # ensure it's valid
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {filepath}: {e}")

    return contents

def save_files_from_api_response(response_json, output_dir, item_name, item_type, report_connection=None):
    """
    Saves base64-encoded files from an API response to the local filesystem.
    ### Parameters
    ----    
    response_json: dict
      The item definition parts.
    output_dir: str
        The base directory where files will be stored. Ej: C:/Users/...
    item_name: str
        The name of the item.
    item_type: str
        The type of the item. E.g., 'report', 'dataset' or 'semanticmodel'.
    report_connection: str only for report item type
        The connection type of the report. E.g., 'LiveConnection' or 'Import' by default it's LiveConnection
    ### Returns
    ----
        A print with the stored files in the local filesystem output_dir.
    Args:
         
    """
    case = item_type.lower()
    if case == 'report' or case == 'reports':
        item_type = 'Report'
    elif case == 'dataset':
        item_type = 'SemanticModel'
    elif case == 'semanticmodel':
        item_type = 'SemanticModel'
    else:
        raise ValueError(f"Invalid item type: {item_type}")


    parts = response_json.get("definition", {}).get("parts", [])
    if not parts:
        print("No files found in response.")
        return

    for part in parts:
        file_path = item_name + "." + item_type + "/" + part.get("path")
        payload = part.get("payload")
        payload_type = part.get("payloadType")

        # Skip invalid entries
        if not file_path or not payload or payload_type != "InlineBase64":
            print(f"Skipping invalid entry: {part}")
            continue

        # Build the full local path
        full_path = os.path.join(output_dir, file_path)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Decode base64 content and write to file
        try:
            decoded_bytes = base64.b64decode(payload)
            if(report_connection=="Import"):
              if part.get("path") == "definition.pbir":
                  pbir = json.loads(decoded_bytes)
                  pbir['datasetReference']['byPath'] = {}
                  pbir['datasetReference']['byPath']['path'] = "../"+item_name+".SemanticModel"
                  del pbir['datasetReference']['byConnection']
                  decoded_bytes = json.dumps(pbir).encode()
            with open(full_path, "wb") as f:
                f.write(decoded_bytes)
            print(f"Saved: {full_path}")
        except Exception as e:
            print(f"Failed to write {file_path}: {e}")
