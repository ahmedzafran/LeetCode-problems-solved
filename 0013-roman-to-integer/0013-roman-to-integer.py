class Solution:
    def romanToInt(self, s: str) -> int:
        number= {"I":1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s = list(s)
        total = 0
        for i in range(len(s)-1):
            num_1, num_2 = int(number[s[i]]), int(number[s[i+1]]) 
            #print(num_1, num_2)
            if num_1 < num_2:
                total -= num_1
                #print(total)
            else:
                total += num_1
                #print(total)
        total += number[s[-1]]
        return total
        