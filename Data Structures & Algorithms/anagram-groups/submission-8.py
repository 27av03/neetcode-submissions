class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # key will equal a tuple of the count[] array, mapping to the words

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())

        