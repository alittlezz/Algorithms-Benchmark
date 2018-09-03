#include "Trie.h"

#include <fstream>
#include <iostream>
#include <vector>

int main(int argc, char** argv)
{
    MAP mp;
    for(int i = 0;i < 26;i++){
        char ch = (char)i + 'a';
        mp[ch] = i;
    }
    Trie trie(26, mp);
    std::string no_file(argv[1]);
    std::ifstream in("./Inputs/input_" + no_file + ".in");
    std::ofstream out("./Outputs/output_" + no_file + "_c++.out");
    int n;
    in >> n;
    for(int i = 0;i < n;i++){
        std::string op, word;
        in >> op >> word;
        if(op == "add"){
            trie.add_word(word);
        }else if(op == "remove"){
            trie.remove_word(word);
        }else if(op == "count"){
            out << trie.count_word(word) << "\n";
        }else if(op == "lp"){
            out << trie.longest_prefix(word) << '\n';
        }
    }
    in.close();
    out.close();
    return 0;
}
