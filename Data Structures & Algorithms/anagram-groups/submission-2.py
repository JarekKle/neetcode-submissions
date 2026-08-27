class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_hash = {}
        out = []
        for i in range(len(strs)):
            s_word = str(sorted(strs[i]))
            if ana_hash.get(s_word) is None:
                ana_hash[s_word] = [strs[i]]
            else:
                ana_hash[s_word].append(strs[i])
        for value in ana_hash.values():
            ans = []
            for text in value:
                ans.append(text)
            out.append(ans)
        return out