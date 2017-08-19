'''
Created on 2017. 6. 3.

@author: Administrator
'''
import shapefile
from shapely.geometry import asShape
import Excel as ex

class HwyDirectionShp:
    def __init__(self, roadSgtShp, facilityShp, direction, excelPath, excelSheet):
        #1. reading road segments and facilities
        
        # open a shapefile with pyshp 
        roadSgt0 = shapefile.Reader(roadSgtShp)
        
        # access geometry of the Shapefile
        roadSgt1 = roadSgt0.shapeRecords()
        
        # convert pyshp object to shapely
        self.roadSgtList = []
        
        for feature in roadSgt1:
            roadSgt2 = asShape(feature.shape.__geo_interface__)
            self.roadSgtList.append(roadSgt2)
        
             
        facility0 = shapefile.Reader(facilityShp)
        facility1 = facility0.shapeRecords()
        self.facilityList = []
             
        for feature in facility1:
            facility2 = asShape(feature.shape.__geo_interface__)
            self.facilityList.append(facility2)
        
        #2. setting order
        nearFrontList, facStartNo, rdSegList, facilList = self.setInitialSgt(direction)
        
        #3. finding the nearest front facility
        nxtRd = 0
        for indf, fac in enumerate(facilList):
            for indr, rsgt in enumerate(rdSegList[nxtRd:]):
                intersects = fac.within(rsgt.buffer(1.0))
                nearFrontList[indr+nxtRd][1]=[abs(facStartNo-indf), fac.coords[0][0], fac.coords[0][1]]
                
                if intersects==True:
#                     print "facility="+str(abs(facStartNo-indf))+", road="+str(indr+nxtRd)
                    nxtRd += indr+1
                    break
                   
        # list to dict        
        nearFrontDict={}
        for rd in nearFrontList:
            nearFrontDict[rd[0]]=rd[1]
        print nearFrontDict
        
        #4. writing excel
        exCol = []
        for rd in nearFrontDict.items():
            exCol.append(rd[1])
          
        ex.excelWriteOnExistingFileCol(excelPath, excelSheet, 2, exCol)
    
    def setInitialSgt(self, direction):
        rdSeg = self.roadSgtList
        facil = self.facilityList
        
        segfirstX = list(rdSeg[0].coords)[0][0]
        seglastX = list(rdSeg[-1].coords)[0][0]
        segfirstY = list(rdSeg[0].coords)[0][1]
        seglastY = list(rdSeg[-1].coords)[0][1]
            
        facilfirstX = list(facil[0].coords)[0][0]
        facillastX = list(facil[-1].coords)[0][0]
        facilfirstY = list(facil[0].coords)[0][1]
        facillastY = list(facil[-1].coords)[0][1]
            
        rdSegList = []
        facilList = []
        nearFrontList = []
        
        if direction == "WB":
            segfirst = -segfirstX
            seglast = -seglastX
            facilfirst = -facilfirstX
            facillast = -facillastX
            
        if direction == "EB":
            segfirst = segfirstX
            seglast = seglastX
            facilfirst = facilfirstX
            facillast = facillastX
        
        if direction == "NB":
            segfirst = segfirstY
            seglast = seglastY
            facilfirst = facilfirstY
            facillast = facillastY
            
        if direction == "SB":
            segfirst = -segfirstY
            seglast = -seglastY
            facilfirst = -facilfirstY
            facillast = -facillastY
            
        if segfirst <= seglast:
            for indrow, row in enumerate(rdSeg):
                nearFrontList.append([indrow, [-1, -1, -1]])
                rdSegList.append(row)
#             print "Road Segment - first is the first"
        else:
            for indrow, row in enumerate(reversed(rdSeg)):
                nearFrontList.append([len(rdSeg)-indrow-1, [-1, -1, -1]])
                rdSegList.append(row)
#             print "Road Segment - first is the last"
        
        if facilfirst <= facillast:
            for row in facil:
                facilList.append(row)
            facStartNo = 0
#             print "Facility - first is the first"
        else:
            for row in reversed(facil):
                facilList.append(row)
            facStartNo = len(facil)-1
#             print "Facility - first is the last"
        
        return nearFrontList, facStartNo, rdSegList, facilList        
        
