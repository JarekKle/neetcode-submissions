class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hash_pref = {}
        min_len = 200
        for string in strs:
            min_len = min(min_len,len(string))
        for string in strs:
            pref = ''
            hash_pref[''] = hash_pref.get('',0) + 1
            for i in range(min_len):
                pref+=string[i]
                hash_pref[pref] = hash_pref.get(pref,0) + 1
        longest_prefix = ''
        for key, value in hash_pref.items():
            if value==len(strs):
                if len(key)>len(longest_prefix):
                    longest_prefix=key
        return longest_prefix