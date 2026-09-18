class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if all(word.isalpha() for word in strs) and len(strs) > 1:
            smallest_word = min(len(word) for word in strs)
            first_word = strs[0]
            remaining_words = strs[1:]
            answer = list()
            for _ in range(smallest_word):
                if any(x[0] != first_word[0] for x in remaining_words):
                    if len(answer) == 0:
                        return ""
                    else:
                        return ''.join(answer)
                else:
                    answer.append(first_word[0])
                    for i, word in enumerate(remaining_words):
                        word = list(word)
                        word.pop(0)
                        remaining_words[i] = ''.join(word)
                    first_word = list(first_word)
                    first_word.pop(0)
                    first_word = ''.join(first_word)
            return ''.join(answer)
        elif len(strs) == 1:
            return strs[0]            

        else:
            return ""
