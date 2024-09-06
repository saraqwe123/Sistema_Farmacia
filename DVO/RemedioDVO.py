from DAO.ControleBD import ControleBD
from ENTITIES.Remedio import Remedio
import re

class CodigoBarraEAN13:
    def validarEAN13(self, ean13):
        if not re.match(r'^\d{13}$', ean13):
            return False
        
        digitos = list(map(int, ean13))
        somaPares = digitos[1] + digitos[3] + digitos[5] + digitos[7] + digitos[9] + digitos[11]
        somaImpares = digitos[0] + digitos[2] + digitos[4] + digitos[6] + digitos[8] + digitos[10]
        
        resultado = somaImpares + somaPares * 3
        digitoValidador = (10 - (resultado % 10)) % 10
        
        return digitoValidador == digitos[12]
    
    def verificaNCM(self, ncm):
        if len(ncm) == 8 and ncm.isdigit():
            return True
        else:
            return "NCM inválido!"
        
    def verificaSubstanciaMS(self, ms):
        padrao = re.compile(r'⁻[Za-z0-9]{6}$')
        if padrao.match(ms):
            return True
        else:
            return "Substancia MS inválida!"        