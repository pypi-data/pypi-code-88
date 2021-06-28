# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from urllib.request import urlopen

from sklearn.model_selection import train_test_split


#import core_helper.helper_general as hg
import src.Prj_Core.core_helper.helper_general as hg
hg.set_base_path()


#import core_helper.helper_acces_db as hadb
import src.Prj_Core.core_helper.helper_acces_db as hadb

import src.Prj_Core.core_helper.helper_feature_selection as hfs

#import core_helper.helper_transformers as ht
import src.Prj_Core.core_helper.helper_transformers as ht

import src.Prj_Core.core_helper.helper_clean as hc
import src.Prj_Core.core_helper.helper_classification_model as hcm

import src.Prj_Core.core_helper.helper_dataframe as hd
import src.Prj_Core.core_helper.helper_siagie_kpi as hsk
import src.Prj_Core.core_helper.helper_terceros_kpi as htk

from sklearn.metrics import classification_report,average_precision_score
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats 
from sklearn.preprocessing import RobustScaler

#################################### 1.FUSION ######################################






def get_df_procesado(anio,col_name_y,key_grupo_grados, grupo_grados,macro_region, 
                     feature_selection=False,df_id_persona=None,anio_serv=None):
    
    
    dtypes_columns = {'COD_MOD': str,
                      'ANEXO':int,                    
                      'COD_MOD_T_MENOS_1':str,
                      'ANEXO_T_MENOS_1':int,                      
                      'UBIGEO_NACIMIENTO_RENIEC':str,
                      'N_DOC':str,
                      'ID_GRADO':int,
                      'ID_PERSONA':int,#nurvo
                      'CODIGO_ESTUDIANTE':str,
                      'NUMERO_DOCUMENTO':str,
                      'NUMERO_DOCUMENTO_APOD':str,
                      'CODOOII':str
                      }   


    
    df_servicios = hadb.get_df_servicios(macro_region=macro_region,anio=anio_serv)    

    list_pd = []
    #5,6,7,8
    for ID_GRADO in grupo_grados:
        url = hg.get_base_path()+"\\src\\Prj_Interrupcion_Estudios\\Prj_Desercion\\_02_Preparacion_Datos\\_02_Estructura_Base\\_data_\\nominal\\estructura_base_EBR_{}_{}_delta_1.csv"
        url = url.format(ID_GRADO,anio)
        df =pd.read_csv(url, dtype=dtypes_columns ,encoding="utf-8")
        df['STR_ID_GRADO'] = "GRADO_" + str(ID_GRADO)      
        df = pd.merge(df,df_servicios, left_on=["COD_MOD","ANEXO"], right_on = ["COD_MOD","ANEXO"] ,how="inner")
        if df_id_persona is not None:
            df = pd.merge(df,df_id_persona[["ID_PERSONA"]], left_on="ID_PERSONA", right_on = "ID_PERSONA",how="inner")        
        list_pd.append(df)
        
    df_reg = pd.concat(list_pd)
    print("df_reg.shape", df_reg.shape)
    anio_notas = anio-1   
    
    
    cls_json = {}
    cls_json['SITUACION_FINAL']=["APROBADO","DESAPROBADO"]
    cls_json['SF_RECUPERACION']=["APROBADO","DESAPROBADO"]
    cls_json['SITUACION_MATRICULA']=["PROMOVIDO","REPITE","INGRESANTE","REENTRANTE"]
    cls_json['JUNTOS']="dummy"
    
    #df_reg = hsk.generar_kpis_historicos(df_reg,anio_df=anio,anio_h=anio-2,cls_json=cls_json,t_anios=4)      
    df_reg = hsk.agregar_notas(df_reg,anio,anio_notas, cls_group=["ZSCORE"],notas_group="CM")    
    '''
    df_reg = htk.agregar_sisfoh(df_reg)       
    df_reg = hsk.generar_kpis_desercion(df_reg,anio_df=anio, anio_h=anio-2 ,t_anios=4)  
      
    df_reg =  htk.agregar_shock_economico(df_reg,anio=anio)  
    
    df_reg = hsk.generar_kpis_traslado(df_reg,anio_df=anio,anio_h=anio-1,t_anios=5)
    df_reg = hsk.generar_kpis_traslado_a_publico(df_reg,anio_df=anio,anio_h=anio-1,t_anios=5)
   
    if key_grupo_grados=="6 prim":
        df_reg = hsk.agregar_distancia_prim_sec(df_reg)
        df_reg = hc.fill_nan_with_nan_category_in_cls(df_reg , ["GRUPO_DISTANCIA"])
    
    '''
    
    df_reg = hc.fill_nan_with_nan_category_in_cls(df_reg , ["SITUACION_MATRICULA_T_MENOS_1",
                                                            "SF_RECUPERACION_T_MENOS_1",
                                                            "PARENTESCO","DSC_DISCAPACIDAD",
                                                            "SEXO_APOD", "SITUACION_FINAL_T_MENOS_1",                                                        
                                                            "SITUACION_MATRICULA_T",
                                                            "TIENE_CERTIFICADO_DISCAPACIDAD",
                                                            "PADRE_VIVE","MADRE_VIVE"])
    
    df_reg = hc.trim_category_cls(df_reg)
    
    df_reg = hsk.formatear_columnas_siaguie(df_reg)
    
   
    
    #df_reg['EDAD_EN_DIAS_T']  = df_reg['EDAD_EN_DIAS_T'].round()
   
   
    columns_too_much_nan_and_categories = ["JUSTIFICACION_RETIRO_T_MENOS_1","DSC_PAIS","DSC_LENGUA"]
    columns_to_drop  = ['ID_PERSONA','COD_MOD','ANEXO','COD_MOD_T_MENOS_1','ANEXO_T_MENOS_1','ID_GRADO_T_MENOS_1',
                        'NUMERO_DOCUMENTO_APOD','N_DOC','NIVEL_INSTRUCCION_APOD'] 
    #cat_muy_largas = ['D_REGION']
    
    columns_to_drop_all = columns_too_much_nan_and_categories+columns_to_drop 
    
    ID_P_T = df_reg['ID_PERSONA']
    
    if col_name_y is not None:
        y = df_reg[col_name_y]
        columns_to_drop_all.append(col_name_y)
    else:    
        y = None
        
        
    X = df_reg.drop(columns = columns_to_drop_all) 

    ct = ht.CatTransformer(pp = "lb",console=True) #lb le
    ct.fit(X)
    X_t = ct.transform(X)
    #print(X_t.columns)
    if feature_selection:
        print("Iniciando proceso de eliminancion de columnas irrelevantes")
        X_t = hfs.drop_cls_unique_value(X_t)
        X_t = hfs.drop_corr_columns(X_t)
        X_t = hfs.drop_nan_columns(X_t)
    
    return ID_P_T, X_t , y

