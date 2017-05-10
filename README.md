# HOV_Project

## Description
This library is written in Python and intended to collect various Highway data on Caltrans Performance Measurement System (PeMS).

## Requirements
requests, bs4, time, datetime

## Class List
### class PeMS(*self, username, pw*)
: Initialization of the webbrowser session and connection to the PeMS

Parameters | Type |
------|:------
**username**|*string*
 || Username of a PeMS account for login
**pw**|*string*
 || Password for the username
 | |
Returns: | |
**session**|*requests.sessions.Session* 
 || The logged-in webbrowser session which would be maintained until the finished the script

### class ChangeLog(*self, session, id*)
 : Stations (sensors on Highway) and the corresponding highway segments information
 
Parameters | Type |
------|------
**session**|*requests.sessions.Session* 
 | Username of a PeMS account for login
**pw**|*string*
 | Password for the username
 | |
Returns: | |
**session**|*requests.sessions.Session* 
 | The logged-in webbrowser session which would be maintained until the finished the script
