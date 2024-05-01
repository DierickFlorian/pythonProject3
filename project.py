import csv
import math
class Mushroom :
    def __init__ ( self , edible : bool ):
        self.edible = edible
        self.attributes = {}
# si un champignon est comestible
    def is_edible ( self ) -> bool :
        return self.edible
    def add_attribute ( self , name : str , value : str ) -> None :
        self.attributes[name] = value
    def get_attribute ( self , name : str ) -> str :
        return self.attributes[name]
def load_dataset(path:str) -> list[Mushroom]:
    res = []
    with open(path, mode='r') as csvfile:
        lecteur_csv = csv.DictReader(csvfile)
        for ligne in lecteur_csv:
            edible = ligne['edible']
            if edible == 'Yes':
                edible = True
            else:
                edible = False
            res.append(Mushroom(edible))

    return res


class Node :
    def __init__ ( self , criterion : str , is_leaf : bool = False ):
        self.criterion = criterion
        self.leaf = is_leaf
        self . edges_ = [] # liste des arcs du noeud
    def is_leaf ( self ) -> bool :
        return self.leaf
    def add_edge ( self , label : str , child : " Node ") -> None :
        edge = Edge(self,child,label)
        self.edges_.append(edge)
class Edge :
    def __init__ ( self , parent : Node , child : Node , label : str ):
        self . parent_ = parent
        self . child_ = child
        self . label_ = label

def get_labels_attribute(attribute, mushrooms):
    res = []
    for mushroom in mushrooms:
        if mushroom.get_attribute(attribute) not in res:
            res.append(mushroom.get_attribute(attribute))
    return res
def get_gain(attribute,mushrooms,entropy):

    labels = get_labels_attribute(attribute,mushrooms)
    for label in labels:
        for mushroom in mushrooms:
            if mushroom.get_attribute(attribute) == label:
                liste.append(mushroom)


def build_decision_tree(mushrooms: list[Mushroom]) -> Node:
    labels = []
    entropy = find_entropy(mushrooms)
    attribute_name = mushrooms[0].attributes.keys()
    liste = []


    for attribute in attribute_name:
        noeud = Node(attribute)
        for mushroom in mushrooms:
            if mushroom.get_attribute(attribute) not in labels:
                labels.append(mushroom.get_attribute(attribute))

        for label in labels:
            for mushroom in mushrooms:
                if mushroom.get_attribute(attribute)== label:
                    liste.append(mushroom)
            final = find_entropy(liste) * truc
        gain_info = entropy - final


    else:
        for i in mushrooms
def find_entropy(mushrooms: list[Mushroom]):
    edible_mushroom = 0
    for mushroom in mushrooms:
        if mushroom.is_edible():
            edible_mushroom += 1
    py = edible_mushroom/ len(mushrooms)
    if py == 0 or py == 1:
        return 0
    else:
        value = (1-py)/py
        return py * math.log(value,2) - math.log((1-py),2)

            

print(load_dataset('mushrooms.csv'))


