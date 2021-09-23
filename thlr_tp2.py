from graphviz import Digraph
from display_automaton import export_automaton


# A tree-based representation of regular expresssions
class RegEx:

    def __init__(self, symbol, children):
        self.symbol = symbol
        self.children = children

    def to_string(self):
        if self.symbol == "*":
            return "(" + self.children[0].to_string() + ")*"
        elif self.symbol == "+":
            return self.children[0].to_string() + "+" \
                + self.children[1].to_string()
        elif self.symbol == ".":
            return self.children[0].to_string() + self.children[1].to_string()
        else:
            return self.symbol

    # Question 4
    # Output an epsilon-NFA equivalent to the regular expression
    def to_enfa(self):
        pass


# Non-deterministic finite automata with epsilon transitions
class ENFA:

    def __init__(self, all_states, initial_states, final_states,
                 alphabet, edges):
        # States: a set of integers
        self.all_states = set(all_states)
        # The alphabet: a set of strings
        # "" stands for epsilon
        self.alphabet = set(alphabet)
        self.alphabet.add("")
        # Initial and final states: two sets of integers
        self.initial_states = set(initial_states).intersection(self.all_states)
        self.final_states = set(final_states).intersection(self.all_states)
        # There must be an initial state; if there isn't, an initial state 0
        # is added
        if not self.initial_states:
            self.initial_states.add(0)
            self.all_states.add(0)
        # Edges: a dictionnary (origin, letter): set of destinations
        self.next_states = {(state, letter): set()
                            for state in self.all_states
                            for letter in self.alphabet}
        for edge in set(edges):
            if (edge[0] in self.all_states) and (edge[2] in self.all_states) \
                    and (edge[1] in self.alphabet):
                self.next_states[(edge[0], edge[1])].add(edge[2])

    # Question 1
    # Add a new state to the automaton
    def new_state(self):
        value = max(self.all_states)
        self.all_states.add(value)
        self.next_states = {(state, letter): set()
                for state in self.all_states
                for letter in self.alphabet}
        return value
        pass

    # Question 2
    # Add a new letter 'letter' to the automaton
    def new_letter(self, letter):
        self.alphabet.add(letter)
        self.next_states = {(state,letter): set()
                for state in self.all_states
                for letter in self.alphabet}
        pass

    # Question 3
    # Insert the automaton matched to the regular expression 'reg_ex'
    # between the two states 'origin' and 'destination' according to
    # Thompson's algorithm
    def convert_reg_ex(self, origin, destination, reg_ex):
        #print(reg_ex.to_string())
        if reg_ex.symbole == ".":
            one = self.new_state()
            two = self.new_state()
            self.edges.append((one,"",two))
            convert_reg_ex(self,origin,one,reg_ex.children[0])
            convert_reg_ex(self,two,destination,reg_ex.children[1])
            pass
        elif(reg_ex.symbole == "+"):
            one = self.new_state()
            two = self.new_state()
            three = self.new_state()
            four = self.new_stats()
            self.edges + [(origin,"",one),(origin,"",two),
                    (three,"",destination),(four,"",destination)]
            convert_reg_ex(self,one,three,reg_ex.children[0])
            convert_reg_ex(self,two,four,reg_ex.children[1])
            pass
        elif(reg_ex.symbole == "*"):
            one = self.new_state()
            two = self.new_state()
            self.edges.append((two,"",one))
            self.edges.append((origin,"",destination))
            self.edges.append((one,"",two))
            self.edges.append((two,"",destination))
            convert_reg_ex(self,one,two,reg_ex.children[0])
            pass
        else:
            self.new_letter(reg_ex.symbole)
            self.edges.append((origin,reg_ex.symbole,destination))
            pass

        self.next_states = {(state, letter): set()
                for state in self.all_states
                for letter in self.alphabet}
        pass

    # Question 5
    # Returns the epsilon forward closure of a state 'origin'
    def epsilon_reachable(self, origin):
        pass

    # Question 6
    # Returns a NFA equivalent to the epsilon NFA by performing a backward
    # removal of epsilon transitions
    def to_nfa(self):
        pass


# Non-deterministic finite automaton
class NFA:

    def __init__(self, all_states, initial_states, final_states,
                 alphabet, edges):
        # States: a set of integers
        self.all_states = set(all_states)
        # The alphabet: a set of strings
        # "" stands for epsilon
        self.alphabet = set(alphabet)
        if "" in self.alphabet:
            self.alphabet.remove("")
        # Initial and final states: two sets of integers
        self.initial_states = set(initial_states).intersection(self.all_states)
        self.final_states = set(final_states).intersection(self.all_states)
        # There must be an initial state; if there isn't, an initial state 0
        # is added
        if not self.initial_states:
            self.initial_states.add(0)
            self.all_states.add(0)
        # Edges: a dictionnary (origin, letter): set of destinations
        self.next_states = {(state, letter): set()
                            for state in self.all_states
                            for letter in self.alphabet}
        for edge in set(edges):
            if (edge[0] in self.all_states) and (edge[2] in self.all_states) \
                    and (edge[1] in self.alphabet):
                self.next_states[(edge[0], edge[1])].add(edge[2])


# =================================== TESTS =============================

base = ENFA([0, 1, 2], [0], [1], ["a", "b"], [(0, "a", 1), (0, "", 1),
(1, "b", 2), (2, "", 0)])
# empty = ENFA([],[],[],[],[]) -> does it exist ?

a = RegEx("a", [])
b = RegEx("b", [])
c = RegEx("c", [])


a_star = RegEx("*", [a])

bc = RegEx(".", [b, c])

e = RegEx("+", [a_star, bc])

'''
[0,1,2] -> states
[0] -> init states
[1] -> final states
["a","b"] -> alphabet
[(0, "a", 1), (0, "", 1),(1, "b", 2), (2, "", 0)] -> edges 
'''

base.new_state()
base.convert_reg_ex(0,3,bc)
export_automaton(base, "base")