########################################################################################

#ID_P_T, X_t , y = get_df_procesado_temp(2019,'DESERCION_2019_2020',"6 prim",[9],"oriente",True,None,2019)
ID_P_T, X_t , y = get_df_procesado(2019,'DESERCION_2019_2020',"6 prim",[9],"oriente",True,None,2019)
test_size = hcm.get_test_size(X_t)
X_train, X_test, y_train, y_test= train_test_split(X_t, y, test_size=test_size,stratify=y,random_state=42)
model_name = "neg_bagging_fraction__lgb_model"
model , predicted_probas  , KPIs = hcm.modelar_clasificacion_binaria(model_name, X_train,y_train,X_test,y_test)

#########################################################################################
'''
ID_P_T, X_t , y = get_df_procesado(2019,'DESERCION_2019_2020',"6 prim",[9],"oriente",True,None,2019)
X_t['randNumCol'] = np.random.normal(3, 2.5, X_t.shape[0])
print(hd.get_bool_columns(X_t))
inputs_num = list(set(X_t.columns.tolist())-set(hd.get_bool_columns(X_t)))


data_ca = {'Variable' : inputs_num,
       'Coeficiente_Asim' : stats.skew(X_t[inputs_num])}
asim = pd.DataFrame(data_ca)


inputs_num_sel = np.array(asim.iloc[:,0][asim['Coeficiente_Asim']<=5])
inputs_num_sel

res_data_num = X_t[inputs_num].describe().transpose()
res_data_num['cv'] = res_data_num.iloc[:,2] / res_data_num.iloc[:,1] * 100
res_data_num

from sklearn.preprocessing import RobustScaler
transformer = RobustScaler().fit(X_t)
data_inputs_s = transformer.transform(X_t)
X_t = pd.DataFrame(data_inputs_s,columns=X_t.columns.tolist())

sns.kdeplot(X_t['randNumCol'],shade = True,vertical = False,cumulative = False,color = "#BB0000")
plt.show()

test_size = hcm.get_test_size(X_t)
X_train, X_test, y_train, y_test= train_test_split(X_t, y, test_size=test_size,stratify=y,random_state=42)
       

model_name = "neg_bagging_fraction__lgb_model"
model , predicted_probas  , KPIs = hcm.modelar_clasificacion_binaria(model_name, X_train,y_train,X_test,y_test)


specific_url_model = "temp/model.sav"
model = pickle.load( open( specific_url_model, "rb" ) )

y_pred2 ,y_prob2_cb,  predicted_probas2 = hcm.predecir_clasificacion_binaria(model,X_test)

'''
#################################### 2.MODELAMIENTO ######################################




