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
    