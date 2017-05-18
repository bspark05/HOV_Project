'''
Created on Feb 21, 2017

@author: Bumsub Park
'''
import PeMS as pms
import Excel as ex
# import PeMS2 as pms2

def rowtoList(records):
        rowList = []
        ind = 0
        row = []
        while ind<=44:
            row.append(records[ind])
            ind+=1
        rowList.append(row)
        return rowList
    
def idList(filename, sheetname, startRowNum=1):
    idExcel = ex.excelRead(filename, sheetname)
    idList = []
    for stationID in idExcel[startRowNum-1:]:
        stationID = str(int(stationID[0].value))
        idList.append(stationID)
    return idList

def idList4CHP(filename, sheetname, startRowNum=2):
    ## input- peMS_Incidents_ID_Mainline.xlsx containing [ID fwy direction abs_pm start end distance]
    idExcel = ex.excelRead(filename, sheetname)
    idList = []
    for stationID in idExcel[startRowNum-1:]:
        stationIDList=[]
        stationIDList.append(str(int(stationID[0].value)))
        stationIDList.append(str(int(stationID[1].value)))
        stationIDList.append(str(stationID[2].value))
        stationIDList.append(str(float(stationID[3].value)))
        stationIDList.append(str(float(stationID[4].value)))
        stationIDList.append(str(float(stationID[5].value)))
        stationIDList.append(str(float(stationID[6].value)))
        idList.append(stationIDList)
    return idList ##Doulbe list

if __name__ == '__main__':
    
#     ##PeMS Incidents Javascript##
#     pems2=pms2.PeMS2()
#     driver = pems2.initSession()
#     print "start!"
#     
#     idList = idList("peMS_ID_test.xlsx", "Sheet1", startRowNum=2)
#     print idList
#     for stationID in idList:
#         acci = pms2.DayOfWeek(driver, stationID)
#         rowList = rowtoList(acci)
#         
#         print rowList[0][0]
#         ex.excelWriteOnExistingFile("peMS_Accident_test.xlsx", "Sheet1", 'A', rowList)
      
    pems = pms.PeMS()
    r, session = pems.initSession("bumsubp@uci.edu", "javawm")
    print "start!"

#     ##ChangeLog##
#     idList = idList("test.xlsx", "Sheet1", startRowNum=2)
#     print idList
#     for stationID in idList:
#         cl = pms.ChangeLog(session, stationID)
#         rowList = rowtoList(cl)
#            
#         print rowList[0][0]        
#         ex.excelWriteOnExistingFile("test_changelog.xlsx", "Sheet1", 'A', rowList)

#     ##AADT##
#     idList = idList("peMS_ID_Mainline.xlsx", "LA", startRowNum=2)
#     print idList
#     for stationID in idList:
#         aadt = pms.AADT(session, stationID, '20160101', '20161231')
#         rowList = rowtoList(aadt)
#           
#         print rowList[0][4]        
#         ex.excelWriteOnExistingFile("peMS_AADT_Mainline.xlsx", "LA", 'A', rowList)

#     ##Incidents##
#     idList = idList4CHP("peMS_Incidents_ID_Mainline.xlsx", "OC", startRowNum=2)
#     for row in idList:
#         chp = pms.CHPIncidents(session, row[0], row[1], row[3], row[4], row[5], row[6], "accident")
#         rowList = rowtoList(chp)
#         
#         print rowList[0][0]
#         ex.excelWriteOnExistingFile("peMS_Incidents_Accidents_Mainline.xlsx", "OC", 'A', rowList)

    ## RawData
    idList = idList("test.xlsx", "Sheet1", startRowNum=2)
    print idList
    for stationID in idList:
        rd = pms.RawData(session, stationID, "201705100700", "201705110900", "flow", "sec")
        rdList = rd[0]
        ex.excelWriteOnExistingFileCol("test2.xlsx", "Sheet1", 1, rdList)
