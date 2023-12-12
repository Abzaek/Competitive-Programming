class UndergroundSystem:

    def __init__(self):
        self.byStation = {}
        self.byID = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.byID[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.byID[id][0], stationName) not in self.byStation:
            self.byStation[(self.byID[id][0], stationName)] = []
        self.byStation[(self.byID[id][0], stationName)].append(t - self.byID[id][1])
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return sum(self.byStation[(startStation, endStation)])/len(self.byStation[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)