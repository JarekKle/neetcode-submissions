class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_hash = {}
        for i in range(len(strs)):
            s_word = str(sorted(strs[i]))
            if ana_hash.get(s_word) is None:
                ana_hash[s_word] = [strs[i]]
            else:
                ana_hash[s_word].append(strs[i])
        return list(ana_hash.values())