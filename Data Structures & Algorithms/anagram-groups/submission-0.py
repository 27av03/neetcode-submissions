class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # Hash map containing the list of anagrams

        for s in strs:
            count = [0] * 26 # a...z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return list(result.values())