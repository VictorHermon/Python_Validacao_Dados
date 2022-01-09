import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido')

    def __str__(self):
        return self.format_cep()

    @staticmethod
    def cep_e_valido(cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def retorna_enederco(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json'
        response = requests.get(url)
        bairro_localidade_uf = response.json()
        # utilizar dir(objeto) para verificar todos os atributos e metodos
        return (
            bairro_localidade_uf['bairro'],
            bairro_localidade_uf['localidade'],
            bairro_localidade_uf['uf']
        )
