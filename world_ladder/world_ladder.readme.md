This is another hard question 

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].


This is BFS solution you want to backtrack to reconstruct the paths 

Here's a general outline of the approach:

Preprocess the Dictionary:

Convert the wordList into a set for faster lookup.
Create an adjacency list to represent the graph of valid transformations.
BFS to Build the Graph:

Perform a BFS starting from beginWord to build the graph.
Keep track of the distance from the beginWord to each word.
Backtracking to Reconstruct Paths:

Use backtracking to reconstruct the paths from beginWord to endWord using the graph and distance information.
At each step, explore all valid neighbors and continue the path.
Optimization:

Instead of reconstructing paths from scratch, build paths incrementally during BFS.
Use a queue of partial paths to efficiently explore and generate valid sequences.


here is the psuedo code 

function findLadders(beginWord, endWord, wordList):
    result = []  # To store the final sequences
    wordList = set(wordList)  # Convert wordList to a set for faster lookup
    if endWord not in wordList:
        return result  # No transformation sequence possible

    # Helper function to build the graph during BFS
    def buildGraph():
        # Implementation to build the graph (adjacency list)
        # ...

    # Helper function to perform BFS and backtracking
    def bfsAndBacktrack():
        # Implementation of BFS and backtracking
        # ...

    # Call the BFS and backtracking function
    bfsAndBacktrack()

    return result
