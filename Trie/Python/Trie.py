class TrieNode:
	def __init__(self, alphabet_size, children = None):
		self.alphabet_size = alphabet_size
		self.children = children
		self.words_touching = 0
		self.words_ending = 0

	@classmethod
	def activate(cls, alphabet_size):
		return cls(alphabet_size, [None for i in range(0, alphabet_size)])

class Trie:
	def __init__(self, alphabet_size, character_mapping):
		self.alphabet_size = alphabet_size
		self.character_mapping = character_mapping
		self.root = TrieNode.activate(alphabet_size)

	def add_word(self, word):
		current_node = self.root
		for i, ch in enumerate(word):
			id = self.character_mapping[ch]
			child = current_node.children[id]
			if child == None:
				child = TrieNode.activate(self.alphabet_size)
			child.words_touching += 1
			if i == len(word) - 1:
				child.words_ending += 1
			current_node.children[id] = child
			current_node = current_node.children[id]

	def remove_word(self, word):
		self.remove_word_recursive(self.root, word, 0)

	def remove_word_recursive(self, current_node, word, position):
		if position == len(word):
			return
		id = self.character_mapping[word[position]]
		child = current_node.children[id]
		self.remove_word_recursive(child, word, position + 1)
		child.words_touching -= 1
		if position == len(word) - 1:
			child.words_ending -= 1
		if child.words_touching == 0:
			child = None
		current_node.children[id] = child

	def count_word(self, word):
		current_node = self.root
		for i, ch in enumerate(word):
			id = self.character_mapping[ch]
			child = current_node.children[id]
			if child == None:
				return 0
			if i == len(word) - 1:
				return child.words_ending
			current_node = child
		return 0

	def longest_prefix(self, word):
		current_node = self.root
		for i, ch in enumerate(word):
			id = self.character_mapping[ch]
			child = current_node.children[id]
			if child == None:
				return word[:i]
			current_node = child
		return word