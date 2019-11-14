""" -tc- Utilise une docstring pour documenter ton module.
        
Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
ou la PEP 257
        
"""

from position import Position
from items import Items
from labyrinth import Labyrinth



class Hero:
    """ -tc- Utilise une docstring pour documenter ton module.
        
    Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    ou la PEP 257
        
    """
    
    def __init__(self,labyrinth): 
        """ -tc- Utilise une docstring pour documenter ta classe.

        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257

        """
        # -tc- Pourquoi instancer Position alors que le héro ne sait pas 
        # -tc- sur quelle position il doit se positionner. Autant recevoir 
        # -tc- cette position en paramètre puis self.position = position
        self.position = Position()  # lien vers l'instance de position correspondante
        # -tc- Tu reçois le labyrinthe en argument via le paramètre labyrinthe. 
        # -tc- Plutôt self.labyrinth = labyrinth que réinstancier. On ne veux pas deux labyrinthes
        self.labyrinth = Labyrinth()  # lien vers l'instance du labyrinth
        self.items = Items()

    def move(self, direction):
        """ -tc- Utilise une docstring pour documenter ta méthode.

        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257

        """
        # nouvelle_position <- demander à l'objet self.position de renvoyer la position dans direction
        new_position = self.position.get_new_position_from_direction(direction)
        # SI nouvelle_position est dans les chemins du labyrinthe:
        if new_position in self.labyrinth.paths:
            # Déplacer le héro
            self.position = new_position
        # SI self.position est dans la liste d'items de labyrinthe:
        if self.labyrinth.has_item_on_position(self.position):
           
    # ramasser l'objet
    def catch_item(self):
        """ -tc- Utilise une docstring pour documenter ta méthode.

        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257

        """
        # item - Demander à self.labyrinthe de me renvoyer l'objet situé à self.position
        item = self.labyrinth.get_item_located_at(self.position)
        # AJouter objet dans la liste self.bag (self.bag.append(item))
        self.bag.append(item)

    def fight_guardian(self):
        """ -tc- Utilise une docstring pour documenter ta méthode.

        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257

        """
        if self.position == self.labyrinth.end:
            # -tc- Pourquoi 3 et qu'est-ce que ce 3 signifie? Plutot utiliser une constante comme NUMBER_OF_ITEMS
            if self.bag == 3:
                # -tc- Des constantes comme Game.VICTORY, Game.GAME_OVER et Game.CONTINUE seraient plus parlantes 
                # -tc- (à définir éventuellement dans une classe Game)
                return 1
            else:
                return 0
