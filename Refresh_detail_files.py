from simplepbi import admin
from simplepbi import datasets
from simplepbi import groups
from simplepbi import dataflows
#from simplepbi import utils

import pydoc

if __name__ == '__main__':	
    ad = pydoc.render_doc(admin, forceload=0, renderer=pydoc.plaintext)
    dataset = pydoc.render_doc(datasets, forceload=0, renderer=pydoc.plaintext)
    group = pydoc.render_doc(groups, forceload=0, renderer=pydoc.plaintext)
    dataflow = pydoc.render_doc(dataflows, forceload=0, renderer=pydoc.plaintext)

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