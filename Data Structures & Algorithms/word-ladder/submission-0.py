class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #edge cases: empty string / same word / endword not valid

        if (beginWord == "") or (beginWord == endWord) or (endWord not in wordList):
            return 0

        def valid_word(word, target):
            counter = 0
            size = len(word)
            for i in range(size):
                if word[i] == target[i]:
                    counter +=1
            if size - counter == 1:
                return True
            else:
                return False
        
        def bfs(start):
            from collections import deque
            queue = deque([(start, 1)])
            visited = set()
            visited.add(start)

            while queue:
                current_word, distance = queue.popleft()
                valid_visits = set(wordList)
                valid_visits = valid_visits - visited
                
                for target_word in wordList:
                    if valid_word(current_word, target_word):
                        if target_word == endWord:
                            return distance + 1
                        if target_word in valid_visits:
                            valid_visits.discard(target_word)
                            visited.add(target_word)
                            queue.append((target_word,distance + 1))
            
            return 0
        return bfs(beginWord)
