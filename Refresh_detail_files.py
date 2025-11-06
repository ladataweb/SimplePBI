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
from simplepbi import pipelines
from simplepbi import scorecards
from simplepbi import azpause
from simplepbi import pushdatasets
from simplepbi.fabric import core
from simplepbi.fabric import adminfab
from simplepbi.fabric import datapipelines
from simplepbi.fabric import semanticmodels
from simplepbi.fabric import report
from simplepbi import utils

import pydoc

if __name__ == '__main__':	
    ad = pydoc.render_doc(admin, forceload=0, renderer=pydoc.plaintext)
    dataset = pydoc.render_doc(datasets, forceload=0, renderer=pydoc.plaintext)
    group = pydoc.render_doc(groups, forceload=0, renderer=pydoc.plaintext)
    dataflow = pydoc.render_doc(dataflows, forceload=0, renderer=pydoc.plaintext)
    reportt = pydoc.render_doc(reports, forceload=0, renderer=pydoc.plaintext)
    dashboard = pydoc.render_doc(dashboards, forceload=0, renderer=pydoc.plaintext)
    app = pydoc.render_doc(apps, forceload=0, renderer=pydoc.plaintext)
    impo = pydoc.render_doc(imports, forceload=0, renderer=pydoc.plaintext)
    gway = pydoc.render_doc(gateways, forceload=0, renderer=pydoc.plaintext)
    capa = pydoc.render_doc(capacities, forceload=0, renderer=pydoc.plaintext)
    pipe = pydoc.render_doc(pipelines, forceload=0, renderer=pydoc.plaintext)
    score = pydoc.render_doc(scorecards, forceload=0, renderer=pydoc.plaintext)
    azpau = pydoc.render_doc(azpause, forceload=0, renderer=pydoc.plaintext)
    pushd = pydoc.render_doc(pushdatasets, forceload=0, renderer=pydoc.plaintext)
    adfab = pydoc.render_doc(adminfab, forceload=0, renderer=pydoc.plaintext)
    coree = pydoc.render_doc(core, forceload=0, renderer=pydoc.plaintext)
    seman = pydoc.render_doc(semanticmodels, forceload=0, renderer=pydoc.plaintext)
    rept = pydoc.render_doc(report, forceload=0, renderer=pydoc.plaintext)
    dpipes = pydoc.render_doc(datapipelines, forceload=0, renderer=pydoc.plaintext)
    utii = pydoc.render_doc(utils, forceload=0, renderer=pydoc.plaintext)

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
    r.write(reportt)
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
    
    pipel=open(r'Pipelines_details.txt', 'w')
    pipel.write(pipe)
    pipel.close()
    
    Scor=open(r'Scorecards_details.txt', 'w')
    Scor.write(score)
    Scor.close()
    
    az=open(r'Az_Pause_Resume_details.txt', 'w')
    az.write(azpau)
    az.close()
    
    pud=open(r'Push_Datasets_details.txt', 'w')
    pud.write(pushd)
    pud.close()
    
    afab=open(r'Fabric_Admin_details.txt', 'w')
    afab.write(adfab)
    afab.close()
    
    corefab=open(r'Fabric_Core_details.txt', 'w')
    corefab.write(coree)
    corefab.close()
    
    semod=open(r'Fabric_SemanticModels_details.txt', 'w')
    semod.write(seman)
    semod.close()
    
    repor=open(r'Fabric_Report_details.txt', 'w')
    repor.write(rept)
    repor.close()
    
    dapipes=open(r'Fabric_DataPipelines_details.txt', 'w')
    dapipes.write(dpipes)
    dapipes.close()
    
    utiil=open(r'Utils_details.txt', 'w')
    utiil.write(utii)
    utiil.close()