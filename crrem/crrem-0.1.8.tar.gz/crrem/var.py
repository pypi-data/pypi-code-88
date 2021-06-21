import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import xlwings as xw
from crrem.database import DataQ
import warnings
warnings.filterwarnings("ignore")

#import raw data from original crrem worksheet
Input = xw.Book('input.xlsx').sheets['Input']
data = xw.Book('input.xlsx').sheets['Back-end']
Zip_nuts = pd.read_excel(pd.ExcelFile('input.xlsx'), 'Back-end2')
Zip_nuts.set_index('ZIP Code to NUTS mapping', inplace = True)
nuts_id = pd.read_excel(pd.ExcelFile('input.xlsx'), 'Back-end4')
nuts_id.set_index('NUTS_ID', inplace = True)

A1 = pd.DataFrame(data.range('A1:B29').value) #NUTS0 - AR
A1.set_index(0, inplace = True)
A32 = pd.DataFrame(data.range('A32:AK60').value) #Emissions factor: electricity & heat (trade adjusted) - A23
A32.columns = A32.iloc[0]
A32 = A32[1:]
A32.set_index('Country', inplace = True)
A32.columns = list(range(2015,2051))
A109 = pd.DataFrame(data.range('A110:D719').value) #Normalisation
A109.set_index(0, inplace = True)
E10 = pd.DataFrame(data.range('E10:G17').value) #Emission factor: other energy sources -H127
E10.set_index(0, inplace = True)
C1 = pd.DataFrame(data.range('C1:D10').value) #property type acronym 
C1.set_index(0, inplace = True)
C18 = pd.DataFrame(data.range('C18:D29').value) #month number
C18.set_index(0, inplace = True)
C63 = pd.DataFrame(data.range('C63:D106').value) #Global Warming Potential of Cooling Gases
C63.set_index(0, inplace = True)
Target = pd.read_excel(pd.ExcelFile('input.xlsx'), 'GHG Target') #GHG decarbonisation target - AXG
Target.set_index('ta', inplace = True)
Target_energy = pd.read_excel(pd.ExcelFile('input.xlsx'), 'Energy Target')
Target_energy.set_index('ta', inplace = True)
G4 = data.range('G4').value #GHG conversion factor: Gas
G5 = data.range('G5').value #Oil
G6 = data.range('G6').value #Heat/Steam - J123
N1 = pd.DataFrame(data.range('N2:Q30').value) #Share of electricity/fossil fuel used for…
N1.set_index(0, inplace = True)
J3 = pd.DataFrame(data.range('J3:J14').value) #Share of heating per month
K3 = pd.DataFrame(data.range('K3:K14').value) #Share of cooling per month
T14 = pd.DataFrame(data.range('T14:T22').value) #CTX: North Antlantic
T2 = pd.DataFrame(data.range('T2:T13').value)
U14 = pd.DataFrame(data.range('U14:U22').value) #CTY: Continental
U2 = pd.DataFrame(data.range('U2:U13').value) 
V2 = pd.DataFrame(data.range('V2:V13').value) #CUN: Mediterranean

#impport raw data from EPC database
target_level = DataQ("select * from crrem.target_levels").data
target_type = DataQ("select * from crrem.target_type").data
property_type = DataQ("select * from crrem.vw_epc_to_crrem_prop_type").data
country = DataQ("select * from crrem.country").data
country_factor = DataQ("select * from crrem.country_factor").data
currency = DataQ("select * from crrem.currency").data
emission_factor = DataQ("select * from crrem.emission_factors").data
energy_conversion_factor = DataQ("select * from crrem.energy_conversion_factor").data
energy_source = DataQ("select * from crrem.energy_source").data
price = DataQ("select * from crrem.price").data
price.set_index('year', inplace=True)
price['price'] = price['price'].astype(float)
scenario_gw = DataQ("select * from crrem.scenario_gw").data
zip_nuts = DataQ("select * from crrem.zip_to_nuts").data
zip_nuts.set_index('zip_code', inplace=True)
energy_use_type = DataQ("select * from crrem.energy_use_type").data
energy_use_breakdown = DataQ("select * from crrem.energy_use_breakdown").data
epc_main_fuel_mapping = DataQ("select * from crrem.epc_main_fuel_mapping").data
hdd_cdd_by_nuts = DataQ("select * from crrem.hdd_cdd_by_nuts").data
hdd_cdd_by_nuts.set_index('nuts_code', inplace=True)

