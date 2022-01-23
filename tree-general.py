
from sys import prefix


class Tree():
    def __init__(self, name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def tree_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level    


    def print_tree(self, datapart):
        space = ' ' * self.tree_level() * 4
        prefixx = space+'|__' 

        if datapart== "name":
            print(prefixx, self.name)
        if datapart == "designation":
            print(prefixx, self.designation)
        elif datapart == "both":
            print(prefixx, self.name, '(', self.designation, ')')
          

        if self.children:
            for child in self.children:
                child.print_tree(datapart)




def build_management_tree():
    root = Tree("Nilupul", "CEO")
    Ch = Tree("Chinmay", "CTO")
    Ge = Tree("Gels","HR Head")

    root.add_child(Ch)
    root.add_child(Ge)

    Vi = Tree("Vishwa", "Infastructure Head")
    Aa = Tree("Aamir", "Application Head")
    Ch.add_child(Vi)
    Ch.add_child(Aa)

    Dh = Tree("Dhaval", "Cloud Manager")
    Ab = Tree("Abhijit", "App Manager")
    Vi.add_child(Dh)
    Vi.add_child(Ab)

    Pi = Tree("Peter","Reqruitement Manager")
    Wa = Tree("Waqar","Policy Manager")
    Ge.add_child(Pi)
    Ge.add_child(Wa)


    return root



if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
