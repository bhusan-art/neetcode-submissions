class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #######Brute force method #############
        a = [0] * len(temperatures);              # 30,8,3,36
        
        for i in range(len(temperatures)):   
            for j in range(i+1,len(temperatures)):  
                if temperatures[j] > temperatures[i]:           
                    a[i] = j - i
                    break
        return a

        ######Mono-Stack Method#########
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > tempeartures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)


        return ans


                

                


