'''
Created on Feb 21, 2017

@author: Bumsub Park
'''

import requests
from bs4 import BeautifulSoup
import time
import datetime

class PeMS:   
    def __init__(self):
        self.url = 'http://pems.dot.ca.gov/'
        
    def initSession(self):
        session = requests.session()
        values = {'username' : 'bumsubp@uci.edu',
                  'password':'javawm',
                  'submit':'login',}
        r=session.post(self.url, data=values)
        return r, session
    
class ChangeLog:
    def __init__(self, session, id):
        self.id =id
        self.url = "http://pems.dot.ca.gov/?html_x=48&report_form=1&pagenum_all=1&county_id=59&station_id="+self.id+"&dnode=VDS"        
        r=session.get(self.url)
        soup = BeautifulSoup(r.content,"lxml")
        self.cl = soup.findAll('table', attrs={"class": "blue_outline_table"})
        self.sd = soup.findAll('div', attrs={"class": "segmentPanelSection"})
        self.attrs = {
                      0: [None,  'Station ID',                      0],
                      ## Roadway Information (from TSN)
                      1: [None,  'Road Width',                      1],
                      2: [None,  'Lane Width',                      2],
                      3: [None,  'Inner Shoulder Width',            3],
                      4: [None,  'Inner Shoulder Treated Width',    4],
                      5: [None,  'Outer Shoulder Width',            5],
                      6: [None,  'Outer Shoulder Treated Width',    6],
                      7: [None,  'Design Speed Limit',              7],
                      8: [None,  'Functional Class',                8],
                      9: [None,  'Inner Median Type',               9],
                      10:[None,  'Inner Median Width',             10],
                      11:[None,  'Terrain',                         11],
                      12:[None,  'Population',                      12],
                      13:[None,  'Barrier',                         13],
                      14:[None,  'Surface',                         14],
                      15:[None,  'Roadway Use',                     15],
                      ## Change Log
                      16: [None,  'Date',                           16],
                      17: [None,  'Status',                         17],
                      18: [None,  'Name',                           18],
                      19: [None,  'Lanes',                          19],
                      20: [None,  'CA PM',                          20],
                      21: [None,  'Abs PM',                         21],
                      22: [None,  'Length',                         22],
                      23: [None,  'Lat',                            23],
                      24: [None,  'Lng',                            24],
                      ## Staion Details
                      25: [None,  'Aliases',                        25],
                      26: [None,  'LDS',                            26],
                      27: [None,  'Owner',                          27],
                      28: [None,  'Assoc. Traffic Census Station',  28],
                      29: [None,  'Comm Type (LDS)',                29],
                      30: [None,  'Speeds',                         30],
                      31: [None,  'Max Cap.',                       31],
                      32: [None,  'Vehicle Classification',         32],
                      ## Lane Detection
                      33: [None,  'Lane',                           33],
                      34: [None,  'Slot',                           34],
                      35: [None,  'Sensor Tech',                    35],
                      36: [None,  'Type',                           36],
                      ## Diagnostics
                      37: [None,  'Threshold Set',                  37],
                      38: [None,  'Flow = 0, Occ > 0 (Intermittent)',38],
                      39: [None,  'High Flow Threshold',            39],
                      40: [None,  'High Occ Threshold',             40],
                      41: [None,  'High Occupancy (High Val)',      41],
                      42: [None,  'Occ = 0; Flow > 0 (Intermittent)',42],
                      43: [None,  'Repeat Occupancy (Constant)',    43],
                      44: [None,  'Occupancy = 0 (Card Off)',       44]
                      }
        
        self.station_ID()
        self.roadway_Information()
        self.change_Log()
        self.stationDetails()
        self.laneDetection()
        self.diagnostics()
        
    def __getitem__(self, key):
        if key in self.attrs:
            return self.attrs[key][0]
        
    def __setitem__(self, key, item):
        if key in self.attrs:
            self.attrs[key][0] = item
            
    def station_ID(self):
        self.attrs[0][0] = str(self.id)
        
    def roadway_Information(self):
        table1 = self.cl[0]
        tds = table1.findAll('td')
        for ind, td in enumerate(tds[1:]):
            if ind%2 == 1:
                self.attrs[(ind//2)+1][0] = str(td.getText())
    
    def change_Log(self):
        table2 = self.cl[1]
        trs = table2.findAll('tr')
        tds = trs[-1].findAll('td')
        for ind, td in enumerate(tds):
            self.attrs[ind+16][0] = str(td.getText())
    
    def stationDetails(self):
        table3 = self.sd[1]
        tds = table3.findAll('td')
        for ind, td in enumerate(tds):
            if ind%2 == 1:
                self.attrs[(ind//2)+25][0] = str(td.getText())
                
    def laneDetection(self):
        table4 = self.sd[2]
        trs = trs = table4.findAll('tr')
        tds = trs[1].findAll('td')
        for ind, td in enumerate(tds):
            self.attrs[ind+33][0] = str(td.getText())

    def diagnostics(self):
        table5 = self.sd[3]
        tds = table5.findAll('td')
        for ind, td in enumerate(tds):
            if ind%2 == 1:
                self.attrs[(ind//2)+37][0] = str(td.getText())

class AADT:
    def __init__(self, session, id, startDate='20160101', endDate='20161231'):
        self.id = str(id)
        sDate = datetime.date(int(startDate[:4]), int(startDate[4:6]), int(startDate[6:]))
        eDate = datetime.date(int(endDate[:4]), int(endDate[4:6]), int(endDate[6:]))

        sUnixtime = str(int(time.mktime(sDate.timetuple())))
        eUnixtime = str(int(time.mktime(eDate.timetuple())))

                
        self.urlAADT = "http://pems.dot.ca.gov/?report_form=1&dnode=VDS&content=analysis&tab=aadt&export=&station_id="+self.id+"&s_time_id="+sUnixtime+"&e_time_id="+eUnixtime+"&html.x=46&html.y=14"
        r=session.get(self.urlAADT)
        soup = BeautifulSoup(r.content,"lxml")
        self.aa = soup.findAll('table', attrs={"class": "inlayTable"})
        
        self.attrs = {
                      0: [None,  'StationID',                   0],
                      ## AADT
                      1: [None,  'Starting Month',              1],
                      2: [None,  'Fwy',                         2],
                      3: [None,  'CA PM',                       3],
                      4: [None,  'Abs PM',                      4],
                      5: [None,  'VDS',                         5],
                      6: [None,  'Name',                        6],
                      7: [None,  'Type',                        7],
                      8: [None,  'Arithmetic Mean',             8],
                      9: [None,  'ASTM Std',                    9],
                      10:[None,  'Conv. AASHTO',                10],
                      11:[None,  'Prov. AASHTO',                11],
                      12:[None,  'Sum of 24 Annual Avg Hours',  12],
                      13:[None,  'Mod. ASTM Std',               13],
                      14:[None,  'Mod. Conv. AASHTO',           14],
                      15:[None,  'Mod. Prov. AASHTO',           15],
                      16:[None,  '% Data Used',                 16],
                      17:[None,  'K',                           17]
                      }
        
        self.station_ID()
        self.aadt()
        
    def __getitem__(self, key):
        if key in self.attrs:
            return self.attrs[key][0]
        
    def __setitem__(self, key, item):
        if key in self.attrs:
            self.attrs[key][0] = item
    
    def station_ID(self):
        self.attrs[0][0] = str(self.id)
    
    def aadt(self):
        table1 = self.aa[0]
        trs = table1.findAll('tr')
        for ind, td in enumerate(trs[-1]):
            if ind%2 == 1:
                self.attrs[ind//2][0]=str(td.string)            

class CHPIncidents:
    def __init__(self, session, fwy, direction, start_AbsPm, end_AbsPm, CHPtype='accident', startDate='20160101', endDate='20161231'):
        self.fwy = fwy
        self.direction = direction
        self.start = start_AbsPm
        self.end = end_AbsPm
        self.CHPtype = CHPtype
        
        sDate = datetime.date(int(startDate[:4]), int(startDate[4:6]), int(startDate[6:]))
        eDate = datetime.date(int(endDate[:4]), int(endDate[4:6]), int(endDate[6:]))
        sUnixtime = str(int(time.mktime(sDate.timetuple())))
        eUnixtime = str(int(time.mktime(eDate.timetuple())))
        
        #http://pems.dot.ca.gov/?report_form=1&dnode=Freeway&content=incidents&tab=inc_perfts&export=&fwy=5&dir=N&s_time_id=1451606400&e_time_id=1483228740&gn=year&q=&severity=sev_all&type[]=accident&type[]=breakdown&type[]=congestion&type[]=hazard&type[]=police&type[]=weather&type[]=other&source_id=&start_pm=72.408&end_pm=73.408&html.x=28&html.y=6

        self.urlCHP = "http://pems.dot.ca.gov/?report_form=1&dnode=Freeway&content=incidents&tab=inc_perfts&export=&fwy="+fwy+"&dir="+direction+"&s_time_id="+sUnixtime+"&e_time_id="+eUnixtime+"&gn=year&q=&severity=sev_all&type[]="+CHPtype+"&source_id=&start_pm="+start_AbsPm+"&end_pm="+end_AbsPm+"&html.x=28&html.y=6"
    
        r=session.get(self.urlCHP)
        soup = BeautifulSoup(r.content,"lxml")
        self.chp = soup.findAll('table', attrs={"class": "inlayTable"})
        
        self.attrs = {
                      0: [None,  'fwy',                           0],
                      1: [None,  'direction',                     1],
                      2: [None,  'start_AbsPm',                   2],
                      3: [None,  'end_AbsPm',                     3],
                      4: [None,  str(CHPtype),                    4]
                      }
        
        self.station_ID()
        self.chpIncidents()
        
    def __getitem__(self, key):
        if key in self.attrs:
            return self.attrs[key][0]
    
    def __setitem__(self, key, item):
        if key in self.attrs:
            self.attrs[key][0] = item
    def station_ID(self):
        self.attrs[0][0] = str(self.fwy)
        self.attrs[1][0] = str(self.direction)
        self.attrs[2][0] = str(self.start)
        self.attrs[3][0] = str(self.end)
        
    def chpIncidents(self):
        table1 = self.chp[0]
        trs = table1.findAll('tr')
        td = trs[-1].findAll('td')[-1]
        self.attrs[4][0] = str(td.string)
            
class RawData:
    def __init__(self, session, id, startTime, endTime, quantity, granularity):
        # Time YYYYMMDDHHMM
        sTime = datetime.datetime(int(startTime[:4]), int(startTime[4:6]), int(startTime[6:8]), int(startTime[8:10]), int(startTime[10:]))
        eTime = datetime.datetime(int(endTime[:4]), int(endTime[4:6]), int(endTime[6:8]), int(endTime[8:10]), int(endTime[10:]))
        
        sUnixtime = str(int(time.mktime(sTime.timetuple())) - 25200)
        eUnixtime = str(int(time.mktime(eTime.timetuple())) - 25200)
        
        self.urlRawData = "http://pems.dot.ca.gov/?report_form=1&dnode=VDS&content=detector_health&tab=dh_raw&export=&station_id="+id+"&s_time_id="+sUnixtime+"&e_time_id="+eUnixtime+"&lanes="+id+"-1&q="+quantity+"&q2=&gn="+granularity+"&html.x=34&html.y=6"
        # flow / nflow / occ / gspeed / speed_not_used
        # sec / 5min / 15min / hour
        
        r=session.get(self.urlRawData)
        soup = BeautifulSoup(r.content,"lxml")
        
        self.rd = soup.findAll('table', attrs={"class": "inlayTable"})[0]
        
class TimeSeries:
    def __init__(self, session, id, startTime, endTime, quantity, granularity):
        self.id = str(id)
        # Time YYYYMMDDHHMM
        sTime = datetime.datetime(int(startTime[:4]), int(startTime[4:6]), int(startTime[6:8]), int(startTime[8:10]), int(startTime[10:]))
        eTime = datetime.datetime(int(endTime[:4]), int(endTime[4:6]), int(endTime[6:8]), int(endTime[8:10]), int(endTime[10:]))
        
        sUnixtime = str(int(time.mktime(sTime.timetuple())) - 28800)
        eUnixtime = str(int(time.mktime(eTime.timetuple())) - 28800)
        
        self.urlTimeSeries = "http://pems.dot.ca.gov/?report_form=1&dnode=VDS&content=loops&tab=det_timeseries&export=&station_id="+id+"&s_time_id="+sUnixtime+"&e_time_id="+eUnixtime+"&tod=all&tod_from=0&tod_to=0&dow_0=on&dow_1=on&dow_2=on&dow_3=on&dow_4=on&dow_5=on&dow_6=on&holidays=on&q="+quantity+"&q2=&gn="+granularity+"&lane1=on&html.x=60&html.y=11"
        # flow / occ / speed /truck_flow / truck_prop / vmt / vht / q / tti / truck_vmt / truck_vht / del_35 / del_40 / del_45 / del_50 / del_55 / del_60 / lost_prod_35 / lost_prod_40 / lost_prod_45 / lost_prod_50 / lost_prod_55 / lost_prod_60
        # 5min / hour / day / week / month
    
        r=session.get(self.urlTimeSeries)
        soup = BeautifulSoup(r.content, "lxml")
        
        self.ts = soup.findAll('table', attrs={"class": "inlayTable"})[0]
        
        self.attrs = {
                      0: [None,  'id',                           0],
                      1: [None,  'time',                         1],
                      2: [None,  str(quantity),                  2]}
        
        self.station_ID()
        self.timeSeries()
        
    def __getitem__(self, key):
        if key in self.attrs:
            return self.attrs[key][0]
    
    def __setitem__(self, key, item):
        if key in self.attrs:
            self.attrs[key][0] = item
    def station_ID(self):
        self.attrs[0][0] = str(self.id)
        
    def timeSeries(self):
        table = self.ts
        tbody = table.findAll('tbody')[0]
        trs = tbody.findAll('tr')
        idList = []
        quantityList = []
        for tr in trs:
            td = tr.findAll('td')[:2]
            idList.append(str(td[0].string))
            quantityList.append(str(td[1].string))
        self.attrs[1][0] = idList
        self.attrs[2][0] = quantityList
            