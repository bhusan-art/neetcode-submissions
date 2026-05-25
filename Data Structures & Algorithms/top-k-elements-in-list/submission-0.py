class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}      #[1,2,3,1,2,2]
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        sort = sorted(dict1.items(),key = lambda x:x[1] ,reverse=True)
        print(sort)

        ans = []

        for i in range(k):
            ans.append(sort[i][0])

        return ans


        