__author__ = 'aulas'


class Departamento():
    """Departamento

    Departamento de la empresa, donde tendra asignado unos empleados
    """
    def __init__(self, nombre_dpto, id_dpto):
        """Constructor

        Constructor de la clase Departamento

        :param nombre_dpto: nombre del departamento
        :type nombre_dpto: str
        :param id_dpto: identificador del departamento
        :type id_dpto: int
        """
        self.nombre_dpto = nombre_dpto
        self.id_dpto = id_dpto
        self.lista_empleados = []

    def anadir_empleado(self, emp):
        """anadir empleado

        Asigna un empleado a este departamento

        :param emp: objeto de la clase Empleado
        :type emp: Empleado
        """
        self.lista_empleados.append(emp)

    def get_salario_total(self):
        """Salario total

        Devuelve la suma de salario de todos los empleados de este departamento

        :return: salario total de todos los empleados de este departamento
        :rtype: float
        """
        salario_total = 0
        for emp_actual in self.lista_empleados:
            salario_total += emp_actual.get_salario()
        return salario_total

    def get_nombre_dpto(self):
        """Nombre del departamento

        Devuelve el nombre del departamento

        :return: nombre del departamento
        :rtype: str
        """
        return self.nombre_dpto

    def get_salario_total_anual(self):
        """Salario total anual

        Devuelve la suma de salario anual de todos los empleados de este departamento

        :return: salario total anual de todos los empleados de este departamento
        :rtype: float
        """
        salario_total_anual = 0
        for emp_actual in self.lista_empleados:
            salario_total_anual += emp_actual.get_salario_anual()
        return salario_total_anual