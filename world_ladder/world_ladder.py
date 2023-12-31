from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    result = []
    wordList = set(wordList)

    if endWord not in wordList:
        return result

    # Helper function to build the graph during BFS
    def buildGraph():
        graph = defaultdict(list)
        visited = set()
        queue = deque([(beginWord, [beginWord])])

        while queue:
            currentWord, path = queue.popleft()
            visited.add(currentWord)

            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = currentWord[:i] + c + currentWord[i+1:]
                    if nextWord in wordList and nextWord not in visited:
                        graph[currentWord].append(nextWord)
                        if nextWord != endWord:
                            queue.append((nextWord, path + [nextWord]))

        return graph

    # Helper function to perform BFS and backtracking
    def bfsAndBacktrack():
        graph = buildGraph()
        queue = deque([(beginWord, [beginWord])])
        visited = set()

        while queue:
            currentWord, path = queue.popleft()
            visited.add(currentWord)

            for neighbor in graph[currentWord]:
                if neighbor == endWord:
                    result.append(path + [endWord])
                elif neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    bfsAndBacktrack()
    return result

# Example Usage:
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

result = findLadders(beginWord, endWord, wordList)
print(result)
