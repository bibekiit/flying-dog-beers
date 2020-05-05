import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
countries=['India', 'China', 'USA', 'UK']
Susceptible=[40, 60, 85, 75]
Exposed=[40, 60, 85, 75]
Infected=[20, 55, 80, 70]
Recovered=[10, 20, 30, 40]
color1='darkgreen'
color2='lightblue'
color3='red'
color4='blue
mytitle='Covid Infections'
tabtitle='COVID!'
myheading='Covid 19 simulation'
label1='Susceptible'
label2='Exposed'
label3='Infected'
label4='Recovered'
githublink='https://github.com/bibekiit/flying-dog-beers'
sourceurl='https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6'

########### Set up the chart
susceptibility = go.Bar(
    x=countries,
    y=Susceptible,
    name=label1,
    marker={'color':color1}
)
exposition = go.Bar(
    x=countries,
    y=Exposed,
    name=label2,
    marker={'color':color2}
)
infection = go.Bar(
    x=countries,
    y=Infected,
    name=label3,
    marker={'color':color3}
)
recovery = go.Bar(
    x=countries,
    y=Recovered,
    name=label4,
    marker={'color':color4}
)


covid_data = [susceptibility,exposition, infection, recovery]
covid_layout = go.Layout(
    barmode='group',
    title = mytitle
)

covid_fig = go.Figure(data=covid_data, layout=covid_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=covid_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
