#ifndef TRIE_H
#define TRIE_H

#include <unordered_map>
#include <cstring>
#include <string>
#include <math.h>

typedef std::unordered_map <char, short> MAP;

class TrieNode{
    public:
        TrieNode();
        TrieNode(short _alphabet_size){
            alphabet_size = _alphabet_size;
            children = new TrieNode*[alphabet_size];
            for(int i = 0;i < alphabet_size;i++){
                children[i] = NULL;
            }
        }
        ~TrieNode(){
            words_touching = 0;
            words_ending = 0;
            delete children;
        }

        int words_touching = 0;
        int words_ending = 0;
        TrieNode **children;
    private:
        short alphabet_size;
};

class Trie{
    public:
        Trie(short alphabet_size, MAP _character_mapping);
        ~Trie();

        void add_word(std::string &word);
        void remove_word(std::string &word);
        void remove_word_recursive(TrieNode *&current_node, std::string &word, int position);
        int count_word(std::string &word);
        std::string longest_prefix(std::string &word);
    private:
        short alphabet_size;
        MAP character_mapping;
        TrieNode *root;
};

#endif // TRIE_H
