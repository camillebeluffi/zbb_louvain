#!/usr/bin/env python 
import os
import CMSSW
from AnalysisEvent import AnalysisEvent
import EventSelection
from CPconfig import eventDumpConfig
#import pdb

def DumpEventInfo(event=None, runNumber=None, eventNumber=None, lsNumber=None, path="./"):
  """Dump informations about a given event"""
  # in case no event is provided, find it using eventNumber
  if event is None:
    if (eventNumber is None) or (runNumber is None):
      print "DumpEventInfo Error: either pass an event or an event number"
      return
    # find event based on run and event
    if os.path.isdir(path):
      dirList=os.listdir(path)
      files=[]
      for fname in dirList:
        files.append(path+fname)
    elif os.path.isfile(path):
      files=[path]
    else:
      files=[]
    events = AnalysisEvent(files)
    EventSelection.prepareAnalysisEvent(events)
    DumpEventInfo(events[(runNumber, eventNumber, lsNumber)])
    return
  # run the producers when we want to print the outcome, and mute unneeded collections
  for product in eventDumpConfig.productsToPrint: getattr(event,product)
  for collection in eventDumpConfig.collectionsToHide: event.removeCollection(collection)
  # Now, we can go on with the printing.
  print event
  #pdb.set_trace()

if __name__=="__main__":
  import sys
  DumpEventInfo(runNumber=sys.argv[1], eventNumber=sys.argv[2], lsNumber=sys.argv[3], path=sys.argv[4])

