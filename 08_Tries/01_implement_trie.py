"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
Difficulty: Medium

Implement the Trie class:
    - Trie()              Initializes the trie object.
    - insert(word)        Inserts the string word into the trie.
    - search(word)        Returns true if word is in the trie.
    - startsWith(prefix)  Returns true if any word has the given prefix.

Examples:
    Input: ["Trie","insert","search","search","startsWith","insert","search"]
           [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
    Output: [null,null,true,false,true,null,true]

Constraints:
    - 1 <= word.length, prefix.length <= 2000
    - word and prefix consist of lowercase English letters.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    # Hint: Each node has a dict of children (char -> TrieNode) and an
    # end_of_word flag. Insert walks/creates nodes. Search walks and checks
    # end_of_word. startsWith walks without checking end_of_word.

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass
