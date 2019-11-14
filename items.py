""" -tc- Utilise une docstring pour documenter ton module.
        
Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
ou la PEP 257
        
"""

from position import Position
from random import choose
from labyrinthh import Labyrinth

# -tc- Je trouve plus utile une classe Item (au singulier qu'une classe Items) pour représenter chaque
# -tc- item indiviellement. Enfin, l'un n'empêche pas l'autre. Une classe Item + un classe Items (que
# -tc- je nommerais volontier ItemCollection ou Syringe, car on a vite fait de manquer le "s" et c'est
# -tc- très rare de nommer une classe au pluriel

""" -tc- Exemple de classe Item
class Item:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
"""

class Items:
    """ -tc- Utilise une docstring pour documenter ta classe.
        
    Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    ou la PEP 257
        
    """

    
    # -tc- Attention, c'est __init__, pas init
    def __init__(self, labyrinth):
        """ -tc- Utilise une docstring pour documenter ta méthode.
        
        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257
        
        """
        # Init instance labyrinthe
        self.labyrinth = labyrinth
        self.labyrinth.items = self.random()

    def random(self):
        """ -tc- Utilise une docstring pour documenter ta méthode.
        
        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257
        
        """
        # Check random position items

        
    # -tc- Pour que ta méthode ajoute un item, il faut qu'elle en reçoive un en argument. Il nous faut dont
    # -tc- un paramètre pour le réceptionner.
    def add_random_position(self):
        """ -tc- Utilise une docstring pour documenter ta méthode.
        
        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257
        
        """
        pass
