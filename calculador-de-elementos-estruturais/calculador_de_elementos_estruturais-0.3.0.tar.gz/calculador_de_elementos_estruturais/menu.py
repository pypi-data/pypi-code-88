from .viga_de_madeira import VigaDeMadeira
from .pilar_de_madeira import PilarDeMadeira
from .enunciado_pv import Enunciado
from .ligacao_corte_duplo import LigacaoCorteDuplo
from .ligacao_parafusada import LigacaoParafusada

class MenuPrincipal:

    def __init__(self):
        mensagem = '''
        
    Bem vindo ao Calculador de Estruturas do 4º TE. A seguir, um pequeno tutorial de uso.
    
    
    Se tudo der certo, você só deve copiar e colar o enunciado. Mas caso não dê:
    
    Quando aparecer um seletor, por exemplo:
    
            (1) Opção 1
            (2) Opção 2
            (3) Opção 3

    Digite apenas o número que está dentro do parênteses. Por exemplo, se sua opção desejada for a 2,
    digite apenas "2" (sem as aspas).
    
    Não é necessário digitar as unidades dos valores. Caso elas sejam digitadas, erros ocorrerão.
    
    '''
    
        print(mensagem)

        while True:
            
            enunciado = Enunciado.pega_enunciado()
            
            if enunciado != ' ':
                if 'PILAR' in enunciado:
                    PilarDeMadeira(enunciado)
                elif 'VIGA' in enunciado:
                    VigaDeMadeira(enunciado)
                elif 'CORTE DUPLO' in enunciado:
                    LigacaoCorteDuplo(enunciado)
                elif 'NOMINAL' in enunciado:
                    LigacaoParafusada()
                else:
                    raise ValueError('Digite um valor válido.')
            else:
                mensagem = '''Qual elemento estrutural irá ser calculado?
        
                (1) Pilar
                (2) Viga
                (3) Ligação Corte Duplo
                (4) Ligação Parafusada
            
                 '''
                elemento = int(input(mensagem))

                if elemento == 1:
                    PilarDeMadeira(None)
                elif elemento == 2:
                    VigaDeMadeira(None)
                elif elemento == 3:
                    LigacaoCorteDuplo(None)
                elif elemento == 4:
                    LigacaoParafusada()
                else:
                    raise ValueError('Digite um valor válido.')
