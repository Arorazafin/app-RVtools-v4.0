
# Dash package
from pandas.io.sql import has_table
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import dash_html_components as html
import dash_table
from plotly.subplots import make_subplots

# standard package
import pandas as pd
import numpy as np
from numpy import sqrt


#date
from datetime import date
from datetime import datetime
from datetime import timedelta

#
import re
import os

# env mngt
from dotenv import load_dotenv 
load_dotenv()


# date & time package
import datetime
import math
from datetime import timedelta
#from datetime import datetime


##db package
#from sqlalchemy import create_engine
#import psycopg2

# local package
from app import app

today = datetime.date.today()
print("Today's date: ", today)


##get env db
#host=os.environ.get('HOST')
#user=os.environ.get('USER')
#database=os.environ.get('DATABASE')
#pwd=os.environ.get('PASSWORD')


#db_url = 'postgresql://'+user+':'+pwd+'@'+host+'/'+database 
#db_url = os.environ.get('URL')

## Create an engine instance
#alchemyEngine = create_engine(db_url)

## Connect to PostgreSQL server
#dbConnection = alchemyEngine.connect()
# Read data from PostgreSQL database table and load into a DataFrame instance
#df_etat_quittance  = pd.read_sql("SELECT * FROM etat_quittance", dbConnection)
##Close the database connection
#dbConnection.close()
#test
#print('table recouvrement',df_recouvrement.head(5))

##Hypthoses

endDate=date.today()
startDate = endDate - timedelta(days=365)
print(startDate)
datelist = pd.date_range(start = startDate, end=endDate, freq ='B').tolist()
datelist = pd.DataFrame(datelist)
size =  len(datelist)
print(size)

vol_2y = .30
vol_5y = .35
vol_10y = .40
vol_15y = .45
vol_30y = .50

