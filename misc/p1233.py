# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
# If a folder[i] is located within another folder[j], it is called a sub-folder of it.
# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 
# Example 1:
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

# Example 2:
# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

# Example 3:
# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 
# Constraints:
# 1 <= folder.length <= 4 * 104
# 2 <= folder[i].length <= 100
# folder[i] contains only lowercase letters and '/'.
# folder[i] always starts with the character '/'.
# Each folder name is unique.

# Time: O(nm), Space: O(nm) --check
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.end = True

    def search(self, prefix):
        cur = self
        for c in prefix:
            if c not in cur.children or cur.end:
                return False
            cur = cur.children[c]
        return True                

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        for f in folder:
            root.addword(f.split("/"))

        res = []
        for f in folder:
            if root.search(f.split("/")):
                res.append(f)   
        return res   
