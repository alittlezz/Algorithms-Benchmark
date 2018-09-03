from Trie import Trie
import sys
import os

if __name__ == "__main__":
	no_file = sys.argv[1]
	dic = {}
	for i in range(ord('a'), ord('z') + 1):
		dic[chr(i)] = i - ord('a')

	trie = Trie(26, dic)

	out = open(os.path.dirname(__file__) + "/../Outputs/output_" + no_file + "_python.out", "w")

	for line in open(os.path.dirname(__file__) + "/../Inputs/input_" + no_file + ".in", "r").readlines()[1:]:
		op, word = line.split()
		if op == "add":
			trie.add_word(word)
		elif op == "remove":
			trie.remove_word(word)
		elif op == "count":
			out.write(str(trie.count_word(word)) + "\n")
		elif op == "lp":
			out.write(trie.longest_prefix(word) + '\n')
