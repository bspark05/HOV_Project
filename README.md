# HOV_Project

## Description
This library is written in Python and intended to collect various Highway data on Caltrans Performance Measurement System (PeMS).

## Requirements
requests, bs4, time, datetime

## Class List
### class PeMS(*self, username, pw*)
: Initialization of the webbrowser session and connection to the PeMS

**Parameter** | |
------|:------
username|*string*
 || Username of a PeMS account for login
pw|*string*
 || Password for the username
 ||
**Return** | |
session|*requests.sessions.Session* 
 || The logged-in webbrowser session which would be maintained until the finished the script

### class ChangeLog(*self, session, id*)
 : Stations (sensors on Highway) and the corresponding highway segments information
 
**Parameter** | |
------|:------
session|*requests.sessions.Session* 
 ||Username of a PeMS account for login
pw|*string*
 || Password for the username
 ||
**Return**| |
0| [Value,  'Station ID',                      0]
 ||## Roadway Information (from TSN)
1| [Value,  'Road Width',                      1]
2| [Value,  'Lane Width',                      2]
3| [Value,  'Inner Shoulder Width',            3]
4| [Value,  'Inner Shoulder Treated Width',    4]
5| [Value,  'Outer Shoulder Width',            5]
6| [Value,  'Outer Shoulder Treated Width',    6]
7| [Value,  'Design Speed Limit',              7]
8| [Value,  'Functional Class',                8]
9| [Value,  'Inner Median Type',               9]
10|[Value,  'Inner Median Width',             10]
11|[Value,  'Terrain',                         11]
12|[Value,  'Population',                      12]
13|[Value,  'Barrier',                         13]
14|[Value,  'Surface',                         14]
15|[Value,  'Roadway Use',                     15]
  ||## Change Log
16| [None,  'Date',                           16]
17| [None,  'Status',                         17]
18| [None,  'Name',                           18]
19| [None,  'Lanes',                          19]
20| [None,  'CA PM',                          20]
21| [None,  'Abs PM',                         21]
22| [None,  'Length',                         22]
23| [None,  'Lat',                            23]
24| [None,  'Lng',                            24]
  ||## Staion Details
25| [None,  'Aliases',                        25]
26| [None,  'LDS',                            26]
27| [None,  'Owner',                          27]
28| [None,  'Assoc. Traffic Census Station',  28]
29| [None,  'Comm Type (LDS)',                29]
30| [None,  'Speeds',                         30]
31| [None,  'Max Cap.',                       31]
32| [None,  'Vehicle Classification',         32]
  ||## Lane Detection
33| [None,  'Lane',                           33]
34| [None,  'Slot',                           34]
35| [None,  'Sensor Tech',                    35]
36| [None,  'Type',                           36]
  ||## Diagnostics
37| [None,  'Threshold Set',                  37]
38| [None,  'Flow = 0, Occ > 0 (Intermittent)',38]
39| [None,  'High Flow Threshold',            39]
40| [None,  'High Occ Threshold',             40]
41| [None,  'High Occupancy (High Val)',      41]
42| [None,  'Occ = 0; Flow > 0 (Intermittent)',42]
43| [None,  'Repeat Occupancy (Constant)',    43]
44| [None,  'Occupancy = 0 (Card Off)',       44]
