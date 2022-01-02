import re


class TelefonesBr:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Telefone Invalido')

    def valida_telefone(self, telefone):
        padrao = '[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}'
        reposta = re.findall(padrao, telefone)
        if reposta:
            return True
        else:
            return False

    def mascara_telefone(self):
        return f''