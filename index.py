
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from app import server

# import all pages in the app
from apps import home, egb, curve, inflation, gss

print('dash version: ', dash.__version__) 

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py

nav_item = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", href="/home", id="page-1-link")),
        dbc.NavItem(dbc.NavLink("EGB", href="/egb", id="page-2-link")),
        dbc.NavItem(dbc.NavLink("Curve", href="/curve", id="page-3-link")),
        dbc.NavItem(dbc.NavLink("Inflation", href="/inflation", id="page-4-link")),
        dbc.NavItem(dbc.NavLink("GSS", href="/gss", id="page-5-link")),

    ],
    fill= True,
)

navbar = dbc.Navbar(
    [
        html.A(
            ## Use row and col to control vertical alignment of logo / brand
            #dbc.Row(
            #    [
            #       dbc.Col(html.Img(src="/assets/nyhavana-logo.png", height="30px"), className="ml-2"),
            #    ],
            #    className="page-1-link",
            #    align="center",
            #    no_gutters=True,
            #),
            #href="/home",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Nav([nav_item], navbar=True, className="ml-2",)
    ],
    color="#F0F0F0",
    sticky = "top"
)


@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)

def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False,False,False
    return [pathname == f"/{i}" for i in ["home","egb", "curve","inflation","gss"]]


# embedding the navigation bar
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        navbar,

        dbc.Container(id="page-content", className="pt-1", fluid=True),
    ]
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
              
def display_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
    elif pathname == '/egb':
        return egb.layout
    elif pathname == '/curve':
        return curve.layout
    elif pathname == '/inflation':
        return inflation.layout
    elif pathname == '/gss':
        return gss.layout


    else:  
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-primary"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )

if __name__ == '__main__':
    #flask
    #app.run_server(debug=True)
    #app.run_server(host='0.0.0.0', debug=True, port=8050)
    app.run_server(host='0.0.0.0', debug=True)
   
 