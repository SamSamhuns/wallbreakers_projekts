import re
from typing import List
from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return self.mostCommonWord_noregex(paragraph, banned)

    def mostCommonWord_noregex(self, paragraph: str, banned: List[str]) -> str:
        punc=set("!?',;. ")
        banned_set=set(banned)
        word_count=defaultdict(int)

        max_tuple=('', 0)
        temp_list=[]
        for i, char in enumerate(paragraph):
            if char in punc or i == len(paragraph) - 1:
                if i == len(paragraph) - 1 and char.isalpha():
                    temp_list.append(char.lower())

                if temp_list != []:
                    word=''.join(temp_list)
                    if word in banned_set:
                        temp_list=[]
                        continue

                    word_count[word] += 1
                    if word_count[word] > max_tuple[1]:
                        max_tuple=(word, word_count[word])
                temp_list=[]
            else:
                temp_list.append(char.lower())

        return max_tuple[0]

    def mostCommonWord_regex(self, paragraph: str, banned: List[str]) -> str:
        wd={}
        banned=set(banned)
        paragraph=filter(None, re.split("[,?!;.\' ]+", paragraph))
        maxc, maxw=0, ''
        for word in paragraph:
            word=word.lower()
            if word not in banned:
                wd[word]=wd.get(word, 0) + 1
                if wd[word] > maxc:
                    maxc=wd[word]
                    maxw=word
        return maxw


"""
No regex solution
Runtime: O(2N) ~ O(N)
Space: O(w) w = no of words

Runtime: 28 ms, faster than 89.21% of Python3 online submissions for Most Common Word.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Most Common Word.
"""
