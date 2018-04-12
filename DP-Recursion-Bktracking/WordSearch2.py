class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i+1j*j : c for i, row in enumerate(board) for j, c in enumerate(row)}
        found = []
        
        def search(node, z, word):
            if node.pop(None,None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4):
                    search(node[c], z+1j**k, word+c)
                board[z] = c    
        for z in board:
            search(root,z,'')
        return found