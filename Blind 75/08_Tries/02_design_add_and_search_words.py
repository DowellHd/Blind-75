"""
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/
Difficulty: Medium

Design a data structure that supports:
    - addWord(word)    Adds word to the data structure.
    - search(word)     Returns true if any string matches word.
                       '.' matches any single character.

Examples:
    Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
           [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output: [null,null,null,null,false,true,true,true]

Constraints:
    - 1 <= word.length <= 25
    - word consists of lowercase English letters.
    - search word may contain '.' which matches any letter.
"""


class WordDictionary:
    # Hint: Trie + DFS for wildcard '.'. On '.', recurse into all children.
    # On a normal character, follow the specific child.

    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass
