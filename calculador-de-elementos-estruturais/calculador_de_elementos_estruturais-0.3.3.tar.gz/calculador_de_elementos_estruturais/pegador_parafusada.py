from .input_normalizado import input_normalizado

class PegadorParafusada:
    
    @staticmethod
    def pega_medida(informacao_desejada):
        medida_aba = float(input_normalizado(informacao_desejada))
        return medida_aba / 10
    
    @staticmethod
    def pega_espessura(informacao_desejada):
        espessura = float(input_normalizado(informacao_desejada))
        return espessura / 10
    
    @staticmethod
    def pega_diametro_parafuso():
        diametro_parafuso = float(input_normalizado('Insira a espessura do parafuso em mm. '))
        return diametro_parafuso / 10
    
    @staticmethod
    def pega_quantidade_parafusos():
        qtd_parafusos = int(input_normalizado('Informe a quantidade de parafusos. '))
        return qtd_parafusos
    
    @staticmethod
    def pega_especificacao_chapa() -> str:
        mensagem = '''Informe a especificação da chapa. 

                (1) MR 250
                (2) AR 350
                (3) AR 350 COR
                (4) AR 415

                 '''

        numero_especificacao = input(mensagem)
        if numero_especificacao == '1':
            return 'MR 250'
        elif numero_especificacao == '2':
            return 'AR 350'
        elif numero_especificacao == '3':
            return 'AR 350 COR'
        elif numero_especificacao == '4':
            return 'AR 415'
        
        print('Digite um valor válido.')
        return PegadorParafusada.pega_especificacao_chapa()
        
    @staticmethod
    def pega_especificacao_parafuso() -> str:
        mensagem = '''Informe a especificação do parafuso. 

                (1) ASTM A307
                (2) ISO 898-1
                (3) ASTM A325
                (4) ISO 4016 Classe 8.8
                (5) ASTM A490
                (6) ISO 4016 Classe 10.9 

                 '''

        numero_especificacao = input(mensagem)
        if numero_especificacao == '1':
            return 'ASTM A307'
        elif numero_especificacao == '2':
            return 'ISO 898-1'
        elif numero_especificacao == '3':
            return 'ASTM A325'
        elif numero_especificacao == '4':
            return 'ISO 4016 8.8'
        elif numero_especificacao == '5':
            return 'ASTM A490'
        elif numero_especificacao == '6':
            return 'ISO 4016 10.9'
        
        print('Digite um valor válido.')
        return PegadorParafusada.pega_especificacao_parafuso()