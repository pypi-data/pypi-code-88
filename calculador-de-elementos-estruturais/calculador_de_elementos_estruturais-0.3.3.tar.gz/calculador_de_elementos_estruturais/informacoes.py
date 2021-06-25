from pandas import DataFrame

informacoes_classe = {'Classe': ('C20', 'C30', 'C40', 'C60'),
                      'Fc0k': (20, 30, 40, 60),
                      'Ec0m': (9500, 14500, 19500, 24500)}
tabela_classe = DataFrame(informacoes_classe, index=(1, 2, 3, 4))

informacoes_kmod1 = {'Permanente': 0.6,
                     'Longa Duração': 0.7,
                     'Média Duração': 0.8,
                     'Curta Duração': 0.9,
                     'Instantânea': 1.1}

duracoes = ('Permanente', 'Longa Duração', 'Média Duração', 'Curta Duração', 'Instantânea')

informacoes_kmod2 = {'1': 1,
                     '2': 1,
                     '3': 0.8,
                     '4': 0.8}

informacoes_kmod3 = {'1ª Categoria': 1, '2ª Categoria': 0.8}

categorias = ('1ª Categoria', '2ª Categoria')

dict_resistencia_dos_parafusos = {'fy': (250,235,635,560,640,895,900),
                             'fu': (415,400,825,725,800,1035,100),}

resistencia_dos_parafusos = DataFrame(dict_resistencia_dos_parafusos, 
                                      index=('ASTM A307', 'ISO 898-1',
                                             'ASTM A325 <= 24', 'ASTM A325 > 24',
                                             'ISO 4016 8.8', 'ASTM A490',
                                             'ISO 4016 10.9'))

def request_resistencia_parafuso(especificacao: str, diametro: float) -> tuple:
    df = resistencia_dos_parafusos
    
    if especificacao == 'ASTM A325':
        if diametro > 24:
            fu = df.loc['ASTM A325 > 24'].fu
            fy = df.loc['ASTM A325 > 24'].fy
        else:
            fu = df.loc['ASTM A325 <= 24'].fu
            fy = df.loc['ASTM A325 <= 24'].fy
    else:
        fu = df.loc[especificacao].fu
        fy = df.loc[especificacao].fy
        
    return fy, fu

dict_resistencia_chapas = {'fy': (250,350,350,415),
                           'fu': (400,50,485,520)}

resistencia_chapas = DataFrame(dict_resistencia_chapas, 
                               index=('MR 250', 'AR 350', 
                                      'AR 350 COR', 'AR 415'))

def request_resistencia_chapas(especificacao: str) -> tuple:
    fu = resistencia_chapas.loc[especificacao].fu
    fy = resistencia_chapas.loc[especificacao].fy
    
    return fy, fu