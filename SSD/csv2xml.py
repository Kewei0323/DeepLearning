#!/usr/bin/env python
# coding:utf-8

#from xml.etree.ElementTree import Element, SubElement, tostring
from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import csv

# create the xml file of images
def create_xml(filename):
	xml = tostring(node_root, pretty_print=True)
	dom = parseString(xml)
	f = open(filename, "wb")
	f.write(dom.toprettyxml(indent='\t', encoding='utf-8'))
	f.close()

# replace your filename
filename = 'frameAnnotationsBOX.csv'

# replace your filename
filename = 'frameAnnotationsBOX.csv'

with open(filename) as f:
    reader = csv.reader(f, delimiter=',')
    start = 0
    
    # replace the picture name of your csvfile first line
    tmp = 'nightClip1--00000'
    for row in reader:
        if(start == 0):
            start += 1
            
            node_root = Element('annotation')
            node_folder = SubElement(node_root, 'folder')
            node_folder.text = 'LISA'
            node_filename = SubElement(node_root, 'filename')
            #replace your own filename
            node_filename.text = tmp
            node_size = SubElement(node_root, 'size')
            node_width = SubElement(node_size, 'width')
            node_width.text = '1280'
            node_height = SubElement(node_size, 'height')
            node_height.text = '960'
            node_depth = SubElement(node_size, 'depth')
            node_depth.text = '3'            
            continue
            
        if(tmp == row[0]):
            node_object = SubElement(node_root, 'object')
            node_name = SubElement(node_object, 'name')
            node_name.text = row[1]
            node_pose = SubElement(node_object, 'pose')
            node_pose.text = 'Unspecified' 
            node_truncated = SubElement(node_object, 'truncated')
            node_truncated.text = '0'
            node_difficult = SubElement(node_object, 'difficult')
            node_difficult.text = '0'
            node_bndbox = SubElement(node_object, 'bndbox')
            node_xmin = SubElement(node_bndbox, 'xmin')
            node_xmin.text = row[2]
            node_ymin = SubElement(node_bndbox, 'ymin')
            node_ymin.text = row[3]
            node_xmax = SubElement(node_bndbox, 'xmax')
            node_xmax.text = row[4]
            node_ymax = SubElement(node_bndbox, 'ymax')
            node_ymax.text = row[5]
        if(tmp != row[0]):
            # save the xml file
            create_xml(tmp)
            # content of xml head
            node_root = Element('annotation')
            node_folder = SubElement(node_root, 'folder')
            node_folder.text = 'LISA'
            node_filename = SubElement(node_root, 'filename')
            #replace your own filename
            node_filename.text = tmp
            node_size = SubElement(node_root, 'size')
            node_width = SubElement(node_size, 'width')
            node_width.text = '1280'
            node_height = SubElement(node_size, 'height')
            node_height.text = '960'
            node_depth = SubElement(node_size, 'depth')
            node_depth.text = '3'

        tmp = row[0]