#FRTR
df_fr = datelist.copy()
df_fr['BTNS 2y'] =  pd.DataFrame(np.random.randn(size) * sqrt(vol_2y) * sqrt(1 / 252.)).cumsum()
df_fr['BTNS 5y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_5y) * sqrt(1 / 252.)).cumsum()
df_fr['FRTR 10y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_10y) * sqrt(1 / 252.)).cumsum()
df_fr['FRTR 15y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_15y) * sqrt(1 / 252.)).cumsum()
df_fr['FRTR 30y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_30y) * sqrt(1 / 252.)).cumsum()
df_fr.set_index(0, inplace = True)

#Bund
df_ge = datelist.copy()
df_ge['BKO 2y'] =  pd.DataFrame(np.random.randn(size) * sqrt(vol_2y) * sqrt(1 / 252.)).cumsum()
df_ge['OBL 5y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_5y) * sqrt(1 / 252.)).cumsum()
df_ge['BUND 10y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_10y) * sqrt(1 / 252.)).cumsum()
df_ge['BUND 15y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_15y) * sqrt(1 / 252.)).cumsum()
df_ge['BUND 30y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_30y) * sqrt(1 / 252.)).cumsum()
df_ge.set_index(0, inplace = True)

#BTP
df_it = datelist.copy()
df_it['BTP 2y'] =  pd.DataFrame(np.random.randn(size) * sqrt(vol_2y) * sqrt(1 / 252.)).cumsum()
df_it['BTP 5y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_5y) * sqrt(1 / 252.)).cumsum()
df_it['BTP 10y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_10y) * sqrt(1 / 252.)).cumsum()
df_it['BTP 15y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_15y) * sqrt(1 / 252.)).cumsum()
df_it['BTP 30y'] = pd.DataFrame(np.random.randn(size) * sqrt(vol_30y) * sqrt(1 / 252.)).cumsum()
df_it.set_index(0, inplace = True)


ctry = ['FR','GE','IT']
ctry_bond = dict()
ctry_bond ['FR'] = df_fr.columns
ctry_bond ['GE'] = df_ge.columns
ctry_bond ['IT'] = df_it.columns

df_dic = dict()
df_dic ['FR'] = df_fr
df_dic ['GE'] = df_ge
df_dic ['IT'] = df_it


print(ctry_bond)


def trade_graph(df1,df2):

    fig1 = go.Figure()

    fig1.add_trace(go.Scatter(x=df1.index, y=df1,
                    mode='lines',
                    name='Sell'))
    
    fig1.add_trace(go.Scatter(x=df2.index, y=df2,
                mode='lines',
                name='Buy'))
    
    fig1.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="right",
            x=1
        )
    )
    fig1.update_layout(title_text='ASW level')
    fig1.update_layout(title_x=0.5)
    

    fig2 = go.Figure()
    df_spread = df2-df1
    fig2.add_trace(go.Scatter(x=df_spread.index, y=df_spread,
                mode='lines',
                name='spread'))
    fig2.update_layout(title_text='ASW spread')
    fig2.update_layout(title_x=0.5)
    

    dcc_graph1 = dcc.Graph(figure = fig1)
    dcc_graph2 = dcc.Graph(figure = fig2)


    res = dict()
    res ={
            'dcc_asw' : dcc_graph1,
            'dcc_spread': dcc_graph2,
    }

    return res

def box_graph(df1,df2, df3, df4):

    dfbox1 = df2-df1
    dfbox2 = df4-df3
    dfbox = dfbox1 + dfbox2

    fig1 = go.Figure()

    fig1.add_trace(go.Scatter(x=dfbox1.index, y=dfbox1,
                    mode='lines',
                    name='trade1'))
    
    fig1.add_trace(go.Scatter(x=dfbox2.index, y=dfbox2,
                mode='lines',
                name='trade2'))
    
    fig1.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="right",
            x=1
        )
    )
    fig1.update_layout(title_text='spread ASW')
    fig1.update_layout(title_x=0.5)
    

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=dfbox.index, y=dfbox,
                mode='lines',
                name='box trade'))
    fig2.update_layout(title_text='Box trade')
    fig2.update_layout(title_x=0.5)
    

    dcc_graph1 = dcc.Graph(figure = fig1)
    dcc_graph2 = dcc.Graph(figure = fig2)


    res = dict()
    res ={
            'dcc_spread' : dcc_graph1,
            'dcc_box': dcc_graph2,
    }

    return res



layout = dbc.Container(
    [
        #dbc.Col([
        #    dbc.Row(dbc.Col('Hypothèses', className='h4')),
        #    

        #]),    
        dbc.Col([
  
            dbc.Tabs(
            [
                dbc.Tab(label="RV", tab_id="rv_id"),
                dbc.Tab(label="ASW Curve", tab_id="aswCurve_id"),
                dbc.Tab(label="Carry Roll-Down", tab_id="c&r_id"),
                dbc.Tab(label="Issuance", tab_id="issuance_id"),
                dbc.Tab(label="Rating", tab_id="rating_id"),

            ],
            id="tabs",
            active_tab="RV",
            ),
            html.Br(),
            html.Div(id="tab-content")#, className="p-4"),
 
        ]),
        
    ],fluid=True
)


#callback tab
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab"),
)
def render_tab_content(active_tab):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab is not None:
        
        if active_tab == "rv_id":
            
            chld = [
                #html.P(),
                dbc.Row(
                    [
                        dbc.Col(['TRADE 1',
                            dbc.Col('Sell'),
                            dbc.Row([
                                dbc.Col ([
                                    dcc.Dropdown(
                                        id='dd-ctry-1s-id',
                                        options=[
                                            {'label': i, 'value': i} for i in ctry
                                        ],
                                        value='FR',
                                        clearable = False,
                                    ),
                                ],xs=12, sm=12, md=12, lg=3, xl=3),
                                
                                dbc.Col([
                                    dcc.Dropdown(
                                        id='dd-bond-1s-id',
                                        options=[
                                            {'label': i, 'value': i} for i in ctry_bond['FR']
                                        ],
                                        value=ctry_bond['FR'][0],
                                        clearable = False,
                                    )
                                ],xs=12, sm=12, md=12, lg=9, xl=9),
                            ]),
                            dbc.Col('Buy'),
                            dbc.Row([
                                dbc.Col ([
                                    dcc.Dropdown(
                                    id='dd-ctry-1b-id',
                                    options=[
                                        {'label': i, 'value': i} for i in ctry
                                    ],
                                    value='FR',
                                    clearable = False,
                                    ),
                                ],xs=12, sm=12, md=12, lg=3, xl=3),
                                dbc.Col([
                                    dcc.Dropdown(
                                    id='dd-bond-1b-id',
                                    options=[
                                        {'label': i, 'value': i} for i in ctry_bond['FR']
                                    ],
                                    value=ctry_bond['FR'][1],
                                    clearable = False,
                                    )
                                ],xs=12, sm=12, md=12, lg=9, xl=9),
                            ]),

                            #dbc.Col(trade_graph(df_fr['BTNS 2y'],df_ge['BKO 2y'])['dcc_asw']),
                            #dbc.Col(trade_graph(df_fr['BTNS 2y'],df_ge['BKO 2y'])['dcc_spread']),
                            dbc.Col(id="graph1-trade1-id"),
                            dbc.Col(id="graph2-trade1-id")




                        ],xs=12, sm=12, md=12, lg=4, xl=4),

                        dbc.Col(['TRADE 2',
                            dbc.Col('Sell'),
                            dbc.Row([
                                dbc.Col ([
                                    dcc.Dropdown(
                                        id='dd-ctry-2s-id',
                                        options=[
                                            {'label': i, 'value': i} for i in ctry
                                        ],
                                        value='GE',
                                        clearable = False,
                                    ),
                                ],xs=12, sm=12, md=12, lg=3, xl=3),
                                
                                dbc.Col([
                                    dcc.Dropdown(
                                        id='dd-bond-2s-id',
                                        options=[
                                            {'label': i, 'value': i} for i in ctry_bond['GE']
                                        ],
                                        value=ctry_bond['GE'][1],
                                        clearable = False,
                                    )
                                ],xs=12, sm=12, md=12, lg=9, xl=9),
                            ]),
                            dbc.Col('Buy'),
                            dbc.Row([
                                dbc.Col ([
                                    dcc.Dropdown(
                                    id='dd-ctry-2b-id',
                                    options=[
                                        {'label': i, 'value': i} for i in ctry
                                    ],
                                    value='GE',
                                    clearable = False,
                                    ),
                                ],xs=12, sm=12, md=12, lg=3, xl=3),
                                dbc.Col([
                                    dcc.Dropdown(
                                    id='dd-bond-2b-id',
                                    options=[
                                        {'label': i, 'value': i} for i in ctry_bond['GE']
                                    ],
                                    value=ctry_bond['GE'][0],
                                    clearable = False,
                                    )
                                ],xs=12, sm=12, md=12, lg=9, xl=9),
                            ]),

                            dbc.Col(id="graph1-trade2-id"),
                            dbc.Col(id="graph2-trade2-id")

                        ],xs=12, sm=12, md=12, lg=4, xl=4),

                        dbc.Col(['BOX TRADE',
                            dbc.Col('Trade 1'),
                            dbc.Col('-------'),
                            dbc.Col('+'),
                            dbc.Col('Trade 2'),
                            dbc.Col('-------'),
                            #dbc.Row('-'),

                            dbc.Col(id="graph1-box-id"),
                            dbc.Col(id="graph2-box-id")
                            

                        ],xs=12, sm=12, md=12, lg=4, xl=4),
               
                    ]
                )
            ]
            
            return  chld


        elif active_tab == "aswCurve_id":   
            chld =  [
                dbc.Row(dbc.Col('ASW Curve change Analysis', className='h4'))
            ]     
            return  chld
        
        elif active_tab == "c&r_id":   
            chld =  [
                dbc.Row(dbc.Col('Carry & Roll-Down Analysis', className='h4'))
            ]     
            return  chld
        
        elif active_tab == "issuance_id":   
            chld =  [
                dbc.Row(dbc.Col('Issuance Calendar', className='h4'))
            ]     
            return  chld
        
        elif active_tab == "rating_id":   
            chld =  [
                dbc.Row(dbc.Col('Rating Outlook', className='h4'))
            ]     
            return  chld
        
        
    return "Select a sheet"


#trade 1 - sell
@app.callback(  
    [   
        Output("dd-bond-1s-id", "options"),
       
    ],  
    [
        Input("dd-ctry-1s-id", "value"),
    ]
)
def dd_update(ctry):
    res=[
        {'label': i, 'value': i} for i in ctry_bond[ctry]
    ],
    return res

#trade 1 - buy
@app.callback(  
    [   
        Output("dd-bond-1b-id", "options"),
       
    ],  
    [
        Input("dd-ctry-1b-id", "value"),
    ]
)
def dd_update(ctry):
    res=[
        {'label': i, 'value': i} for i in ctry_bond[ctry]
    ],
    return res

#trade 2 - sell
@app.callback(  
    [   
        Output("dd-bond-2s-id", "options"),
       
    ],  
    [
        Input("dd-ctry-2s-id", "value"),
    ]
)
def dd_update(ctry):
    res=[
        {'label': i, 'value': i} for i in ctry_bond[ctry]
    ],
    return res

#trade 2 - buy
@app.callback(  
    [   
        Output("dd-bond-2b-id", "options"),
       
    ],  
    [
        Input("dd-ctry-2b-id", "value"),
    ]
)
def dd_update(ctry):
    res=[
        {'label': i, 'value': i} for i in ctry_bond[ctry]
    ],
    return res


#trade 1 - graph
@app.callback(  
    [   
        Output("graph1-trade1-id", "children"),
        Output("graph2-trade1-id", "children"),
        


       
    ],  
    [
        Input("dd-ctry-1s-id", "value"),
        Input("dd-bond-1s-id", "value"),
        Input("dd-ctry-1b-id", "value"),
        Input("dd-bond-1b-id", "value"),
    ]
)
def graphs_update(ctry1s, bond1s,ctry1b, bond1b):
    
    df1s= df_dic[ctry1s].copy()
    df1s = df1s[bond1s]
    df1b= df_dic[ctry1b].copy()
    df1b = df1b[bond1b]
    
    res1 = trade_graph(df1s,df1b)['dcc_asw']
    res2 = trade_graph(df1s,df1b)['dcc_spread']
  
    return res1, res2


#trade 2 - graph
@app.callback(  
    [   
        Output("graph1-trade2-id", "children"),
        Output("graph2-trade2-id", "children"),
               
    ],  
    [
        Input("dd-ctry-2s-id", "value"),
        Input("dd-bond-2s-id", "value"),
        Input("dd-ctry-2b-id", "value"),
        Input("dd-bond-2b-id", "value"),
    ]
)
def graphs_update(ctry2s, bond2s,ctry2b, bond2b):
    
    df2s= df_dic[ctry2s].copy()
    df2s = df2s[bond2s]
    df2b= df_dic[ctry2b].copy()
    df2b = df2b[bond2b]
    
    res1 = trade_graph(df2s,df2b)['dcc_asw']
    res2 = trade_graph(df2s,df2b)['dcc_spread']
  
    return res1, res2


#trade 2 - graph
@app.callback(  
    [   
        Output("graph1-box-id", "children"),
        Output("graph2-box-id", "children"),
               
    ],  
    [
        Input("dd-ctry-1s-id", "value"),
        Input("dd-bond-1s-id", "value"),
        Input("dd-ctry-1b-id", "value"),
        Input("dd-bond-1b-id", "value"),
        Input("dd-ctry-2s-id", "value"),
        Input("dd-bond-2s-id", "value"),
        Input("dd-ctry-2b-id", "value"),
        Input("dd-bond-2b-id", "value"),
    ]
)
def graphs_update(ctry1s, bond1s,ctry1b, bond1b,ctry2s, bond2s,ctry2b, bond2b):
    
    df1s= df_dic[ctry1s].copy()
    df1s = df1s[bond1s]
    df1b= df_dic[ctry1b].copy()
    df1b = df1b[bond1b]
    
    df2s= df_dic[ctry2s].copy()
    df2s = df2s[bond2s]
    df2b= df_dic[ctry2b].copy()
    df2b = df2b[bond2b]
    
    res1 = box_graph(df1s,df1b,df2s,df2b)['dcc_spread']
    res2 = box_graph(df1s,df1b,df2s,df2b)['dcc_box']
  
    return res1, res2