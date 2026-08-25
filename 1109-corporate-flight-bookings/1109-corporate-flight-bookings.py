class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+2)
        for i in bookings:
            ans[i[0]] += i[2]
            ans[i[1]+1] -= i[2]
        for i in range(1,n+1):
            ans[i] += ans[i-1]
        return ans[1:n+1]