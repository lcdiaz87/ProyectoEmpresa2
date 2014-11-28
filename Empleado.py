__author__ = 'aulas'


class Empleado():
    """Empleado

    Empleado que puede ser asignado a un departamento de la empresa
    """
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """Constructor

        Constructor de la clase empleado

        :param nombre: nombre del empleado
        :type nombre: str
        :param apellidos: apellidos del empleado
        :type apellidos: str
        :param dni: D.N.I. del empleado
        :type dni: str
        :param direccion: direccion del empleado
        :type direccion: str
        :param edad: edad del empleado
        :type edad: int
        :param email: email del empleado
        :type email: str
        :param salario: salario del empleado
        :type salario: float
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """salario

        devolver salario del empleado

        :return: salario del empleado
        :rtype: float
        """
        return self.salario

    def get_dni(self):
        """D.N.I.

        devolver DNI del empleado

        :return: DNI del empleado
        :rtype: str
        """
        return self.dni

    def get_nombre_apellido(self):
        """apellidos

        devolver apellidos del empleado

        :return: apellidos del empleado
        :rtype: str
        """
        return self.nombre % " " % self.apellidos

    def get_edad(self):
        """edad

        devolver edad del empleado

        :return: edad del empleado
        :rtype: int
        """
        return self.edad

    def get_email(self):
        """email

        devolver email del empleado

        :return: email del empleado
        :rtype: str
        """
        return self.email

    def get_direccion(self):
        """direccion

        devolver direccion del empleado

        :return: direccion del empleado
        :rtype: str
        """
        return self.direccion

    def get_salario_anual(self):
        """salario anual

        devolver salario anual del empleado

        :return: salario anual del empleado
        :rtype: float
        """
        return self.salario * 12
