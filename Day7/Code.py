from enum import Enum

class Tree:
    def __init__(self, name, data, parent = None):
        self.name = name
        self.children = []
        self.data = data
        self.parent = parent
    def add_child(self, node):
        assert isinstance(node, Tree)
        node.parent = self
        self.children.append(node)
    def __repr__(self):
        return str(self.name)
    def __str__(self):
        return str(self.name)
    def get_all_children(self):
        node_list = []
        node_list.append(self)
        if(self.children != None):
            for child in self.children:
                node_list.extend(child.get_all_children())
                
        return node_list
    def get_child(self, name):
        for child in self.children:
            if(child.name == name):
                return child
        return None
    def get_all_child_data(self):
        nodes = self.get_all_children()
        return [node.data for node in nodes]
    def get_root(self):
        if(self.parent == None):
            return self
        else:
            return self.parent.get_root()

class TreeDir(Tree):
    def __init__(self, type, name, data, children = None, parent = None):
        super(TreeDir, self).__init__(name, data, parent)
        self.type = type
    def __repr__(self):
        return str("{}: {}".format(self.type, self.name))
    def get_all_files(self):
        return [node for node in self.get_all_children() if node.type == NodeType.FILE]
    def get_all_dirs(self):
        return [node for node in self.get_all_children() if node.type == NodeType.DIR]
    def size(self):
        if(self.type == NodeType.FILE):
            return self.data
        
        files = self.get_all_files()
        return sum(map(lambda f: int(f.data), files))

class NodeType(Enum):
    FILE = 1
    DIR = 2

def move_dir(currentDir, dir):
    match dir:
        case "..":
            currentDir = currentDir[:currentDir.rfind("/")]
        case "/":
            currentDir = "/"
        case _:
            currentDir += "/" + dir
    
    return currentDir

with open("Day7/Data.txt") as f:
    lines  = [[s for s in line.split(" ")] for line in f.read().split("\n")]
    currentDir = ""
    currentNode  = TreeDir(NodeType.DIR, "/", None)

    for line in lines:
        if(line[0] == "$" and line[1] == "cd"):
            currentDir = move_dir(currentDir, line[2])
            if(line[2] == ".."):
                currentNode = currentNode.parent
            elif(line[2] == "/"):
                currentNode = currentNode.get_root()
            else:
                currentNode = currentNode.get_child(line[2])
        elif(line[0] == "dir"):
            currentNode.add_child(TreeDir(NodeType.DIR, line[1], None,  currentNode))
        elif(str(line[0]).isdigit()):
            currentNode.add_child(TreeDir(NodeType.FILE, line[1], int(line[0]), currentNode))
    
root = currentNode.get_root()
dirs = root.get_all_dirs()
totalSum = 0
for dir in dirs:
    size = dir.size()
    if(size <= 100000):
        totalSum += size

totalSpace = 70000000
spaceRequired = 30000000
usedSpace = root.size()
spaceToDelete = spaceRequired - (totalSpace - usedSpace)

dirSizes = [dir.size() for dir in dirs]
dirSizes.sort()
smallestDir = next(filter(lambda n: n >= spaceToDelete, dirSizes))

print("Answer to Q1: {}".format(totalSum))
print("Answer to Q2: {}".format(smallestDir))