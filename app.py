import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash_table
import dash_bootstrap_components as dbc
from sklearn.preprocessing import StandardScaler
import dash_pivottable
from data import data

df = pd.read_csv(r'Dataset.csv')
dfr = pd.read_csv(r"Dataset.csv")
country_options = [dict(label=country, value=country) for country in df['Country_Region'].unique()]
zz=['Total Population value','Available Manpower value','Aircraft Strength value', "Helicopter Fleet Strength value","Tank Strength value", "Navy Fleet Strengths value" ]
scaler = StandardScaler()
y=scaler.fit_transform(df[zz])
df_scaled = pd.DataFrame(y, columns=zz)
df_scaled = pd.concat([df_scaled, df["Country_Region"]], axis=1)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


dropdown_country = dcc.Dropdown(
    id='country1',
    options=country_options,
    multi=False,
    style={'height': '30px', 'width': '130px', "color":"black"}
)
dropdown_country2 = dcc.Dropdown(
    id='country2',
    options=country_options,
    multi=False,
    style={'height': '30px', 'width': '130px', "color":"black"}
)
def prepare_daily_report():


    return df
options=[]
x={}
for i in range(2,33):
    x={'label': dfr.columns[i], "value":dfr.columns[i]}
    options.append(x)
    x={}


app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

server = app.server
app.layout = html.Div([
    html.Table(
        [
            html.Tr([
                html.Th("Choose Two Countries to Compare"),
                html.Th(dropdown_country),
                html.Th(dropdown_country2),

            ]),

            html.Tr([
                html.Td("Military Strength Power Index:"),
                html.Td(id="c11"),
                html.Td(id="c21"),
            ]),
            html.Tr([
                html.Td("Defense Spending Budget Value In $:"),
                html.Td(id="c12"),
                html.Td(id="c22"),
            ]),
            html.Tr([
                html.Td("Total Population value:"),
                html.Td(id="c13"),
                html.Td(id="c23"),
            ]),
            html.Tr([
                html.Td("Available Manpower value:"),
                html.Td(id="c14"),
                html.Td(id="c24"),
            ]),
            html.Tr([
                html.Td("Attack Aircraft Strength value:"),
                html.Td(id="c15"),
                html.Td(id="c25"),
            ]),
            html.Tr([
                html.Td("Helicopter Fleet Strength value:"),
                html.Td(id="c16"),
                html.Td(id="c26"),
            ]),
            html.Tr([
                html.Td("Tank Strength value:"),
                html.Td(id="c17"),
                html.Td(id="c27"),
            ]),
            html.Tr([
                html.Td("Navy Fleet Strengths value:"),
                html.Td(id="c18"),
                html.Td(id="c28"),
            ]),
            html.Div([
            dcc.Graph(id='graph'),

            ]),

        ], className="customers"),

html.Div([html.Div([html.H1("Choropleth Map For the Variables")],
                   style={"margin-left":"830px", "padding-bottom": "30", "color":"white"}
                   ),
          html.Div([html.Span("Feature to display : ", className="six columns",
                              style={"text-align": "right", "width": "40%", "padding-top": 10, "color":"white"}),
                    dcc.Dropdown(id="value-selected", value='Military Strength Power Index',
                                 options=options,
                                 style={"display": "block", "margin-left": "auto", "margin-right": "auto",
                                        "width": "70%"},
                                 className="six columns")], className="row"),
          dcc.Graph(id="my-graph")
          ], className="zo"
         ),
html.Div([html.Div([html.H1("Pivot Table")],
                   style={"margin-left":"830px", "padding-bottom": "30", "color":"Black"}
                   ),
    dash_pivottable.PivotTable(
        id='table',
        data=data,
        cols=['Country Name'],
        colOrder="key_a_to_z",
        rows=['Total Population Value'],
        rowOrder="key_a_to_z",
        rendererName="Line Chart",
        aggregatorName="Maximum",
    ),
 ])
], className="Main")
#                                                Table And Radar
@app.callback(
    [
        Output("c21", "children"),
        Output("c22", "children"),
        Output("c23", "children"),
        Output("c24", "children"),
        Output("c25", "children"),
        Output("c26", "children"),
        Output("c27", "children"),
        Output("c28", "children"),
        Output("c11", "children"),
        Output("c12", "children"),
        Output("c13", "children"),
        Output("c14", "children"),
        Output("c15", "children"),
        Output("c16", "children"),
        Output("c17", "children"),
        Output("c18", "children"),
        Output("graph", "figure"),


    ],
    [
        Input("country2", "value"),
        Input("country1", "value"),
    ]
)
def thz(Country2, Country1):
    bo1 = df.loc[df['Country_Region'] == (Country1)].reset_index()
    bo2 = df.loc[df['Country_Region'] == (Country2)].reset_index()
    bo3 = df_scaled.loc[df_scaled['Country_Region'] == (Country1)].reset_index()
    bo4 = df_scaled.loc[df_scaled['Country_Region'] == (Country2)].reset_index()

    r = [bo3['Total Population value'].values[0], bo3['Available Manpower value'].values[0],
           bo3['Aircraft Strength value'].values[0], bo3["Helicopter Fleet Strength value"].values[0],
           bo3["Tank Strength value"].values[0], bo3["Navy Fleet Strengths value"].values[0]]

    ri = [bo4['Total Population value'].values[0], bo4['Available Manpower value'].values[0],
           bo4['Aircraft Strength value'].values[0], bo4["Helicopter Fleet Strength value"].values[0],
           bo4["Tank Strength value"].values[0], bo4["Navy Fleet Strengths value"].values[0]]

    theta = [df_scaled.columns[0], df_scaled.columns[1], df_scaled.columns[2], df_scaled.columns[3], df_scaled.columns[4], df_scaled.columns[5]]
    c211 = bo2["Military Strength Power Index"].values[0]
    c212 = bo2["defense spending budget value"].values[0]
    c213 = bo2["Total Population value"].values[0]
    c214 = bo2["Available Manpower value"].values[0]
    c215 = bo2['Attack Aircraft Strength value'].values[0]
    c216 = bo2["Helicopter Fleet Strength value"].values[0]
    c217 = bo2["Tank Strength value"].values[0]
    c218 = bo2["Navy Fleet Strengths value"].values[0]
    c111 = bo1["Military Strength Power Index"].values[0]
    c112 = bo1["defense spending budget value"].values[0]
    c113 = bo1["Total Population value"].values[0]
    c114 = bo1["Available Manpower value"].values[0]
    c115 = bo1['Attack Aircraft Strength value'].values[0]
    c116 = bo1["Helicopter Fleet Strength value"].values[0]
    c117 = bo1["Tank Strength value"].values[0]
    c118 = bo1["Navy Fleet Strengths value"].values[0]

    trace = go.Scatterpolar(r=r,
                            theta= theta,
                            fill = 'toself',
                            name = Country1)

    traces = go.Scatterpolar(r=ri,
                            theta= theta,
                            fill = 'toself',
                            name = Country2)




    return str(c211), \
        str(c212), \
        str(c213), \
        str(c214), \
        str(c215), \
        str(c216), \
                str(c217), \
                str(c218),\
                str(c111), \
                str(c112), \
                str(c113), \
                str(c114), \
                str(c115), \
                str(c116), \
                str(c117), \
                str(c118), \
                 {"data": [trace, traces],
                        "layout": go.Layout(polar=dict(
                            radialaxis=dict(
                                visible=True,
                            )))}
