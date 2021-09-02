import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = dbc.Container([
            html.Br(),
            dbc.Row([
                dbc.Col(" EUR markets (demo)", className="h1 text-center")
            ]),
            dbc.Row([
                dbc.Col("RV Tools - digital version v2.0", className="h2 text-center")
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        children=
                            [
                                #html.H3(children='Portefeuille',className="text-center"),
                                dbc.Button("EGB Analysis",
                                                    href="/egb",
                                                    color="primary",
                                                    #className="mt-3"
                                ),
                                
                        ],
                        body=True, 
                        color="dark", 
                        outline=True)
                ], xs=12, sm=6, md=6, lg=3, xl=3),
                dbc.Col([
                    dbc.Card(
                        dbc.Button("Curve Analysis",href="/curve",color="primary"),
                        body=True, 
                        color="dark", 
                        outline=True
                    )
                ],xs=12, sm=6, md=6, lg=3, xl=3),
                dbc.Col([
                    dbc.Card(
                        dbc.Button("Inflation Anlaysis",href="/inflation",color="primary"),
                        body=True, 
                        color="dark", 
                        outline=True
                    )
                ],xs=12, sm=6, md=6, lg=3, xl=3),
                dbc.Col([
                    dbc.Card(
                        dbc.Button("GSS Analysis",href="/gss",color="primary"),
                        body=True, 
                        color="dark", 
                        outline=True
                    )
                ],xs=12, sm=6, md=6, lg=3, xl=3),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.Button("Database management",color="info"),
                        body=True, 
                        color="dark", 
                        outline=True
                    )
                ],xs=12, sm=6, md=6, lg=3, xl=3),
                dbc.Col([
                    dbc.Card(
                        dbc.Button("...",color="info"),
                        body=True, 
                        color="dark", 
                        outline=True
                    )
                ],xs=12, sm=6, md=6, lg=3, xl=3),
                dbc.Col([
                    dbc.Card(
                        dbc.Button("...",color="info"),
                        body=True, 
                        color="dark", 
                        outline=True
                    )
                ],xs=12, sm=6, md=6, lg=3, xl=3),
                dbc.Col([
                    dbc.Card(
                        dbc.Button("...",color="info"),
                        body=True, 
                        color="dark", 
                        outline=True
                    )
                ],xs=12, sm=6, md=6, lg=3, xl=3),

            ]),

        
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),


            dbc.Row([
                dbc.Col(html.A(children='Copyright 2021 AR')
                        , className="mb-5 text-center")
            ]),
    
            

    ],fluid=True
)

