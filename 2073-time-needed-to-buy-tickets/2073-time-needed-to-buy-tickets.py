class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque()

        for i in range(len(tickets)):
            q.append(i)
        turns = 0


        while tickets[k]>0:
            front = q.popleft()

            tickets[front] -= 1

            if tickets[front] > 0:
                q.append(front)
            turns += 1
        return turns