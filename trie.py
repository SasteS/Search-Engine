class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False
        self.broj_ponavljanja_reci = 0

class Trie:
    def __init__(self):
        self.root = TrieNode("*") #moze i ""
    
    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode(letter)
            current_node = current_node.children[letter]
        current_node.is_end_of_word = True
    
    def does_word_exist(self, word):
        if word == "":
            return True
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return current_node.is_end_of_word
    