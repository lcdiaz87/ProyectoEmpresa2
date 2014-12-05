from unittest import TestCase

from mockito import *

from src.Empleado import *
from src.Departamento import *


__author__ = 'aulas'


class TestDepartamento(TestCase):
    """Test del ProyectoEmpresa

    Clase para testear el proyecto, donde podemos ver dos testeos que se definiran a continuacion
    """
    def test_get_salario_total(self):
        """Test Salario Total

        Realiza una comprobacion para comprobar si el metodo get_salario_total funciona bien, con la ayuda del mock
        """
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        emp4 = mock(Empleado)
        emp5 = mock(Empleado)
        when(emp1).get_salario().thenReturn(100)
        when(emp2).get_salario().thenReturn(200)
        when(emp3).get_salario().thenReturn(300)
        when(emp4).get_salario().thenReturn(400)
        when(emp5).get_salario().thenReturn(500)
        dept = Departamento("departamento1", 1)
        dept.anadir_empleado(emp1)
        dept.anadir_empleado(emp2)
        dept.anadir_empleado(emp3)
        dept.anadir_empleado(emp4)
        dept.anadir_empleado(emp5)
        res = dept.get_salario_total()
        self.assertEqual(res, 1500)

