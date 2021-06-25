import importlib
import dash, dash_core_components as dcc, dash_html_components as html, dash_bootstrap_components as dbc
import dorianUtils.dccExtendedD as dcce
import smallPowerDash.smallPowerTabs as sptabs

# ==============================================================================
#                       INSTANCIATIONS
# ==============================================================================
baseFolder = '/home/dorian/data/sylfenData/'
folderPkl  = baseFolder + 'smallPower_pkl/'

dccE=dcce.DccExtended()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],title='small power explorer',url_base_pathname = '/smallPowerDash/')
tabCompute = sptabs.ComputationTab(folderPkl,app,baseId='ct_')
tabModule  = sptabs.ModuleTab(folderPkl,app,baseId='mt_')
tabSelectedTags = sptabs.TagSelectedSmallPowerTab(folderPkl,app,baseId='ts_')
tabUnitSelector = sptabs.UnitSelectorSmallPowerTab(folderPkl,app,baseId='ut_')
tabMultiUnits  = sptabs.MultiUnitSmallPowerTab(folderPkl,app,baseId='mu_')

titleHTML=html.H1('Small Power Explorer V3.1')
tabsLayout= dccE.createTabs([tabSelectedTags,tabUnitSelector,tabMultiUnits,tabModule,tabCompute])
app.layout = html.Div([html.Div(titleHTML),html.Div(tabsLayout)])
app.run_server(port=45001,debug=True,use_reloader=False)
