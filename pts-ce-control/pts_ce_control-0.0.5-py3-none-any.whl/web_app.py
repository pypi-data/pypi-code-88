import sys
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import base64
from dash.dependencies import Input, Output, State, MATCH
import time
import re
import logging
import can
import pts_ce_control.cell_emulator as cell_emulator

STARTUP = True
ce = None
no_cell_emulators = 1
interface = "pcan"
vector_app = None

def run_webapp():
    print(""" \
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,*************************************************
    ,****..........***..........****,****...,**...,***
    ,****          **,          ********,   **,   ****
    ,****   ,*******,*******.   ****,***   .**.  .**,*
    ,****   ,***************.   ********   ,**   ,****
    ,****   ,***************.   ****,**,   **,   *****
    ,****   ,***************.   *******   .**   ,*****
    ,****   ,*******,*******.   ****,**   ,*,   ****,*
    ,****   ,***************.   ******,   **.   ******
    ,****   ,***************.   ****,*   .**   ,******
    ,****   ,***************.   ******   **,   *******
    ,****   ,*******,*******.   ****,,   **.  .*****,*
    ,****   ,***************.   *****   ,**   ,*******
    ,****   ,***************.   ****,   ***   ********
    ,****   ,***************.   ****,   **   .********
    ,***,   ,***,***,***,***.   ,***   ,,*   ***,***,*
    ,****          **,          ****   ,*,   *********
    ,*******************************,*****************
    ,*************************************************
    """)
    print("[]// PTS CE Control Application")
    print("Open http://localhost:8050 in your webbrowser to use this app")

    if STARTUP:
        cell_voltage = 0

    def local_ce_state():
        # Init Data
        data = {}
        for i in range(19):
            data["Cell" + str(i)]={
                                    "voltage" : cell_voltage,
                                    "current" : 0
                                    }
        return data

    def get_ce_values():
        if STARTUP:
            ce_state = local_ce_state()
        else:
            ce_state = ce.get_ce_state()
        cells = []
        voltages = []
        currents = []
        for cell in ce_state:
            cells.append(cell)
            voltages.append(ce_state[cell]['voltage'])
            currents.append(ce_state[cell]['current'])
        df = {'cell': cells, 'voltage': voltages, 'current': currents}
        return df


    def get_options(label_list):
        dict_list = []
        for i in label_list:
            dict_list.append({'label': i, 'value': i})
        return dict_list

    def get_ce_panel(ce_id=1):
        panel = html.Div(className='row',
             children=[
                html.Div(className='four columns div-user-controls',
                         children=[
                             html.Img(src=app.get_asset_url('pass_logo_03202020.svg')),
                             html.H1(f'PTS CE Control Frontend - CE ID {ce_id}'),
                             html.P('See current Values and Set Voltages'),
                             html.P('Pick The Cells you want below'),
                             html.Div(
                                 className='div-for-dropdown',
                                 children=[
                                     dcc.Dropdown(id={'type': 'cellselector','index': ce_id}, options=get_options(get_ce_values()['cell']),
                                                  multi=True, value=[get_ce_values()['cell'].sort()],
                                                  style={'backgroundColor': '#1E1E1E'},
                                                  className='cellselector'
                                                  )
                                          ],
                                style={'color': '#1E1E1E'}
                                     ),
                            html.Div(
                                 children = [
                                     html.Button(   'Select All',
                                                    id={'type': 'select-all','index': ce_id},
                                                    n_clicks=0,
                                                    type="submit",
                                                    className='button'),
                                     html.P("Cell Voltage Setpoint [V]  "),
                                     dcc.Input(
                                                    placeholder='2.5',
                                                    type='number',
                                                    value=0,
                                                    id={'type': 'cellvoltageinput','index': ce_id},
                                                    style={'backgroundColor': '#1E1E1E'}
                                                ),

                                     html.P("Cell Voltage Amplitude Setting [V]  "),
                                     dcc.Input(
                                                    placeholder='2.5',
                                                    type='number',
                                                    value=0,
                                                    id={'type': 'cellvoltageamp','index': ce_id},
                                                    style={'backgroundColor': '#1E1E1E'}
                                                ),

                                     html.P("Cell Voltage Frequency Setpoint [Hz]  "),
                                     dcc.Input(
                                                    placeholder='2.5',
                                                    type='number',
                                                    value=0,
                                                    id={'type': 'cellvoltagefreq','index': ce_id},
                                                    style={'backgroundColor': '#1E1E1E'}
                                                ),
                                            ]
                                    )
                                ]

                         ),
                html.P(id={'type': 'placeholder','index': ce_id}),
                html.Div(className='eight columns div-for-charts bg-grey',
                         children=[
                             dcc.Graph(id={'type': 'timeseries','index': ce_id}, config={'displayModeBar': False}, animate=True),
                             dcc.Interval( id = {'type': 'interval-component','index': ce_id},interval = 1*1000,n_intervals = 0)
                         ])
                          ])
        return panel

    def init_can():
        global ce
        global STARTUP
        if interface == "pcan":
            can.rc['interface'] = 'pcan'
            can.rc['channel'] = 'PCAN_USBBUS1'
            can.rc['bitrate'] = 500000
            bus = can.interface.Bus()

            ##### Cell Emulator Controller
            ce = cell_emulator.CellEmulator(bus=bus,address='CellEmulator1')
            STARTUP = False
        else:
            can.interface.Bus(bustype='vector',
                              app_name=vector_app,
                              channel=[0],
                              bitrate=500000)

            ##### Cell Emulator Controller
            ce = cell_emulator.CellEmulator(bus=bus,address='CellEmulator1')
            STARTUP = False


    # Initialize the app
    app = dash.Dash(__name__)
    app.config.suppress_callback_exceptions = True

    #Setup Cell Emulators
    ce_tabs = []
    for i in range(no_cell_emulators):
        ce_tabs.append(dcc.Tab(label=f'Cell emulator {i+1}',className='custom-tab',children=[get_ce_panel(i+1)]))

    app.layout = html.Div([dcc.Tabs(parent_className='custom-tabs',className='custom-tabs-container',children=ce_tabs)])

    @app.callback(
        Output({'type': 'cellselector', 'index': MATCH}, 'value'),
        Input({'type': 'select-all', 'index': MATCH}, 'n_clicks'),
        [State({'type': 'cellselector', 'index': MATCH}, 'options'),
         State({'type': 'cellselector', 'index': MATCH}, 'value')])
    def select_all(selected, options, values):
        return [i['value'] for i in options]

    @app.callback(Output({'type': 'cellvoltageinput', 'index': MATCH}, 'value'),
                  [Input({'type': 'cellvoltageinput', 'index': MATCH}, 'value'),
                   Input({'type': 'cellselector', 'index': MATCH},'value'),
                   Input({'type': 'cellvoltageamp', 'index': MATCH}, 'value'),
                   Input({'type': 'cellvoltagefreq', 'index': MATCH}, 'value'),
                   State({'type': 'cellvoltageselector', 'index': MATCH}, 'id')]
                  )
    def update_values(slider_value,selected_cells,amp,freq,id):
        print(f"Working on Cell Emulator #{id['index']}")
        if not STARTUP:
            ce.ce_address = f"CellEmulator{id['index']}"
            for cell_str in selected_cells:
                cell = int(re.findall('\d+', cell_str)[0])
                if slider_value >= 0.5:
                    ce.set_cell_relay_state(cell,1)
                else:
                    ce.set_cell_relay_state(cell,0)
            if ce is not None:
                for cell_str in selected_cells:
                    cell = int(re.findall('\d+', cell_str)[0])
                    print(f"Setting cell {cell} with voltage {slider_value}, frequency {amp} and amplitude {freq}")
                    ce.set_single_cell_voltage(cell,slider_value,freq=freq,ampl=amp)
            else:
                for cell_str in selected_cells:
                    cell = int(re.findall('\d+', cell_str)[0])
                    ce.set_cell_relay_state(cell,0)
        return slider_value


    # @app.callback(Output({'type': 'cellvoltageselector', 'index': MATCH}, 'value'),
    #               Input({'type': 'cellvoltageinput','index': MATCH}, 'value'))
    # def update_value_input(slider_value):
    #     return slider_value

    # Callback for timeseries
    @app.callback(Output({'type': 'timeseries', 'index': MATCH}, 'figure'),
                  [Input({'type': 'interval-component', 'index': MATCH}, 'n_intervals')])
    def update_graph(n_intervals):
        print("Updating...")
        global STARTUP
        if n_intervals == 1:
            init_can()
            df = get_ce_values()
        else:
            df = get_ce_values()
        figure = {'data': [go.Bar(  x = df['cell'],
                                    y = df['voltage'],
                                    name = 'Cell Voltage',
                                    yaxis = 'y1',
                                    offsetgroup=0),
                           go.Bar(  x = df['cell'],
                                    y = df['current'],
                                    name = 'Cell Current',
                                    yaxis = 'y2',
                                    offsetgroup=1)],
                  'layout': go.Layout(
                      colorway=["#55BBE2", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                      template='plotly_dark',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      margin={'b': 15},
                      hovermode='x',
                      autosize=True,
                      barmode='group',
                      title={'text': 'Cell Voltages', 'font': {'color': 'white'}, 'x': 0.5},
                      xaxis={},
                      yaxis= {'title': 'Cell Voltage [V]', 'range': [0, 5]},
                      yaxis2= {'title': 'Cell Current [mA]', 'side': 'right','range': [0, 500]}
                  ),

                  }

        return figure



    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run_server(debug=True)

if __name__ == '__main__':
    run_webapp()