class Building:
    def __init__(self, building_details, building_price, crrem_data='uk_epc'):
        #add 7 EPC columns as property_details, in a json object
        if crrem_data == 'crrem':
            self.epc = building_details
        elif crrem_data == 'uk_epc': 
            if type(building_details) is int:
                epc = DataQ(f"""select * from public.epcsourcedata where "BUILDING_REFERENCE_NUMBER" = {building_details} """).data
                self.epc = epc.set_index('BUILDING_REFERENCE_NUMBER')
                self.building_price = building_price
            elif type(building_details) is dict:
                #convert row of json to dataframe row
                self.epc = pd.DataFrame(data=building_details,index=[0])
        self.building_price = building_price
        self.stranding_year = None
        self.loss_vlaue = None

    def VAR(self, target_temp=1.5, RCP_scenario=4.5, discount_factor=0.02, end_year=2050, Diagram=False, crrem_data='uk_epc'):
    # /////////////////////////////////////////////////////////////////
    # Original CRREM Model
    # ///////////////////////////////////////////////////////////////// 
        if crrem_data == 'crrem':
            ## Estimate current emissions
            years = list(range(2018,2051))
            '''
            a. data normalisation
            '''
            #1. weather noramlisation: heat/cool
            AXC279_AXE = A109.iloc[277:554,:]
            AXC279_AXE.set_index(1, inplace = True)
            AXC279_AXD = AXC279_AXE.iloc[:,:-1]
            AXC584_AXE = A109.iloc[582:610,:]
            AXC584_AXE.set_index(1, inplace = True)
            AXC584_AXD = AXC584_AXE.iloc[:,:-1]

            AXC2_AXE = A109.iloc[0:277,:]
            AXC2_AXE.set_index(1, inplace = True)
            AXC2_AXD = AXC2_AXE.iloc[:,:-1]
            AXC556_AXE = A109.iloc[554:582,:]
            AXC556_AXE.set_index(1, inplace = True)
            AXC556_AXD = AXC556_AXE.iloc[:,:-1]

            #AR, country acronym
            if self.epc['input_M'] != 0:
                AR = A1.loc[self.epc['input_M'],1]
            else:
                AR = self.epc['input_M']

            #AP: NUTS3
            ZIP = AR + str(self.epc['input_O'])
            AP = Zip_nuts.loc[ZIP].iloc[0]

            try:
                AWZ = (AXC279_AXD.loc[AP[:4]]/AXC279_AXE.loc[AP[:4]][3])[2]
            except KeyError:
                AWZ = (AXC584_AXD.loc[AP[:2]]/AXC584_AXE.loc[AP[:2]][3])[2]
            try:
                AXA = (AXC2_AXD.loc[AP[:4]]/AXC2_AXE.loc[AP[:4]][3])[2]
            except KeyError:
                AXA = (AXC556_AXD.loc[AP[:2]]/AXC556_AXE.loc[AP[:2]][3])[2]

            #2. data coverage normalisation
            if self.epc['input_AQ']!= 0:
                AWT = self.epc['input_AR']/self.epc['input_AQ'] 
            else:
                AWT = 0

            if self.epc['input_AG']!= 0:
                AWQ = self.epc['input_AR']/self.epc['input_AG']
            else:
                AWQ = 0

            if self.epc['input_AJ']!= 0:
                AWR = self.epc['input_AR']/self.epc['input_AJ'] 
            else:
                AWR= 0

            if self.epc['input_AM']!= 0:
                AWS = self.epc['input_AR']/self.epc['input_AM'] 
            else:
                AWS = 0

            if self.epc['input_AU']!= 0:
                AWU = self.epc['input_AR']/self.epc['input_AU'] 
            else:
                AWU = 0

            if self.epc['input_AY']!= 0:
                AWV = self.epc['input_AR']/self.epc['input_AY'] 
            else:
                AWV = 0

            #3. month noramlisation
            AWX = 12/self.epc['input_AJ'] #month normalisation

            #4. vacant area normalisation
            AWY = self.epc['input_AR']/(self.epc['input_AR']-self.epc['input_AD']) 

            #5. Electricity normalisation by month across different regions(North Atlantic, Continental, Mediterranean)
            #CTX - CUS
            #CTZ - starting month number
            CTZ = C18.loc[self.epc['input_I']][1]
            #CUA - ending month number
            CUA = CTZ + self.epc['input_J'] - 1
            #CUB_CUM: Month included

            months = list(range(1,13))
            CUB_CUM = list(range(1,13))
            for month in months:
                if (month >= CTZ and month <= CUA) or (month+12 >= CTZ and month+12 <= CUA):
                        CUB_CUM[month-1] = 1
                else:
                    CUB_CUM[month-1] = 0

            #CTX/CTY/CUN
            CTX29 = T14

            CTX17 = T2

            CTY29 = U14

            CTY17 = U2

            CUN17 = V2

            CUB_CUM_i = pd.DataFrame(CUB_CUM).reset_index().drop(['index'], axis = 1)
            if (AR==CTX29).any()[0]:
                CUS = 1/(CUB_CUM_i*CTX17).sum()[0]
            elif (AR == CTY29).any()[0]:
                CUS = 1/(CUB_CUM_i * CTY17).sum()[0]
            else:
                CUS = 1/(CUB_CUM_i * CUN17).sum()[0]

            #CUO: Heat_norm_12
            CUN3 = J3
            CUO = 1/(CUB_CUM_i * CUN3).sum()[0]

            #CUQ: Cool_norm_12
            CUP3 = K3
            CUQ = 1/(CUB_CUM_i * CUP3).sum()[0]

            '''
            b. BI_CO - HDD index and CT_DZ - CDD index
            '''
            #Share of electricity/fossil fuel used for heating/cooling
            BMG_BMJ = N1

            #BI_CO - HDD index
            BI_CO = pd.Series(0.0,index=years)
            for year in years:
                BI_CO[year] = ((nuts_id.loc[AP]['HDD_2015'] + (year-2015)*nuts_id.loc[AP]['HDD_45_pa'])/(nuts_id.loc[AP]['HDD_2015'] + 3*nuts_id.loc[AP]['HDD_45_pa']))

            #CT_DZ - CDD index
            CT_DZ = pd.Series(0.0,index=years)
            for year in years:
                CT_DZ[year] = ((nuts_id.loc[AP]['CDD_2015'] + (year-2015)*nuts_id.loc[AP]['CDD_45_pa'])/(nuts_id.loc[AP]['CDD_2015'] + 3*nuts_id.loc[AP]['CDD_45_pa']))

            '''
            c. KA:KH: emission share
            '''
            #KA: export emission
            A32_year = A32.loc[AR][self.epc['input_F']]

            #slice A32 for UK 2018
            A32_UK_base = A32.loc['UK'][years[0]]

            #slice A32 for 2018
            A32_base = A32.loc[AR][years[0]]

            KA = -AWT*self.epc['input_BQ']*G6-AWQ*self.epc['input_BL']*A32_year

            #JT - JZ
            #JT - Electricity emission
            JT = AWQ*(self.epc['input_AF']-self.epc['input_BM'])*A32_base + self.epc['input_BM']*A32_year

            #JU - Gas emission
            JU = AWR*self.epc['input_AI']*G4

            #JV - Oil emission
            JV = AWS*self.epc['input_AL']*G5

            #JW - District heating emission
            JW = AWT*self.epc['input_AO']*G6*A32_base/A32_UK_base

            #JX - District cooling emission
            JX = AWU*self.epc['input_AS']*G6*A32_base/A32_UK_base

            #JY - Other emission # can add another
            E10_AW = E10.loc[self.epc['input_AW']].fillna(0)[2]
            JY = AWV*self.epc['input_AX']*E10_AW

            #JZ - Fugitive emission  # can add another
            #fugitive gas - global warming potential
            C63_BF = C63.loc[self.epc['input_BF']][1]
            AT = C63_BF*self.epc['input_BG'] #leak
            JZ = AT

            #Total emission calculation
            #KJ: AS.LENG_norm 
            KJ = JT*CUS+(JU+JV+JW+JY)*CUO+JX*CUQ+JZ*AWX+KA*AWX

            # KB: Electricity emission share
            KB = JT/(JT+JU+JV+JW+JX+JY+JZ)

            # KC: Gas emission share
            KC = JU/(JT+JU+JV+JW+JX+JY+JZ)

            # KD: Oil emission share
            KD = JV/(JT+JU+JV+JW+JX+JY+JZ)

            # KE: Gas emission share
            KE = JW/(JT+JU+JV+JW+JX+JY+JZ)

            # KF: Gas emission share
            KF = JX/(JT+JU+JV+JW+JX+JY+JZ)

            # KG: Gas emission share
            KG = JY/(JT+JU+JV+JW+JX+JY+JZ)

            # KH: Gas emission share
            KH = JZ/(JT+JU+JV+JW+JX+JY+JZ)

            '''
            d. KK: final total emissions(kgCO2e)
            '''
            KK = -KA+(KJ+KA)*(AWY*KB*(1+(BMG_BMJ.loc[AR][1])*(BI_CO[years[0]]*AWZ-1) 
                        + BMG_BMJ.loc[AR][2]*(CT_DZ[years[0]]*AXA-1)) + (KC+KD+KE)
                        * (1+(BMG_BMJ.loc[AR][3]*(BI_CO[years[0]]*AWZ-1)))*AWZ+KF*AXA)

            ## Projected future emissions
            '''
            a. EE_FK: grid index
            '''
            EE_FK = pd.Series(0.0,index=years)
            for year in years:
                EE_FK[year] = (A32.loc[AR][year]/A32.loc[AR][years[0]])

            '''
            b. CZZ_DBF: Electricity procurement
            '''
            CZZ = AWQ*self.epc['input_AF']*AWY*((1+(BMG_BMJ.loc[AR][1]*(BI_CO[years[0]]*AWZ-1))+(BMG_BMJ.loc[AR][2]*(CT_DZ[years[0]]*AXA-1))))*CUS
            '''
            c. KP: emissions projection(kgCO2e)
            '''
            KP = pd.Series(0.0,index=years)
            for year in years:
                KP[year] = KK*(KB*(((EE_FK[year]/EE_FK[years[0]])*(self.epc['input_AF']/CZZ)
                +(1-self.epc['input_AF']/CZZ))*(1+BMG_BMJ.loc[AR][1]*(BI_CO[year]-1))) + (KC+KD+KG)*
                (BI_CO[year]/BI_CO[years[0]])*(1+BMG_BMJ.loc[AR][3]*(BI_CO[year]-1))
                + KF*(CT_DZ[year]/CT_DZ[years[0]]) + KE*BI_CO[year]+KH)

            '''
            d. MA: emissions intensity projection(kgCO2e/m2)
            '''
            MA = KP/self.epc['input_AC']

            ## Derive emissions target
            #CRREM can provide property type by percentage of floor area as self.epc['input, and compute target through weighted average
            country_code = A1.loc[''.join(map(str, self.epc['input_M'])),1]
            property_type_code = C1.loc[''.join(map(str, self.epc['input_Q'])),1]
            asset_code1 = country_code + '_' + property_type_code + '_' + '1.5'
            FP = Target.loc[asset_code1]

            asset_code2 = country_code + '_' + property_type_code + '_' + '2'
            HA = Target.loc[asset_code2]
            if target_temp == 1.5:
                target = FP
            elif target_temp == 2:
                target = HA
                
            ## VAR calculation
            floor_area = self.epc['input_AC']
            emission = MA
            total_emission = emission * floor_area
            total_target = target * floor_area
            carbon_price = price[price['source']=='carbon']['price'][:end_year-2018+1]
            excess_cost = carbon_price * (total_emission - total_target)

            costs = pd.Series(np.nan, index=years)
            value = pd.Series(np.nan, index=years)
            for year in years:
                if excess_cost[year] < 0:
                    costs[year] = 0
                    value[year] = excess_cost[year]
                else:
                    costs[year] = excess_cost[year]
                    value[year] = 0

            discount_costs = costs.tolist().copy()
            discount_value = value.tolist().copy()

            for year in years:
                discount_costs[year - 2018] = discount_costs[year - 2018] / (1 + discount_factor) ** (year - 2018)
                discount_value[year - 2018] = discount_value[year - 2018] / (1 + discount_factor) ** (year - 2018)

            VAR = (sum(discount_costs) + sum(discount_value)) / self.building_price
            
            #stranding year and loss value
            stranding = target - emission
            self.stranding_year = stranding[stranding < 0].index[0]
            self.loss_value = sum(discount_costs) + sum(discount_value)
            
            ## Stranding Diagram
            if Diagram == True:
                #import MA as emission metric
                Baseline = [emission.iloc[0]]*len(emission) #create baseline pandas series with same index as climate_grid
                baseline = pd.Series(Baseline, index = emission.index)   

                #plot diagram
                plt.figure(figsize = (20,10))
                plt.plot(target, 'g', label = 'Decarbonisation target')
                plt.plot(emission, 'k', label = 'Climate and grid corrected asset performance')
