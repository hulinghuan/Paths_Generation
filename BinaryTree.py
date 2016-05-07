import sys
import pdb
import copy

class BinaryTree:
    def __init__(self, id):
        self.id = id
        self.childs = []
        self._travelednodes = []
        self._loopcount = 0

    # Return True if this is a leaf node, vice versa
    def isleaf(self):
        if len(self.childs) == 0:
            return True
        else:
            return False
    
    # Generate all paths, and print them to stdout
    def print_all_possible_paths(self):
        self._travelednodes.append(self)
        for eachchild in self.childs:
            clonedchild = copy.deepcopy(eachchild)
            if clonedchild.id < self.id:
                # Make sure for, while, do while, etc. only loop once
                if clonedchild._loopcount < 1:
                    clonedchild._loopcount += 1
                    clonedchild._travelednodes = [node for node in self._travelednodes]
                    clonedchild.generate_possible_paths()
                else:
                    continue
            else:
                clonedchild._travelednodes = [node for node in self._travelednodes]
                clonedchild.generate_possible_paths()
        if self.isleaf():
            for each_traveled_node in self._travelednodes:
                sys.stdout.write(str(each_traveled_node.id))
            print ""
    
    # Generate all paths, save it to "generatedpaths" parameters
    # args : 
    #       generatedpaths - list
    def generate_all_possible_paths(self, generatedpaths):
        self._travelednodes.append(self)
        for eachchild in self.childs:
            clonedchild = copy.deepcopy(eachchild)
            if clonedchild.id < self.id:
                # Make sure for, while, do while, etc. only loop once
                if clonedchild._loopcount < 1:
                    clonedchild._loopcount += 1
                    clonedchild._travelednodes = [node for node in self._travelednodes]
                    clonedchild.generate_all_possible_paths(generatedpaths)
                else:
                    continue
            else:
                clonedchild._travelednodes = [node for node in self._travelednodes]
                clonedchild.generate_all_possible_paths(generatedpaths)
        if self.isleaf():
            generatedpaths.append(self._travelednodes)

if __name__ == '__main__':
    A = BinaryTree(1)
    B = BinaryTree(2)
    C = BinaryTree(3)
    D = BinaryTree(4)
    E = BinaryTree(5)
    F = BinaryTree(6)
    G = BinaryTree(7)
    A.childs.append(B)
    B.childs.append(C)
    B.childs.append(F)
    C.childs.append(D)
    C.childs.append(E)
    D.childs.append(C)
    E.childs.append(B)
    generatedpaths = []
    A.generate_all_possible_paths(generatedpaths)
    for eachpath in generatedpaths:
        for eachnode in eachpath:
            sys.stdout.write(str(eachnode.id))
        print ""

