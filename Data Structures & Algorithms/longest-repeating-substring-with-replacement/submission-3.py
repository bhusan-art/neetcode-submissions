class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        longest = 0

        for right in range(len(s)):

            # character count 
            count[s[right]] = count.get(s[right],0) + 1

            #calculating the frequency in current windows
            max_freq = max(count[s[right]],max_freq)
            
            # If too many replacements are needed, shrink the window
            while (right-left+1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            longest = max(right-left+1,longest)
        return longest

