class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strs = ["act","pots","tops","cat","stop","hat"]
        '''dict1 = {}
        for key in strs:
            st = "".join(sorted(key));
            if st not in dict1:
                dict1[st] = [];
            dict1[st].append(key);
        return list(dict1.values())'''     # time complexity  O(n * k log k)

        # Method 2
        dict1 = {};
        for word in strs:
            count = [0] * 26; # for a to z, 26 array
            for ec in word:
                count[ord(ec) - ord('a')] += 1

            key = tuple(count);

            if key not in dict1:
                dict1[key] = []
            dict1[key].append(word)
        return list(dict1.values())


