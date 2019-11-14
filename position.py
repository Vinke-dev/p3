class Position:
    # Init x = horizontal, y = vertical
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Deplacement    
    def up(self):
        return Position(self.y + 1, self.x)

    def down(self):
        return Position(self.y - 1, self.x)
    
    def left(self):
        return Position(self.x - 1, self.y)

    def right(self):
        return Position(self.x + 1, self.y)

    # -tc- Utile également d'ajouter une méthode __eq__(self, other) pour
    # -tc- comparer deux positions entre elles et __hash__(self) pour 
    # -tc- pouvoir utiliser une instance de position en clé de dictionnaire
    # -tc- ou dans un ensemble
