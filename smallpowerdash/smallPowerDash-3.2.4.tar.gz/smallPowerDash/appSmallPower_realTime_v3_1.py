import importlib
import dash, dash_core_components as dcc, dash_html_components as html, dash_bootstrap_components as dbc
import dorianUtils.dccExtendedD as dcce
import smallPowerDash.smallPowerTabs as sptabs

# ==============================================================================
#                       INSTANCIATIONS
# ==============================================================================
connParameters ={
'host'     : "192.168.1.44",
'port'     : "5434",
'dbname'   : "Jules",
'user'     : "postgres",
'password' : "SylfenBDD"
}

dccE=dcce.DccExtended()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],title='RealTime SmallPower',
                                                        url_base_pathname = '/smallPowerRealTime/')

tabSelectedTagsRT = sptabs.RealTimeTagSelectorTab(app,connParameters=connParameters)
titleHTML=html.H1('Small Power Real Time V3.1')
tabsLayout= dccE.createTabs([tabSelectedTagsRT])
app.layout = html.Div([html.Div(titleHTML),html.Div(tabsLayout)])
# app.run_server(port=45000,debug=True,use_reloader=False)
app.run_server(port=45000,host='0.0.0.0',debug=False,use_reloader=False)
