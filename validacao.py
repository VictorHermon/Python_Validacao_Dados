from validate_docbr import CPF


class ValidaCpf:
    
    def __init__(self, documento):
        self.analisa_cpf(documento)

    def analisa_cpf(self, documento):
        documento = str(documento)
        if len(documento) == 11:
            valida_cpf = CPF()
            if valida_cpf.validate(documento):
                self.cpf = valida_cpf.mask(documento)
            else:
                print('CPF inserido não é valido')
        else:
            print('Número de digitos incorreto')
            