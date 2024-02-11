class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        a = []
        s = []
        for i in range(len(words)):
            s.append(''.join(sorted(words[i])))
        print(s)
        a.append(words[0])
        for i in range(1,len(words)):
            if (s[i] != s[i-1]):
                a.append(words[i])
        return a