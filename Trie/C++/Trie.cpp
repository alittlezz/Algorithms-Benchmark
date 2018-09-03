#include "Trie.h"

Trie::Trie(short _alphabet_size, MAP _character_mapping){
    alphabet_size = _alphabet_size;
    character_mapping = _character_mapping;
    root = new TrieNode(alphabet_size);
}

Trie::~Trie(){

}

void Trie::add_word(std::string &word){
    TrieNode *current_node = root;
    for(int i = 0;i < word.size();i++){
        TrieNode** child = &current_node->children[character_mapping[word[i]]];
        if((*child) == NULL){
            *child = new TrieNode(alphabet_size);
        }
        (*child)->words_touching++;
        if(i == word.size() - 1){
            (*child)->words_ending++;
        }
        current_node = *child;
    }
}

void Trie::remove_word(std::string &word){
    remove_word_recursive(root, word, 0);
}

void Trie::remove_word_recursive(TrieNode *&current_node, std::string &word, int position){
    if(position == word.size()){
        return;
    }
    TrieNode** child = &current_node->children[character_mapping[word[position]]];
    remove_word_recursive(*child, word, position + 1);
    (*child)->words_touching--;
    if(position == word.size() - 1){
        (*child)->words_ending--;
    }
    if((*child)->words_touching == 0){
        delete (*child);
        *child = NULL;
    }
}

int Trie::count_word(std::string &word){
    TrieNode *current_node = root;
    for(int i = 0;i < word.size();i++){
        TrieNode** child = &current_node->children[character_mapping[word[i]]];
        if((*child) == NULL){
            return 0;
        }
        if(i == word.size() - 1){
            return (*child)->words_ending;
        }
        current_node = *child;
    }
    return 0;
}

std::string  Trie::longest_prefix(std::string &word){
    TrieNode *current_node = root;
    for(int i = 0;i < word.size();i++){
        TrieNode** child = &current_node->children[character_mapping[word[i]]];
        if((*child) == NULL){
            return word.substr(0, i);
        }
        current_node = *child;
    }
    return word;
}
