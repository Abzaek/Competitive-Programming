class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenMap = {}
        self.timeList = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenMap[tokenId] = currentTime
        self.timeList[currentTime] += 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenMap:
            if currentTime - self.tokenMap[tokenId] < self.timeToLive:
                self.timeList[self.tokenMap[tokenId]] -= 1
                self.tokenMap[tokenId] = currentTime
                self.timeList[self.tokenMap[tokenId]] += 1
            
    def countUnexpiredTokens(self, currentTime: int) -> int:
        counter = 0
        for i in self.timeList:
            if currentTime - i < self.timeToLive:
                counter += self.timeList[i]

        return counter
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)