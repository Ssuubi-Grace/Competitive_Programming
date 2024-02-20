class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = "qwertyuiop"
        sec = "asdfghjkl"
        third = "zxcvbnm"
        
        rows = [set(row) for row in [first, sec, third]]
        valid_words = []
        for word in words:
            word_lower = word.lower()
            if set(word_lower) <= rows[0]:
                valid_words.append(word)
            elif set(word_lower) <= rows[1]:
                valid_words.append(word)
            elif set(word_lower) <= rows[2]:
                valid_words.append(word)
        return valid_words
