""" -tc- Utilise une docstring pour documenter ton module.
        
Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
ou la PEP 257
        
"""

from position import Position

class Labyrinth:
    """ -tc- Utilise une docstring pour documenter ta classe.

    Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    ou la PEP 257

    """
    
# Init item
    def __init__(self):
        """ -tc- Utilise une docstring pour documenter ta méthode.

        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257

        """
        self.start = None
        self.end = None
        self.guardian = None
        self.hero = None
        self.width = None
        self.height = None
        # -tc- walls ferait plus de sens au pluriel, puisqu'il y en a plusieurs
        self.wall = []
        self.paths = []
        self.inventory = ["tube","needle","ether"] 
        # -tc- C'est plutôt macgyver ou le héro qui a un sac, non?
        self.bag = []

# load labyrinth file for reading the txt    
    def load_from_file(self,maze):
        """ -tc- Utilise une docstring pour documenter ta méthode.

        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257

        """
        # -tc- attention au mélange d'anglais et de français
        with open(maze, "r") as carte: 
            for y, line in enumerate(carte):
                for x, col in enumerate(line):
                    position = Position(x , y)
                    if col == "d":
                        self.paths.append(position)
                        self.start = (position)
                    elif col == "e":
                        self.end = position
                    elif col == "g":
                        self.paths.append(position)
                        self.guardian = position
                    elif col == "#":
                        self.wall.append(position)
                    elif col == ".":
                        self.paths.append(position)

            self.width = x + 1
            self.height = y + 1

   #Console mode, placer mon mode console ici ou ailleurs ?
   
    # -tc- Eviter les méthodes d'affichage dans mes classes de modèle. Utiliser des classes d'affichage séparées
    def show_console(self):
        """ -tc- Utilise une docstring pour documenter ta méthode.

        Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
        ou la PEP 257

        """
        
        for y in range(self.height):
            for x in range(self.width):
                position = Position(x, y)
                if position == self.start:
                    print("d")
                elif position in self.inventory:
                    print # je sais pas quoi mettre ici
                elif position == self.hero:
                    print("h")
                elif position == self.guardian:
                    print("g")
                elif position == self.end:
                    print("e")
                elif position in self.paths:
                    print(".")
                elif position in self.wall:
                    print("#")

def main():
    """ -tc- Utilise une docstring pour documenter ta fonction.

    Note: voir https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    ou la PEP 257

    """
    # -tc- lorsqu'un fonction est vide, utilise l'instruction pass
    pass


if __name__ == "__main__":
    main()
