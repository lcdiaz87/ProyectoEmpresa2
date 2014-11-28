__author__ = 'Luis Carlos'


class Empresa():
    """Empresa

    Empresa de este proyecto
    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """Constructor

        Constructor de la clase empresa

        :param nombre_empresa: nombre de la empresa
        :type nombre_empresa: str
        :param cif: C.I.F. de la empresa
        :type cif: str
        :param razon_social: razon social de la empresa
        :type razon_social: str
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.lista_departamentos = []

    def anadir_departamento(self, dept):
        """Anadir departamento

        Anade un departamento a la empresa
        :param dept: objeto de la clase Departamento
        :type dept: Departamento
        """
        self.lista_departamentos.append(dept)

