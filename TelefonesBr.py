import re


class TelefonesBr:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Telefone Invalido')

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        reposta = re.findall(padrao, telefone)
        if reposta:
            return True
        else:
            return False

    def format_numero(self):
        # +00(00)00000-0000
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        if resposta.group(1):
            numero_formatado = f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
            return numero_formatado
        else:
            numero_formatado = f'({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
            return numero_formatado
