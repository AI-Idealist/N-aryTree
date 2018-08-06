class Node:
    def __init__(self, key, value):
        self.key = key
        self.parent = None
        self.children = []
        self.value = value

    def children(self):
        return self.children
    
    def add_child(self, node):
        self.children.append(node)
        
    def rem_child(self,node):
        self.children.remove(node)    
        
    def rev_children(self):
        children = self.children[:]
        children.reverse()
        return children
    
    def set_parent(self, node):
        self.parent = node
       
       
 class Tree:
    def __init__(self, root):
        self.root = root
        self.cur_node = self.root
                        
    def breadth_first(self,root):
        visited = []
        stack = [root] 
        while stack:
            cur_node = stack[0]
            
            stack = stack[1:]
            visited.append(cur_node)
            for child in cur_node.children:
                stack.append(child)            
        return visited 
    
    def depth_first(self,root):
        visited = []
        stack = [root]
        while stack:
            cur_node = stack[0]
            stack = stack[1:]
            visited.append(cur_node)        
            for child in cur_node.rev_children():
                stack.insert(0, child)
        return visited

    def find_node(self,key,node):
        if node.key == key:
                
                return node
        for child in node.children:
                temp = self.find_node(key,child)            
                if temp:
                    return temp
    
            
    # voeg node toe indien key niet aanwezig
    def add_node(self,new):
        if new and self.cur_node:
            if not self.find_node(new.key,self.root):
                self.cur_node.add_child(new)
                new.set_parent(self.cur_node)
                self.cur_node = new
            
         
    # wrapper voeg node toe indien key niet aanwezig en parentkey wel aanwezig
    def wadd_node(self,key, parentkey, value):
        node = self.find_node(key,self.root)
        if node:
            return
        
        parent = self.find_node(parentkey,self.root)
        if parent:
            print(parent.key)
            self.cur_node = parent
            self.add_node(Node(key,value))
      
    
    def winsert_node(self,key, parentkey, value):
        node = self.find_node(key,self.root)
        if node:
            return
        
        parent = self.find_node(parentkey,self.root)
        if parent:
            self.cur_node = parent
            self.insert_node(Node(key,value))
        
    def insert_node(self,new):
        if new and self.cur_node:
            parent = self.cur_node.parent
            children = self.cur_node.children                        
        
        if parent and children:
            
            new.set_parent(parent)
            parent.add_child(new)
                            
            self.cur_node.set_parent(new) 
            new.add_child(self.cur_node)
            
            parent.rem_child(self.cur_node)                       
            self.cur_node = new
      
                         
    # verwijder node indien node met key aanwezig, maar niet root is.
    # de root heeft geen ouder, dus kinderen kunnen niet daaraan gekoppeld worden
    def del_node(self):
        if self.cur_node:
            if not self.cur_node.parent:
                return
            if not self.cur_node.children:
                p = self.cur_node.parent
                p.rem_child(self.cur_node)
                self.cur_node = p
            else:
                print(self.cur_node.key)
                p = self.cur_node.parent
                print(p.key)
                
                for child in self.cur_node.children:
                    child.set_parent(p)
                    p.add_child(child)
                    
                p.rem_child(self.cur_node)
                self.cur_node = p
        
    def wdel_node(self,key):
        node = self.find_node(key,self.root)
        if node:
            self.cur_node = node
            self.del_node()
    
    def print_tree(self):
        node_list = self.breadth_first(self.root)
        for node in node_list:
            if not node.parent:
                str = "None"
            else:
                str = node.parent.key                 
            print("%s;%s;%s" %(node.key,str,node.value))
           
       
    def serialize(self):
        f = open("treev4.txt", "w")
        node_list = self.breadth_first(self.root)
        for node in node_list:
            if not node.parent:
                str = "None"
            else:
                str = node.parent.key                
            print("%s;%s;%s" %(node.key,str, node.value),file=f )
        
        f.close()
        
        
    def deserialize(self):
        f = open("treev4.txt", "r")
        line = f.readline()
        line = line.strip('\n')
        data = line.split(";")
                
        self.root = Node(data[0],self.replaceNone(data[1]),self.replaceNone(data[2]))
        for line in f:
            line = line.strip('\n')
            data = line.split(";")
            self.add_node(data[0],self.replaceNone(data[1]),self.replaceNone(data[2]))
        
        
    def maxDepth(self, node):
        print(node.key)
        if node is None:
            return 0 ; 
        else:
            t = [0]
            for child in node.children:
                depth = self.maxDepth(child)
                t.append(depth)
            return max(t) + 1

    @classmethod
    def replaceNone(self,line):
        if line == "None":
            return None
        else: 
            return line
            
            
tree = Tree(Node("Albert","is my father"))
tree.add_node(Node("Gerard","tht is me"))
tree.cur_node = tree.root
tree.add_node(Node("Sake","is my borther"))
tree.add_node(Node("Anandi","is my niece"))

tree.wadd_node("Wodan","Gerard","is my dog")
tree.wadd_node("the cats", "Gerard", "do not like me")

tree.print_tree()
tree.cur_node = tree.find_node("Gerard", tree.root)
tree.insert_node(Node("Gerda", "is lief"))
#tree.winsert_node("Gera","Gerard","is tweeling")
print()
tree.print_tree()
tree.winsert_node("Gera","Gerard","is tweeling")
tree.print_tree()
tree.cur_node = tree.find_node("Sake", tree.root)
tree.wdel_node("Sake")
tree.print_tree()
