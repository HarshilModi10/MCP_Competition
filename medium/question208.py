class Node(object):
    def __init__(self):
        self.is_word = False
        self.child = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root        
        for ch in word:
            if ch not in cur.child: 
                cur.child[ch] = Node()
            cur = cur.child[ch]
            
        cur.is_word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        
        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
            
        return cur.is_word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        
        for ch in prefix:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)