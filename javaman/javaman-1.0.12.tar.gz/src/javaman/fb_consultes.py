sync_productes = """
select 
    p.EMPRESA_ID, p.ID, p.ARTICLE, p.CODI_ARTICLE, pa.ID ATRIBUT_ID, 
    p.DATA_BAIXA, pm.PES PES_NET, pm.PES + pm.TARA PES_BRUT, pm.AMPLADA, pm.LLARGADA,
    pm.ALTURA, pe.EAN13_ARTICLE, 1, pe.EAN13_CAIXA, pp.UNITATS_SUP, pl.CONTROL_LOTS_VENDA
from ARTICLES p
join ARTICLES_ATRIBUTS pa on p.ID = pa.ARTICLE_ID
join ARTICLES_MIDES pm on p.ID = pm.ARTICLE_ID
join ARTICLES_EANS pe on pa.ID = pe.ARTICLE_ATRIBUT_ID
join ARTICLES_PARAMETRES pp on p.ID = pp.ARTICLE_ID
left join SELECT_ARTICLES_C_ESTOCS(p.ID, CURRENT_DATE) pl on p.ID = pl.ARTICLE_ID
join (select ARTICLE_ATRIBUT_ID, SUM(QUANTITAT_TOTAL) STOCK 
       FROM  ARTICLES_ESTOCS 
       GROUP BY ARTICLE_ATRIBUT_ID 
       HAVING SUM(QUANTITAT_TOTAL) > 0
) ps on pa.ID = ps.ARTICLE_ATRIBUT_ID
where p.ID not in (1268, 2127) and pl.CONTROL_ESTOCS = 'S';
"""

sync_clients = """
select c.EMPRESA_ID, t.ID, c.ID, t.NOM_LLARG_I_COMERCIAL, c.DATA_BAIXA, LEFT(tp.IDIOMA_CODI,2)
from clients c
join tercers t on c.TERCER_ID = t.ID
join tercers_parametres tp on t.id = tp.tercer_id
"""

sync_transportistes = """
select r.EMPRESA_ID, r.ID, t.NOM_LLARG
FROM REPARTIDORS r
join TERCERS t on r.TERCER_ID = t.ID
"""

sync_comanda = """
select
    c.EMPRESA_ID, 
    c.ID COMANDA_ID,
    c.NUMERO_COMANDA,
    cd.TERCER_ID CLIENT_ID,
    cd.REPARTIDOR_ID,
    CASE WHEN c_cli.COMANDA_ID IS NULL THEN cd_ter.NOM_LLARG_I_COMERCIAL ELSE c_cli.TERCER END NOM_CLIENT,
    CASE WHEN c_cli.COMANDA_ID IS NULL THEN cd_carrer.CARRER ELSE c_cli.ADRECA END ADRECA,
    CASE WHEN c_cli.COMANDA_ID IS NULL THEN cd_adr.CPOSTAL ELSE c_cli.CPOSTAL END CPOSTAL,
    CASE WHEN c_cli.COMANDA_ID IS NULL THEN cd_poble.POBLE ELSE c_cli_poble.POBLE END POBLE,
    CASE WHEN c_cli.COMANDA_ID IS NULL THEN cd_comu.PAIS_CODI ELSE c_cli_comu.PAIS_CODI END CODI_PAIS,
    CASE WHEN c_cli.COMANDA_ID IS NULL THEN NULL ELSE c_cli.TELEFON END TELEFON,
    CASE WHEN c_cli.COMANDA_ID IS NULL THEN NULL ELSE c_cli.EMAIL END MAIL,
    cd.PES_NET, cd.PES_BRUT
    
from comandes c
join comandes_distribucio cd on c.ID = cd.COMANDA_ID
join adreces_distribucio cd_adr on cd.ADRECA_DISTRIBUCIO_ID = cd_adr.ID
join carrers cd_carrer on cd_adr.CARRER_ID = cd_carrer.ID
join pobles cd_poble on cd_adr.POBLE_ID = cd_poble.ID
join comarques cd_coma on cd_poble.COMARCA_ID = cd_coma.ID
join provincies cd_prov on cd_coma.PROVINCIA_ID = cd_prov.ID
join comunitats cd_comu on cd_prov.COMUNITAT_ID = cd_comu.ID

join tercers cd_ter on cd.TERCER_ID = cd_ter.ID
join clients cd_cli on cd_ter.ID = cd_cli.TERCER_ID and c.EMPRESA_ID = cd_cli.EMPRESA_ID    
left join comandes_client c_cli on c.ID = c_cli.COMANDA_ID
left join pobles c_cli_poble on c_cli.POBLE_ID = c_cli_poble.ID
left join comarques c_cli_coma on c_cli_poble.COMARCA_ID = c_cli_coma.ID
left join provincies c_cli_prov on c_cli_coma.PROVINCIA_ID = c_cli_prov.ID
left join comunitats c_cli_comu on c_cli_prov.COMUNITAT_ID = c_cli_comu.ID
where c.ID = ?
"""

sync_comanda_linies = """
select cl_atr.ID ATRIBUT_ID, sum(cl.QUANTITAT) QUANTITAT, min(cl.NUMERO_LINIA) nl, min(cl.DESCRIPCIO), 
sum(cl.QUANTITAT) QUANTITAT_PENDENT
from comandes c
join comandes_linies cl on c.ID = cl.COMANDA_ID
join articles_atributs cl_atr on cl.ARTICLE_ATRIBUT_ID = cl_atr.ID
join articles cl_art on cl_atr.ARTICLE_ID = cl_art.ID
LEFT join select_articles_c_estocs(cl_art.ID, c.DATA_COMANDA) cl_art_stk on cl_art.ID =  cl_art_stk.ARTICLE_ID
where cl_art_stk.CONTROL_ESTOCS = 'S' and c.ID = ?
group by ATRIBUT_ID
HAVING sum(cl.QUANTITAT) > 0
"""

sync_comandes_pendents = """
SELECT C.ID, C.NUMERO_COMANDA, C.DATA_COMANDA, T.NOM_LLARG_I_COMERCIAL
FROM COMANDES C
JOIN CLIENTS CL ON C.CLIENT_ID = CL.ID
JOIN TERCERS T ON CL.TERCER_ID = T.ID
left join SELECT_COMANDES_ESTATS_MAG(C.ID) CE ON C.ID = CE.COMANDA_ID
where C.DATA_INICI IS NULL AND CE.MAG_PENDENT_SERVIR = 'S' AND C.DATA_ANULACIO IS NULL;
"""