#                                                Choropleth Map
@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("value-selected", "value")]
)
def update_figure(selected):
    # dff = prepare_confirmed_data()

    dff = prepare_daily_report()
    dff['hover_text'] = dff["Country_Region"] + ": " + dff[selected].apply(str)

    trace = go.Choropleth(
                          locations=dff['CODE'], z=np.log(dff[selected]),
                          text=dff['hover_text'],
                          hoverinfo="text",
                          marker_line_color='white',
                          autocolorscale=False,
                          reversescale=True,
                          colorscale="RdBu", marker={'line': {'color': 'rgb(180,180,180)', 'width': 0.0}},
                          colorbar={"thickness": 10, "len": 0.3, "x": 0.9, "y": 0.7,
                              'title': {"side": "bottom"},
                              'tickvals': [2, 10],
                              'ticktext': ['100', '100,000']})
    return {"data": [trace],
            "layout": go.Layout(height=800, geo={'showframe': False, 'showcoastlines': False,
                                                 'projection': {'type': "miller"}, "bgcolor":'black'})}

#                                                Pivot Table
@app.callback(Output('output', 'children'),
              [Input('table', 'cols'),
               Input('table', 'rows'),
               Input('table', 'rowOrder'),
               Input('table', 'colOrder'),
               Input('table', 'aggregatorName'),
               Input('table', 'rendererName')])
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
    ]


if __name__ == '__main__':
    app.run_server(port=8090, debug=True)