y_test2_total = []
y_pred2_total = []

grupos_grados = { "1 prim": [4],"2 prim": [5],"3-5 prim": [6,7,8], "6 prim": [9], "1-4 sec": [10,11,12,13],"5 sec": [14]}
#grupos_grados = {  "6 prim": [9]}

lista_mr = ["centro","norte","sur","oriente","lima"]
PATH_RESULT = "resultado"

for key, grupo_grado  in grupos_grados.items():
    KPIs_list = []
    
    for macro_region in lista_mr:
        print("--------------------- ",macro_region,"-----------------")
        path = "{}/{}/{}".format(PATH_RESULT,key,macro_region)
        hg.validar_directorio(path) 
                
        ID_P_T, X_t , y = get_df_procesado(2019,'DESERCION_2019_2020',key,grupo_grado,macro_region,True)
                
        test_size = hcm.get_test_size(X_t)
        
        X_train, X_test, y_train, y_test= train_test_split(X_t, y, test_size=test_size,stratify=y,random_state=42)
        t_train = X_train.shape[0]
        t_test =  X_test.shape[0]
        
        ID_P_T2, X_test2 , y_test2 = get_df_procesado(2021,None,key,grupo_grado,macro_region,False,None,2021)
        
        X_test2 = hd.igualar_columnas(X_t,X_test2)
        
        y_test2_total.append(y_test2)    
        
        y_prob2_nbf = y_prob2_spw = y_prob2_cb = 0
             
        print("inicio ", "neg_bagging_fraction__lgb_model")
        model_name = "neg_bagging_fraction__lgb_model"
        path_directory_model = path +"/"+model_name 
        model , predicted_probas  , KPIs = hcm.modelar_clasificacion_binaria(model_name, X_train,y_train,X_test,y_test,path_directory_model)
        KPIs_list.append([macro_region,model_name,t_train,t_test,KPIs])
        y_pred2 ,y_prob2_nbf,  predicted_probas2 = hcm.predecir_clasificacion_binaria(model,X_test2)
        print("fin ", "neg_bagging_fraction__lgb_model")
        
        
        print("inicio ", "scale_pos_weight__lgb_model")
        model_name = "scale_pos_weight__lgb_model"
        path_directory_model = path +"/"+model_name 
        model , predicted_probas  , KPIs = hcm.modelar_clasificacion_binaria(model_name, X_train,y_train,X_test,y_test,path_directory_model)
        KPIs_list.append([macro_region,model_name,t_train,t_test,KPIs])
        y_pred2 ,y_prob2_spw,  predicted_probas2 = hcm.predecir_clasificacion_binaria(model,X_test2)
        print("fin ", "scale_pos_weight__lgb_model")
        '''  
        model_name = "custom_bagging__lgb_model"
        path_directory_model = path +"/"+model_name 
        model , predicted_probas  , KPIs = hcm.modelar_clasificacion_binaria(model_name, X_train,y_train,X_test,y_test,path_directory_model)
        KPIs_list.append([macro_region,model_name,t_train,t_test,KPIs])
        y_pred2 ,y_prob2_cb,  predicted_probas2 = hcm.predecir_clasificacion_binaria(model,X_test2)
        '''    
        
        X_test2["neg_bagging_fraction__lgb_model"] = y_prob2_nbf
        X_test2["scale_pos_weight__lgb_model"] =  y_prob2_spw
        X_test2["custom_bagging__lgb_model"] =  y_prob2_cb
        
        X_t['DESERCION'] = y    
        X_t['ID_PERSONA'] = ID_P_T
        
        #X_test2['DESERCION'] = y_test2    
        X_test2['ID_PERSONA'] = ID_P_T2
        print("inicio guardando csvs ")
        X_t.to_csv(path+"/X_t.csv",index =False , encoding="utf-8")
        X_test2.to_csv(path+"/X_t_mas_1.csv",index =False , encoding="utf-8")
        print("fin  guardando csvs ")
        y_pred2_total.append(y_pred2)

    path = "{}/{}".format(PATH_RESULT,key)
    hg.validar_directorio(path)    

    df_result = hcm.get_result_df(KPIs_list)
    df_result.to_excel(path+"/resultados.xlsx")  
    
