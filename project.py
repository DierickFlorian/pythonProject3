import csv
import math
class Mushroom :
    def __init__(self, edible : bool):
        self.edible = edible
        self.attributes = {}
# si un champignon est comestible
    def is_edible(self) -> bool :
        return self.edible
    def add_attribute ( self , name : str , value : str ) -> None :
        self.attributes[name] = value
    def get_attribute ( self , name : str ) -> str :
        return self.attributes[name]

def load_dataset(path:str) -> list[Mushroom]:
    """
    Fonction pour charger le dataset de champignons à partir d'un fichier CSV
    """
    res = []
    with open(path, mode='r') as csvfile:
        lecteur_csv = csv.DictReader(csvfile)
        for ligne in lecteur_csv:
            edible = ligne['edible']
            if edible == 'Yes':
                edible = True
            else:
                edible = False
            mushroom = Mushroom(edible)
            for attribute in list(ligne.keys ())[1:]:
                mushroom.add_attribute(attribute, ligne[attribute])
            res.append(mushroom)
    return res


class Node :
    def __init__ ( self , criterion : str , is_leaf : bool = False ):
        self.criterion_ = criterion
        self.leaf = is_leaf
        self . edges_ = [] # liste des arcs du noeud
    def is_leaf ( self ) -> bool :
        return self.leaf
    def add_edge ( self , label : str , child) -> None :
        edge = Edge(self,child,label)
        self.edges_.append(edge)
class Edge :
    def __init__ ( self , parent : Node , child : Node , label : str ):
        self . parent_ = parent
        self . child_ = child
        self . label_ = label

def get_labels_attribute(attribute, mushrooms):
    """
    Fonction pour obtenir les labels d'un attribut à partir d'une liste de champignons
    """
    res = []
    for mushroom in mushrooms:
        if mushroom.get_attribute(attribute) not in res:
            res.append(mushroom.get_attribute(attribute))
    return res
def get_subset_mushroom(mushrooms, label,attribute):
    """
    Fonction pour obtenir un sous-ensemble de champignons avec un certain label pour un attribut donné

    """
    temp = []
    for mushroom in mushrooms:
        if mushroom.get_attribute(attribute) == label:
            temp.append(mushroom)
    return temp
def get_gain(attribute,mushrooms,entropy):
    """
    Fonction pour calculer le gain d'information d'un attribut donné
    """
    add = 0
    labels = get_labels_attribute(attribute,mushrooms)
    for label in labels:
        subset = get_subset_mushroom(mushrooms, label,attribute)
        entropy_CAv = find_entropy(subset)
        pAv = len(subset)/ len(mushrooms)

        add += pAv * entropy_CAv

    return entropy - add, labels

def build_tree(mushrooms,attribute_name,best_gain = 0):
    """
    # Fonction pour construire l'arbre de décision récursivement
    """
    entropy = find_entropy(mushrooms)
    if entropy == 0:
        res = "No"
        if mushrooms[0].is_edible():
            res = "Yes"
        return Node(res,True)
    for attribute in attribute_name:
        gain, labels = get_gain(attribute, mushrooms, entropy )
        if gain > best_gain:
            best_labels = labels
            best_attribute = attribute
            best_gain = gain
    noeud = Node(best_attribute)
    for label in best_labels:
        subset = get_subset_mushroom(mushrooms,label,best_attribute)
        attribute_name.remove(best_attribute)
        noeud.add_edge(label,build_tree(subset,attribute_name))
        attribute_name.append(best_attribute)
    return noeud
def build_decision_tree(mushrooms: list[Mushroom]) -> Node:
    attribute_name = list(mushrooms[0].attributes.keys())
    return build_tree(mushrooms,attribute_name)


def find_entropy(mushrooms: list[Mushroom])->int:
    """
    Fonction pour calculer l'entropie d'un ensemble de champignons
    """
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
def display(noeud : Node, compteur):
    "Fonction pour afficher l'arbre de décision en profondeur avec un compteur pour l'indentation"
    attribute = noeud.criterion_
    if noeud.is_leaf():
        print("\t"*compteur,attribute)
    for edge in noeud.edges_:
        print("\t"*compteur, attribute," : ", edge.label_)
        display(edge.child_,compteur+1)
def is_edible(root : Node, mushroom : Mushroom) -> bool: #faire un test de is_edible qui va dans les branches de l'arbre ou qui teste avec des attributs qui sont pas dans l'arbre genre color
    """
    Fonction utilisant un parcours en profondeur pour déterminer la comestibilité d'un champignon en suivant l'arbre de décision
    """
    attribute = root.criterion_
    if root.is_leaf():
        res = True
        if attribute == "No":
            res = False
        return res
    for edge in root.edges_:
        if mushroom.get_attribute(attribute) == edge.label_:
            return is_edible(edge.child_,mushroom)
global stack
stack = []

def to_bool(noeud : Node,res)-> str:
    "Fonction qui transforme l'arbre en expressions boolèennes"
    attribute = noeud.criterion_
    for edge in noeud.edges_:
        stack.append(str(attribute) + " = "+ str(edge.label_))
        res = to_bool(edge.child_,res)
        stack.pop()

    if noeud.criterion_ == "Yes":
        for i in range(len(stack)):

                res +="(" +stack[i]
                if len(stack) >1 and i != len(stack ) -1:
                    res += ") and "
        if len(stack) > 1:
            res += ") or \n"
        else:
            res += ") or \n"
    return res


##################################################################################################################################
###Tests####
#Idée : tester un cas ou edible n'est pas le 1er attribut
#Idée : tester un cas ou le fichier csv envoyé n'est pas correct
#Idée : On peut coder facilement si on se base sur le fichier mushrooms or notre fonction devrait fonctionner sur tous les fichiers de champignons donc faire des tests sur des fichiers différents
#tester si l'arbre a bien un attribut edible
#tester si l'exemple du pdf fonctionne
#tester si la fonction display affiche correctement les arbres vides
#rapport : optimiser mes fonctions pour éviter de recalculer labels par exemple et expliquer dans mon rapport
arbre = build_decision_tree(load_dataset('mushrooms.csv'))
print(to_bool(arbre,""))
#display(arbre,0)

