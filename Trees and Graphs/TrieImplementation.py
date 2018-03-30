class TrieNode(object):
	"""docstring for TrieNode"""
	def __init__(self):
		self.children = {}
		self.endOfWord = False

	self.root = TrieNode()

	def insert(self, word):
		current = self.root
		for i in range(len(word)):
			if word[i] not in current.children:
				current.children[word[i]] = TrieNode()
			current = current.children[word[i]]
		current.endofWord = True

	def search(self, word):
		current = self.root
		for i in range(len(words)):
			if word[i] not in current.childern:
				return False
			current = current.children[word[i]]
		return current.endOfWord

	def delete(self,word):
		deleteHelper(root, word, 0)

	def deleteHelper(current, word, index):
		if index == len(word):
			if current.endofWord == True:
				return False
			current.endofWord = False
			return len(current.children.keys()) == 0

		if word[i] not in current.children:
			return False

		shouldDelete = delete(current.children[word[i]], word, index+1)

		if shouldDelete:
			current.children.del(word[i])
			return len(current.children.keys()) == 0
		return False









		