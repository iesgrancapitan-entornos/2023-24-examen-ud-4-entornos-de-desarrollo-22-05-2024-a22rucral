"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""


class Gato:

    def __init__(self):
        """
        Inicializa un bojeto en la clase gato
        """
        self.maulla = 'Miau'

    def maullar(self):
        """
        Clase que lanza un print para maullar
        """
        print(self.maulla)


g = Gato()
g.maullar()
