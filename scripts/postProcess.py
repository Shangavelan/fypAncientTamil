import os

class WordBreak(object):
    def __init__(self):
        self.children = []
        self.leafNode = False

    def getTrieNode(self):
        temp = WordBreak()
        temp.children = []
        for i in range(26):
            temp.children.append(None)
        temp.leafNode = False
        return temp

    def search(self, root, x):
        tNode = root
        for i in x:
            idx = ord(i) - 97
            if tNode.children[idx] == None:
                return False
            tNode = tNode.children[idx]
        if tNode and tNode.leafNode:
            return True

    def insertTrieNode(self, root, x):
        x = str(x)
        tNode = root
        for i in x:
            index = ord(i) - 97
            if tNode.children[index] == None:
                tNode.children[index] = self.getTrieNode()
            tNode = tNode.children[index]
        tNode.leafNode = True
		
        # this function checks if it is possible 
        # to do a wordbreak
    def isPossibleWordBreak(strr, root):
        l = len(strr)
        if(l == 0):
            return True
        for i in range(1, l+1):
            if(root.search(root, strr[:i]) and isPossibleWordBreak(strr[i:], root)):
                return True
            return False
        
#driver code

# creating object of WordBreak() class
ob = WordBreak()
# calling our wordBreak function
ans = ob.wordBreak(string,["உடையார"])
# displaying results
print(ans)