# N-aryTree
N-ary Tree implementation

This N-ary tree implementation provides functions and variables for programmers who need to maintain information in a tree-like structure.

N-aray tree entails:
- information is contained in nodes
- A Node contains 0,1 of children
- A Node has 1 parent
- The relation between parent and its childrens is set by hand (unlike a binare search tree)
- every Node has a unique key, you can use to identify the node
- The first Node is called root and has no parent.

This tree has two variables available for the programmer:
- root. This varable always points to the root node.
- current_node points to the node you want to apply a function to. After calling a function f.e. del_node the current node points to anther node.

There are several categories of functions:

modifying the tree
- add_node
- del_node
- insert_node

traversing the tree
- breath_first
- depth_first
- find_node

show and save the tree
- print_tree
- serialize
- deserialize

return information about the tree
- maxdepth

There also some convience-functions(wrappers)
- wadd_node (creates a Node based on key and value, the Node is automatically created)
- wdel_node (deletes a Node based on key-value)
- winsert_node (inserts a Node based on key and value,the Node is automaticly created) 
