class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n  = len(senate)
        R = deque()
        D = deque()

        for i in range(n):
            if senate[i] == "R":
                R.append(i)
            else:
                D.append(i)
        

        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r < d:
                R.append(r+n)
            else:
                D.append(d+n)
        if R:
            return "Radiant"
        else:
            return "Dire"
