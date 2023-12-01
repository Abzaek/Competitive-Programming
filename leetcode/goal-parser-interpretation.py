class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        count = 1
        for i in command:
            if i == "G":
                ans += "G"

            if count == len(command):
                break
            if i == "(":
                if command[count] == ")":
                    ans += "o"
                else:
                    ans += "al"
            count += 1
        return ans

        