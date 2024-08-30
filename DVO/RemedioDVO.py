from DAO.ControleBD import ControleBD
from ENTITIES.Remedio import Remedio
import re

class CodigoBarraEAN13:
    def validar(self):
        remedio = Remedio()
        if not re.match(r'^\d{13}$', remedio.ean13):
            return False
        
        digitos = list(map(int, remedio.ean13))
        somaPares = digitos[1] + digitos[3] + digitos[5] + digitos[7] + digitos[9] + digitos[11]
        somaImpares = digitos[0] + digitos[2] + digitos[4] + digitos[6] + digitos[8] + digitos[10]
        
        resultado = somaImpares + somaPares * 3
        digitoValidador = (10 - (resultado % 10)) % 10
        
        return digitoValidador == digitos[12]
    
