# UCI_HOV_Project

## Description
This library is written in Python and intended to collect various Highway data on Caltrans Performance Measurement System (PeMS).

## Requirements
requests, bs4, time, datetime

## Class List
### class PeMS(*self, username, pw*)
: Initialization of the webbrowser session and connection to the PeMS
  #### function initSession(username, pw)
  **Parameter of the function** | |
  ------|:------
  username|*string*
   || Username of a PeMS account for login
  pw|*string*
   || Password for the username
   ||
  **Return** | |
  session|*requests.sessions.Session* 
   || The logged-in webbrowser session which would be maintained until the finished the script

- example of log-in process

>import PeMS as pms
> 
>pems = pms.PeMS()
>
>r, session = pems.initSession("PeMS account", "your password")
>
>print "start!"

### class ChangeLog(*self, session, id*)
 : Stations (sensors on Highway) and the corresponding highway segments information
 
**Parameter** | |
------|:------
session|*requests.sessions.Session* 
 ||Username of a PeMS account for login
id|*string*
 || Station ID of interest
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
16| [Value,  'Date',                           16]
17| [Value,  'Status',                         17]
18| [Value,  'Name',                           18]
19| [Value,  'Lanes',                          19]
20| [Value,  'CA PM',                          20]
21| [Value,  'Abs PM',                         21]
22| [Value,  'Length',                         22]
23| [Value,  'Lat',                            23]
24| [Value,  'Lng',                            24]
  ||## Staion Details
25| [Value,  'Aliases',                        25]
26| [Value,  'LDS',                            26]
27| [Value,  'Owner',                          27]
28| [Value,  'Assoc. Traffic Census Station',  28]
29| [Value,  'Comm Type (LDS)',                29]
30| [Value,  'Speeds',                         30]
31| [Value,  'Max Cap.',                       31]
32| [Value,  'Vehicle Classification',         32]
  ||## Lane Detection
33| [Value,  'Lane',                           33]
34| [Value,  'Slot',                           34]
35| [Value,  'Sensor Tech',                    35]
36| [Value,  'Type',                           36]
  ||## Diagnostics
37| [Value,  'Threshold Set',                  37]
38| [Value,  'Flow = 0, Occ > 0 (Intermittent)',38]
39| [Value,  'High Flow Threshold',            39]
40| [Value,  'High Occ Threshold',             40]
41| [Value,  'High Occupancy (High Val)',      41]
42| [Value,  'Occ = 0; Flow > 0 (Intermittent)',42]
43| [Value,  'Repeat Occupancy (Constant)',    43]
44| [Value,  'Occupancy = 0 (Card Off)',       44]

### class AADT(*self, session, id, startDate='20160101', endDate='20161231'*)
 : Average Annual Daily Traffic (AADT) of a specific station during a certain time period (Default period - 20160101 ~ 20161231)
 
**Parameter** | |
------|:------
session|*requests.sessions.Session* 
 ||Username of a PeMS account for login
id|*string*
 || Station ID of interest
startDate|*string*
 || starting date of the time range (YYYYMMDD)
endDate|*string*
 || end date of the time range (YYYYMMDD)
 ||
**Return**| |
0| [Value,  'Station ID',                  0]
 ||## AADT
1| [Value,  'Starting Month',              1]
2| [Value,  'Fwy',                         2]
3| [Value,  'CA PM',                       3]
4| [Value,  'Abs PM',                      4]
5| [Value,  'VDS',                         5]
6| [Value,  'Name',                        6]
7| [Value,  'Type',                        7]
8| [Value,  'Arithmetic Mean',             8]
9| [Value,  'ASTM Std',                    9]
10|[Value,  'Conv. AASHTO',                10]
11|[Value,  'Prov. AASHTO',                11]
12|[Value,  'Sum of 24 Annual Avg Hours',  12]
13|[Value,  'Mod. ASTM Std',               13]
14|[Value,  'Mod. Conv. AASHTO',           14]
15|[Value,  'Mod. Prov. AASHTO',           15]
16|[Value,  '% Data Used',                 16]
17|[Value,  'K',                           17]

### class CHPIncidents(*self, session, fwy, direction, start_AbsPm, end_AbsPm, CHPtype='accident', startDate='20160101', endDate='20161231'*)
 : California Highway Patrol Incidents data based on absolute postmile of the Highway during a specific time perioud.(Default incident - 'accident'/ Default period - 20160101 ~ 20161231)
 
**Parameter** | |
------|:------
session|*requests.sessions.Session* 
 ||Username of a PeMS account for login
fwy|*string*
 || Station ID of interest
direction|*string*
 || Direction of Highway
start_AbsPm|*float*
 || Starting absolute postmile of a road segment
end_AbsPm|*float*
 || Ending absolute postmile of a road segment
CHPtype|*string*
 || Type of incidents (one among 'accident', 'breakdown', 'congestion', 'hazard', 'police', 'weather', 'other')
startDate|*string*
 || starting date of the time range (YYYYMMDD)
endDate|*string*
 || end date of the time range (YYYYMMDD)
 ||
**Return**| |
0| [Value,  'fwy',                           0]
1| [Value,  'direction',                     1]
2| [Value,  'start_AbsPm',                   2]
3| [Value,  'end_AbsPm',                     3]
4| [Value,  str(CHPtype),                    4]
