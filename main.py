from acesso_cep import BuscaEndereco

cep = '06813170'

objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.retorna_enederco()

print(f'Bairro: {bairro} \nCidade: {cidade}, \nUF: {uf}')