#                 plt.plot(baseline, ':k', label = 'Baseline asset performance')
#                 plt.plot(baseline.iloc[[0]],'kD', markersize = 10, label = '2018 performance') 

                #highlight stranding year
                stranding = target - emission
                stranding_year = stranding[stranding < 0].index[0]
                plt.plot(emission[[stranding_year]], 'ro', markersize = 20, label = 'Stranding')

                #Excess emissions
                plt.fill_between(years, target.tolist(), emission.tolist(), where = (target < emission), color='C1', alpha=0.3, label = 'Excess emissions')
                plt.legend(loc = 'best', fontsize = 12)

                #set title and axis labels
                plt.title(f'Stranding Diagram', fontsize = 25)
                plt.xlabel('Year', fontsize = 15)
                plt.ylabel('GHG intensity [kgCO2e/m²/a]', fontsize = 15)
                plt.show()
            
    # /////////////////////////////////////////////////////////////////
    # EPC Model
    # /////////////////////////////////////////////////////////////////  
        elif crrem_data == 'uk_epc':
            # 1.Data preparation GHG emission target
            # find property type id
            property_type_id = property_type.loc[property_type['epc_prop_type'] == self.epc['PROPERTY_TYPE'].iloc[0]]['prop_use_type_id'].iloc[0]

            # specify target based on property type/target type/scenario
            years = list(range(2018,end_year+1))
            if target_temp == 1.5:
                gw_scenario_id = 1
            elif target_temp == 2.0:
                gw_scenario_id = 2
            emission_target = target_level[(target_level['prop_use_type_id']==property_type_id) & (target_level['target_type_id']==1) & (target_level['gw_scenario_id']==gw_scenario_id)]['target_level']
            emission_target = emission_target[:end_year-2018+1]
            emission_target.index = years
            energy_target = target_level[(target_level['prop_use_type_id']==property_type_id) & (target_level['target_type_id']==2) & (target_level['gw_scenario_id']==gw_scenario_id)]['target_level']
            energy_target = energy_target[:end_year-2018+1]
            energy_target.index = years

            # HDD/CDD projection
            # HDD - HDD index
            RCP = 'RCP' + str(RCP_scenario)

    #         if self.epc['POSTCODE'].iloc[0] != 0:
    #             NUTS3 = 'UK' + self.epc['POSTCODE'].iloc[0].split(' ')[0]

            years_index = list(range(3, 36))
            HDD = pd.DataFrame(columns=years_index, index=[1])
            for year in years_index:
                if RCP == 'RCP4.5':
                    if len(self.epc['NutsCode']) > 1:
                        HDD.iloc[0, year - 3] = (hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_2015'].iloc[0] + year *
                                                 hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_rcp45_pa'].iloc[0]) / (
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']][
                                                                'hdd_2015'].iloc[0] + 3 *
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_rcp45_pa'].iloc[0])
                    else:
                        HDD.iloc[0, year - 3] = (hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_2015'].iloc[0] + year *
                                                 hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_rcp45_pa'].iloc[0]) / (
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_2015'].iloc[0] + 3 *
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_rcp45_pa'].iloc[0])
                elif RCP == 'RCP8.5':
                    if len(self.epc['NutsCode']) > 1:
                        HDD.iloc[0, year - 3] = (hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_2015'].iloc[0] + year *
                                                 hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_rcp85_pa'].iloc[0]) / (
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']][
                                                                'hdd_2015'].iloc[0] + 3 *
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_rcp85_pa'].iloc[0])
                    else:
                        HDD.iloc[0, year - 3] = (hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_2015'].iloc[0] + year *
                                                 hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_rcp85_pa'].iloc[0]) / (
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_2015'].iloc[0] + 3 *
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['hdd_rcp85_pa'].iloc[0])

            # assumption1: if one zip macthes multiple nuts, take the first nuts
            # CDD - CDD index
            CDD = pd.DataFrame(columns=years_index, index=[1])
            for year in years_index:
                if RCP == 'RCP4.5':
                    if len(self.epc['NutsCode']) > 1:
                        CDD.iloc[0, year - 3] = (hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_2015'].iloc[0] + year *
                                                 hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_rcp45_pa'].iloc[0]) / (
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']][
                                                                'cdd_2015'].iloc[0] + 3 *
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_rcp45_pa'].iloc[0])
                    else:
                        CDD.iloc[0, year - 3] = (hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_2015'].iloc[0] + year *
                                                 hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_rcp45_pa'].iloc[0]) / (
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_2015'].iloc[0] + 3 *
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_rcp45_pa'].iloc[0])
                else:
                    if len(self.epc['NutsCode']) > 1:
                        CDD.iloc[0, year - 3] = (hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_2015'].iloc[0] + year *
                                                 hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_rcp85_pa'].iloc[0]) / (
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']][
                                                                'cdd_2015'].iloc[0] + 3 *
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_rcp85_pa'].iloc[0])
                    else:
                        CDD.iloc[0, year - 3] = (hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_2015'].iloc[0] + year *
                                                 hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_rcp85_pa'].iloc[0]) / (
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_2015'].iloc[0] + 3 *
                                                            hdd_cdd_by_nuts.loc[self.epc['NutsCode']]['cdd_rcp85_pa'].iloc[0])
            CDD.columns = list(range(2018, 2051))
            HDD.columns = list(range(2018, 2051))
            HDD.fillna(0, inplace=True)
            CDD.fillna(0, inplace=True)
            HDD = HDD.iloc[:,:end_year-2018+1]
            CDD = CDD.iloc[:,:end_year-2018+1]

            # 2. GHG emission projection
            # emission data
            #impute missing data with median of property type
            if self.epc['CO2_EMISS_CURR_PER_FLOOR_AREA'].iloc[0] == None:
                current_emission = self.epc['CO2_EMISS_CURR_PER_FLOOR_AREA_Median'].iloc[0]
            else:
                current_emission = self.epc['CO2_EMISS_CURR_PER_FLOOR_AREA'].iloc[0]
            if self.epc['ENERGY_CONSUMPTION_CURRENT'].iloc[0] == None:
                current_energy = self.epc['ENERGY_CONSUMPTION_CURRENT_Median'].iloc[0]
            else:
                current_energy = self.epc['ENERGY_CONSUMPTION_CURRENT'].iloc[0]

            elec_heat = energy_use_breakdown['percentage'][0] / 100  # share of electricity for heating in UK
            elec_cool = energy_use_breakdown['percentage'][1] / 100
            fuel_heat = energy_use_breakdown['percentage'][2] / 100
            grid = emission_factor['value']  # emission factor for UK
            start = grid[0]
            for i in grid.index:
                grid[i] = grid[i]/start

            # electricity usage share
            electricity_share = epc_main_fuel_mapping.loc[epc_main_fuel_mapping['epc_main_fuel'] == self.epc['MAIN_FUEL'].iloc[0]]['weight_elec'].iloc[0]
            elec_energy = current_energy*electricity_share
            elec_procured = elec_energy*((1+(elec_heat*(HDD.iloc[0, 0]-1)+elec_cool*(CDD.iloc[0, 0]-1))))

            emission = pd.Series(0, index=list(range(2018, 2051)))

            # assumption 2: district heating/cooling and fugitive emission not considered
            for year in years:
                emission.iloc[year - 2018] = current_emission*(electricity_share*(((grid[year - 2018]/grid[0])
                            *(elec_energy/elec_procured)+(1-elec_energy/elec_procured))
                            *(1+elec_heat*(HDD.iloc[0, year-2018]-1)+elec_cool*(CDD.iloc[0, year-2018]-1)))
                            +(1 - electricity_share)*(HDD.iloc[0, year - 2018]/HDD.iloc[0, 2018 - 2018])
                            *(1 + fuel_heat*(HDD.iloc[0, year - 2018])))

            emission = emission[:end_year-2018+1]
            emission_baseline = pd.Series(current_emission)
            emission_baseline = emission_baseline.repeat(len(emission.T))
            emission_baseline.index = years 
            emission_excess = emission - emission_target
            if len(emission_excess[emission_excess > 0]) == 0:
                emission_stranding_year = 2050
            else:
                emission_stranding_year = emission_excess[emission_excess > 0].index[0]

            # 3. energy projection
            # energy energy projection
            energy = pd.Series(0, index=list(range(2018, 2051)))
            for year in years:
                energy.iloc[year - 2018] = current_energy*(electricity_share*(((grid[year - 2018]/grid[0])
                        *(elec_energy/elec_procured)+(1-elec_energy/elec_procured))
                        *(1+elec_heat*(HDD.iloc[0, year-2018]-1)+elec_cool*(CDD.iloc[0, year-2018]-1)))
                        +(1 - electricity_share)*(HDD.iloc[0, year - 2018]/HDD.iloc[0, 2018 - 2018])
                        *(1 + fuel_heat*(HDD.iloc[0, year - 2018])))

            energy = energy[:end_year-2018+1]
            energy_baseline = pd.Series(current_energy)
            energy_baseline = energy_baseline.repeat(len(energy.T))
            energy_baseline.index = years 
            energy_excess = energy - energy_target
            if len(energy_excess[energy_excess > 0]) == 0:
                energy_stranding_year = 2050
            else:
                energy_stranding_year = energy_excess[energy_excess > 0].index[0]

            # 4. energy costs
            elec_cost = price[price['source']=='elect_incl_vat']['price'][:end_year-2018+1] #electricity price incl. VAT
            gas_cost = price[price['source']=='gas_incl_vat']['price'][:end_year-2018+1] #gas price incl. VAT
            oil_cost = price[price['source']=='oil_incl_vat']['price'][:end_year-2018+1] #oil price incl. VAT
            wood_cost = price[price['source']=='wood_incl_vat']['price'][:end_year-2018+1] #wood pellets price incl. VAT
            coal_cost = price[price['source']=='coal_incl_vat']['price'][:end_year-2018+1] #coal price incl. VAT
            carbon_price = price[price['source']=='carbon']['price'][:end_year-2018+1] #carbon price incl. VAT
            total_energy = current_energy

            elec_cost = total_energy*elec_cost*epc_main_fuel_mapping.loc[epc_main_fuel_mapping['epc_main_fuel'] == self.epc['MAIN_FUEL'].iloc[0]]['weight_elec'].iloc[0]
            gas_cost = total_energy*gas_cost*epc_main_fuel_mapping.loc[epc_main_fuel_mapping['epc_main_fuel'] == self.epc['MAIN_FUEL'].iloc[0]]['weight_gas'].iloc[0]
            oil_cost = total_energy*oil_cost*epc_main_fuel_mapping.loc[epc_main_fuel_mapping['epc_main_fuel'] == self.epc['MAIN_FUEL'].iloc[0]]['weight_oil'].iloc[0]
            wood_cost = total_energy*wood_cost*epc_main_fuel_mapping.loc[epc_main_fuel_mapping['epc_main_fuel'] == self.epc['MAIN_FUEL'].iloc[0]]['weight_wood'].iloc[0]
            coal_cost = total_energy*coal_cost*epc_main_fuel_mapping.loc[epc_main_fuel_mapping['epc_main_fuel'] == self.epc['MAIN_FUEL'].iloc[0]]['weight_coal'].iloc[0]

            # 5. excess carbon costs and value at risk
            floor_area = self.epc['TOTAL_FLOOR_AREA'].iloc[0]
            total_emission = emission * floor_area
            total_target = emission_target * floor_area
            excess_cost = carbon_price * (total_emission - total_target)

            costs = pd.Series(np.nan, index=years)
            value = pd.Series(np.nan, index=years)
            for year in years:
                if excess_cost[year] < 0:
                    costs[year] = 0
                    value[year] = excess_cost[year]
                else:
                    costs[year] = excess_cost[year]
                    value[year] = 0

            discount_costs = costs.tolist().copy()
            discount_value = value.tolist().copy()

            for year in years:
                discount_costs[year - 2018] = discount_costs[year - 2018] / (1 + discount_factor) ** (year - 2018)
                discount_value[year - 2018] = discount_value[year - 2018] / (1 + discount_factor) ** (year - 2018)

            VAR = (sum(discount_costs) + sum(discount_value)) / self.building_price

            self.stranding_year = emission_stranding_year
            self.loss_value = sum(discount_costs) + sum(discount_value)
            #plot diagram
            if Diagram == True:
                years = list(range(2018,end_year+1))
                plt.figure(figsize = (20,10))
                plt.plot(emission_target, 'g', label = 'Decarbonisation emission_target')
                plt.plot(emission, 'k', label = 'Climate and grid corrected asset performance')
#                 plt.plot(emission_baseline, ':k', label = 'emission_baseline asset performance')
#                 plt.plot(emission_baseline.iloc[[0]],'kD', markersize = 10, label = '2018 performance') 

                #highlight stranding year
                stranding = emission_target - emission
                if (stranding<0).any():
                    stranding_year = stranding[stranding < 0].index[0]
                    plt.plot(emission[[stranding_year]], 'ro', markersize = 20, label = 'Stranding')

                #Excess emissions
                plt.fill_between(years, emission_target.tolist(), emission.tolist(), where = (emission_target < emission), color='C1', alpha=0.3, label = 'Excess emissions')
                plt.legend(loc = 'best', fontsize = 12)

                #set title and axis labels
                plt.title(f'Stranding Diagram(Asset #{self.epc.index.tolist()[0]})', fontsize = 25)
                plt.xlabel('Year', fontsize = 15)
                plt.ylabel('GHG intensity [kgCO2e/m²/a]', fontsize = 15)
                plt.show()

        return VAR

class Portfolio:
    def __init__(self, buildings):
        self.buildings = buildings
    
    def add_building(self, building):
        self.buildings.append(building)
        
    def VAR(self,target_temp=1.5, RCP_scenario=4.5, discount_factor=0.02, end_year=2050, Diagram=False, crrem_data='uk_epc'):
        total_loss = 0
        total_price = 0
        years = list(range(2018,end_year+1))
        strand_buildings = pd.Series(0, index=years)
        for building in self.buildings:
            building.VAR(target_temp=target_temp, RCP_scenario=RCP_scenario, discount_factor=discount_factor, end_year=end_year, Diagram=False, crrem_data=crrem_data)
            total_loss += building.loss_value
            total_price += building.building_price
            if building.stranding_year < end_year:
                strand_buildings[building.stranding_year] += 1
        if Diagram == True:
            strand_buildings = strand_buildings.cummax()
            plt.figure(figsize = (20,10))
            plt.plot(strand_buildings, 'g', label = 'Decarbonisation emission_target')
            plt.title('Number of stranding assets over time', fontsize=25)
            plt.show()          
        return total_loss/total_price
