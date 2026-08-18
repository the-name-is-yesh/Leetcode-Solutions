class Solution:



    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a=[]
        for i in range(left,right+1):
            j=i
            c=0
            d=0
            while(j>0):
                dig=j%10
                j//=10
                d+=1
                if dig==0:
                    break
                if i%dig==0:
                    c+=1
            if c==d:
                a.append(i)
        return a