#################################### 3.RESULTADO FINAL ######################################




url =   "resultado/nacional_15042021.dta"        
nacional_15042021 = pd.read_stata(url)   
df_siagie_2021= hadb.get_siagie_por_anio(2021,id_nivel_list=["B0","F0"])
print(df_siagie_2021[df_siagie_2021.COD_MOD=="0327879"].shape)

df_delta = pd.merge(df_siagie_2021,nacional_15042021,left_on="ID_PERSONA",right_on="ID_PERSONA",how="left")
df_delta = df_delta[df_delta.RISK_SCORE.isna()==True].copy()

df_delta.drop_duplicates(subset=['ID_PERSONA'], keep='last',inplace=True)

print(df_delta[df_delta.COD_MOD=="0320879"].shape)

print(df_delta.shape)


#grupos_grados = {"1 prim": [4]}
#lista_mr = ["centro"]
grupos_grados = {"1 prim": [4],"2 prim": [5], "3-5 prim": [6,7,8], "6 prim": [9], "1-4 sec": [10,11,12,13],"5 sec": [14]}
lista_mr = ["centro","norte","sur","oriente","lima"]
list_result = []
PATH_RESULT = "resultado"
SUB_FOLDER_DELTA = "delta_15042021"

df_resumen = hcm.get_kpi_df_nacional(PATH_RESULT,grupos_grados,lista_mr)

for key, grupo_grado  in grupos_grados.items():
    
    for macro_region in lista_mr:
        
        specific_url = '{}/{}/{}/{}'.format(PATH_RESULT,key,macro_region,"X_t.csv")            
        X_t=pd.read_csv(specific_url, encoding="utf-8",nrows=0)         
        del X_t['DESERCION'] 
        del X_t['ID_PERSONA']
        
        print(11111111111111111111111111111111111111)
        ID_P_T2, X_test2 , y_test2 = get_df_procesado(2021,None,key,grupo_grado,macro_region,False,df_delta,2021)
        print(X_test2.shape)
        print(22222222222222222222222222)
        X_test2 = hd.igualar_columnas(X_t,X_test2)
        best_model = df_resumen[(df_resumen.key_grupo_grado==key) & (df_resumen['Macro Región']==macro_region)].Modelo.iloc[0]
        specific_url_model = '{}/{}/{}/{}/{}'.format(PATH_RESULT,key,macro_region,best_model,"model.sav")
        
                
        print("best_model : ",best_model)
        print("specific_url_model > ",specific_url_model)
        model = pickle.load( open( specific_url_model, "rb" ) )
        
        y_pred2 ,y_prob2_cb,  predicted_probas2 = hcm.predecir_clasificacion_binaria(model,X_test2)
        X_test2["neg_bagging_fraction__lgb_model"] = 0
        X_test2["scale_pos_weight__lgb_model"] =  0
        X_test2["custom_bagging__lgb_model"] =  0
        
        X_test2[best_model] = y_prob2_cb
        
        X_test2['ID_PERSONA'] = ID_P_T2
        
        out_path = '{}/{}/{}/{}'.format(PATH_RESULT,SUB_FOLDER_DELTA,key,macro_region)
        hg.validar_directorio(out_path) 
        X_test2.to_csv(out_path+"/X_t_mas_1.csv",index =False , encoding="utf-8")



export_final = hcm.export_resultado_final_nacional(alto=0.75,medio=0.5, grupos_grados=grupos_grados,
                                                   lista_mr=lista_mr,  path=PATH_RESULT,delta_path=SUB_FOLDER_DELTA)

print(export_final.PREDICCION.value_counts())

#################################### 3.RESULTADO FINAL ######################################

export_final = hcm.export_resultado_final_nacional(alto=0.75,medio=0.5, grupos_grados=grupos_grados,
                                                   lista_mr=lista_mr,  path=PATH_RESULT)



scores = ["Precision","Recall","Average Precision"] #"ROC AUC","F1"
hcm.show_barplot_resultado_final_nacional(grupos_grados=grupos_grados,lista_mr=lista_mr,scores=scores,path=PATH_RESULT)








  