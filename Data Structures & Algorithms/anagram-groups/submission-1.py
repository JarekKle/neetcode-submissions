class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_hash = {}
        out = []
        for i in range(len(strs)):
            s_word = str(sorted(strs[i]))
            if ana_hash.get(s_word) is None:
                ana_hash[s_word] = [i]
            else:
                ana_hash[s_word].append(i)
        for value in ana_hash.values():
            ans = []
            for index in value:
                ans.append(strs[index])
            out.append(ans)
        return out