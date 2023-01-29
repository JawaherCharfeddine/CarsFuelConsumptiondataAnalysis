"""convert from XML to CSV"""


import pandas as pd
import pandas_datareader as data
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import os
import csv
import math
from statistics import *
import xml.etree.ElementTree as ET



def xml_to_csv(path, output):
  tree = ET.parse(path)
  root = tree.getroot()
  root.tag
  root.attrib

  d = {}
  i = 0
  for child in root:
      #print(child.attrib["time"])
      for childs in child:
        dt = {"time" : child.attrib["time"]}
        d[i] = {**dt, **dict(childs.attrib.items())}
        i += 1

  df = pd.DataFrame.from_dict(d,orient="index")
  df.to_csv(output)



xml_to_csv('emissionwith.xml', 'emissionwith.csv')
xml_to_csv('emissionwithout.xml', 'emissionwithout.csv')
