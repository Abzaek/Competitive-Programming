class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d = str(eval(a  + " + " + b))
        d = list(d)
        for i in range(len(d) - 1, 0, -1):

            if d[i] >= "2":
                d[i] = str(int(d[i]) - 2)
                d[i - 1] = str(int(d[i -1]) + 1)
        
        if d[0] >= "2":
            d[0] = str(int(d[0]) - 2 )
            d = ["1"] + d

        return "".join(d)


        