"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Persona:
    def __init__(self, nombre, dni, apellidos):
        """
        Inicializa un objeto en la clase persona
        :param nombre:
        :param dni:
        :param apellidos:
        """
        self.__nif = dni
        self.__nombre = nombre
        self.__apellidos = apellidos


class Estudiante(Persona):
    curso = "Primaria"

    def __init__(self, nif, curso, nombre, apellidos, dni):
        """
        Inicializa el objeto en la clase estudiante
        :param nif:
        :param curso:
        :param nombre:
        :param apellidos:
        :param dni:
        """
        super().__init__(nombre, dni, apellidos)
        self.nif = nif
        self.curso = curso
        self.nombre = nombre
        self.apellidos = apellidos

    @property
    def nif(self):
        """

        :rtype: object
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        self.__nif = value

    @property
    def curso(self):
        """

        :return: el curso en el que se encuentra
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        self.__curso = value

    @property
    def nombre(self):
        """

        :return: el nombre del estudiante
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        self.__nombre = value

    @property
    def apellidos(self):
        """

        :return: apellidos del estudiante
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        self.__apellidos = value
