from simplepbi import admin
from simplepbi import datasets
from simplepbi import groups
from simplepbi import dataflows
from simplepbi import reports
from simplepbi import dashboards
from simplepbi import apps
from simplepbi import imports
from simplepbi import gateways
from simplepbi import capacities
#from simplepbi import utils

import pydoc

if __name__ == '__main__':	
    ad = pydoc.render_doc(admin, forceload=0, renderer=pydoc.plaintext)
    dataset = pydoc.render_doc(datasets, forceload=0, renderer=pydoc.plaintext)
    group = pydoc.render_doc(groups, forceload=0, renderer=pydoc.plaintext)
    dataflow = pydoc.render_doc(dataflows, forceload=0, renderer=pydoc.plaintext)
    report = pydoc.render_doc(reports, forceload=0, renderer=pydoc.plaintext)
    dashboard = pydoc.render_doc(dashboards, forceload=0, renderer=pydoc.plaintext)
    app = pydoc.render_doc(apps, forceload=0, renderer=pydoc.plaintext)
    impo = pydoc.render_doc(imports, forceload=0, renderer=pydoc.plaintext)
    gway = pydoc.render_doc(gateways, forceload=0, renderer=pydoc.plaintext)
    capa = pydoc.render_doc(capacities, forceload=0, renderer=pydoc.plaintext)

    a=open(r'Admin_details.txt', 'w')
    a.write(ad)
    a.close()
       
    d=open(r'Datasets_details.txt', 'w')
    d.write(dataset)
    d.close()
       
    g=open(r'Groups_details.txt', 'w')
    g.write(group)
    g.close()
       
    f=open(r'Dataflows_details.txt', 'w')
    f.write(dataflow)
    f.close()
    
    r=open(r'Reports_details.txt', 'w')
    r.write(report)
    r.close()
    
    db=open(r'Dashboards_details.txt', 'w')
    db.write(dashboard)
    db.close()
    
    ap=open(r'Apps_details.txt', 'w')
    ap.write(app)
    ap.close()
    
    im=open(r'Imports_details.txt', 'w')
    im.write(impo)
    im.close()
    
    gw=open(r'Gateways_details.txt', 'w')
    gw.write(gway)
    gw.close()
    
    cap=open(r'Capacities_details.txt', 'w')
    cap.write(capa)
    cap.close()
    