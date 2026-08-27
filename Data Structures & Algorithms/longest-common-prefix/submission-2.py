class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hash_pref = {}
        min_len = 200
        longest_prefix = ''
        for string in strs:
            min_len = min(min_len,len(string))
        for string in strs:
            pref = ''
            hash_pref[''] = hash_pref.get('',0) + 1
            for i in range(min_len):
                pref+=string[i]
                hash_pref[pref] = hash_pref.get(pref,0) + 1
                if hash_pref[pref] == len(strs) and len(pref)>len(longest_prefix):
                    longest_prefix = pref
        return longest_prefix