#!/usr/bin/env python
import sys
import xml.dom.minidom as minidom

doc = minidom.Document()
annotation = doc.createElement("annotation")
doc.appendChild(annotation)

def addobject(_name, _xmin, _xmax, _ymin, _ymax):
    obj = doc.createElement("object")
    
    name = doc.createElement("name")
    textname = doc.createTextNode(_name)
    name.appendChild(textname)
    obj.appendChild(name)
    
    box = doc.createElement("nbdbox")
    obj.appendChild(box)
    
    xmin = doc.createElement("xmin")
    xmax = doc.createElement("xmax")
    ymin = doc.createElement("ymin")
    ymax = doc.createElement("ymax")
    
    textxmin = doc.createTextNode(_xmin)
    xmin.appendChild(textxmin)
    textxmax = doc.createTextNode(_xmax)
    xmax.appendChild(textxmax)
    textymin = doc.createTextNode(_ymin)
    ymin.appendChild(textymin)
    textymax = doc.createTextNode(_ymax)
    ymax.appendChild(textymax)

    box.appendChild(xmin)
    box.appendChild(xmax)
    box.appendChild(ymin)
    box.appendChild(ymax)
    
    annotation.appendChild(obj)


fi=sys.argv[1]
fin=open(fi+".txt", "r");
alllines = fin.readlines();
fin.close()
for eachline in alllines:
    arr = eachline.split()
    a = min(int(arr[1]), int(arr[3]))
    b = max(int(arr[1]), int(arr[3]))
    c = min(int(arr[2]), int(arr[4]))
    d = max(int(arr[2]), int(arr[4]))
    addobject(arr[0],str(a), str(b), str(c), str(d))
 
fout = file(fi+".xml","w")
doc.writexml(fout,"\t", "\t", "\n")
fout.close()
