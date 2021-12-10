import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px


# external JavaScript files
external_scripts = [
    {
        'src': 'https://www.googletagmanager.com/gtag/js?id=G-ET46TBPVET',
    }
]


# app initialize
dash_app = dash.Dash(
    __name__,
    external_scripts=external_scripts,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],

)

app = dash_app.server
dash_app.config["suppress_callback_exceptions"] = True
dash_app.title = 'NYC Tobacco and Alcohol Licenses 2019'
dash_app._favicon = ('assets/favicon.ico')

# Load data

## JSON for NYC zip code boundaries
with open('assets/nyc-zip-code.geojson') as f:
	mapdata = json.load(f)


## Load statistics data for the zip codes
df = pd.read_csv("assets/combined_final.csv",
                   dtype={"zip": str, "percentage": float,
                          "tobacco": int, "alcohol": int,
                          "B02001_001E": int, "B02008_001E": int,
                          "B02009_001E": int, "B02010_001E": int,
                          "B02011_001E": int, "B02012_001E": int,
                          "B02013_001E": int, "B03001_002E": int,
                          "B03001_003E": int
                })


# Clean data
## Setup the classifications for tobacco and alcohol numbers
tobaccoLabels = ['A', 'B', "C"]
df['tobacco_classification'] = pd.qcut(df['tobacco'], 3, labels = tobaccoLabels)
alcoholLabels = ['1', '2', '3']
df['alcohol_classification'] = pd.qcut(df['alcohol'], 3, labels = alcoholLabels)
df['class'] = df['tobacco_classification'].astype(str) + df['alcohol_classification'].astype(str)

## Setup hover text
df['Information'] = 'Tobacco Licenses: ' + df['tobacco'].astype(str) + '<br>' + \
    'Alcohol Licenses: ' + df['alcohol'].astype(str) + '<br>' + \
    'Population: ' + df['B02001_001E'].astype(str) + '<br>' + \
    'Persons Below Poverty Line: ' + df['percentage'].astype(str) + '% <br>'

# Setup variables

## Colors
## A3: #be64ac B3: #8c62aa C3: #3b4994
## A2: #dfb0d6 B2: #a5add3 C2: #5698b9
## A1: #e8e8e8 B1: #ace4e4 C1: #5ac8c8
colormap = {
    'A1': '#e8e8e8', 'B1': '#ace4e4', 'C1': '#5ac8c8',
    'A2': '#dfb0d6', 'B2': '#a5add3', 'C2': '#5698b9',
    'A3': '#be64ac', 'B3': '#8c62aa', 'C3': '#3b4994'
}



## Zip codes
zipcodes = df['zip'].unique().tolist() 
zipcodes.sort()

selection = set()

# Functions
def build_banner():
   return html.Div(
      id="banner",
      className="banner",
      children=[
        html.Img(src=dash_app.get_asset_url("cunysps_2021_2linelogo_spsblue_1.png"), style={'height':'75%', 'width':'75%'}),
        html.H6("NYC Tobacco and Alcohol Licenses 2019"),
        ],
    )


def build_graph_title(title):
   return html.P(className="graph-title", children=title)

def draw_map():
    fig = px.choropleth_mapbox(df, geojson=mapdata, locations='zip', 
                           color="class", 
                           color_discrete_map=colormap, 
                           category_orders={"class": ['C3', 'B3', 'A3', 'C2', 'B2', 'A2', 'C1', 'B1', 'A1']},
                           featureidkey="properties.postalCode",
                           color_continuous_scale="Viridis",
                           range_color=(0, 75),
                           mapbox_style="carto-positron",
                           zoom=10, center = {"lat": 40.70229736498986, "lon": -74.01581689028704},
                           opacity=0.5,
                           labels={'zip':'Zipcode'},
                           hover_name=df['zip'],
                           hover_data=["Information"]
                          )


    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
        width=800,
        height=600
        )

    return fig




# Draw the choropleth map and store it
choropleth_map = draw_map()

dash_app.layout = html.Div(
  children=[
        html.Div(
        id="top-row",
        children=[
            html.Div(
               className="row",
               id="top-row-header",
               children=[
                  html.Div(
                     className="column",
                     id="header-container",
                     children=[
                         build_banner(),
                         html.P(
                            id="instructions",
                            children=[
                                "This Dash app utilizes data from ",
                                html.A(
                                    "NYC's Active Tobacco Retail Dealer Licenses",
                                    href='https://data.cityofnewyork.us/Business/Active-Tobacco-Retail-Dealer-Licenses/adw8-wvxb'
                                    ),
                                ", ",
                                html.A(
                                    "NYS's Liquor Authority Current List of Active Licenses",
                                    href='https://data.ny.gov/Economic-Development/Liquor-Authority-Current-List-of-Active-Licenses/hrvs-fxs2'
                                    ),
                                ", ",
                                html.A(
                                    "U.S Census Bureau's American Community Survey 5-Year Data (2009-2019)",
                                    href='https://www.census.gov/data/developers/data-sets/acs-5year.html'
                                    ),
                                ", and ",
                                html.A(
                                    "NYC's Zip Code Boundaries data",
                                    href='https://data.cityofnewyork.us/Business/Zip-Code-Boundaries/i8iw-xf4u'
                                    ),                                                      
                                ". This is designed to understand, if any, the confluence of poverty, demographics, tobacco and alcohol licenses.",
                                html.Br(),
                                html.Br(),
                                "This app is hosted on ",
                                html.A(
                                    "Azure's cloud platform (https://portal.azure.com)",
                                    href='https://portal.azure.com'
                                    ),
                                ". The Github for this application is here ",
                                html.A(
                                    "https://github.com/logicalschema/data608-final-project-sslee",
                                    href='https://github.com/logicalschema/data608-final-project-sslee'
                                    ),
                                ".",
                                html.Br(),
                                html.Br(),
                            ],
                         ),
                         html.Hr(className="divider"),
                         html.B("Color Key"),
                         html.Div(style={'display': 'flex', 'justify-content': 'space-between'},
                            children=[
                                html.P("Poor", style={'color':'red'}),
                                html.P("Fair", style={'color':'orange'}),
                                html.P("Good", style={'color':'green'})
                            ]
                            ),
                         html.Hr(className="divider"),
                         build_graph_title(html.B("Zip Code")),
                         dcc.Dropdown(
                           id="zip-dropdown",
                           options=[
                               {"label": i, "value": i} for i in zipcodes
                           ],
                           value=zipcodes[0],
                         ),
                   ]
                  ),
                  html.Div(
                     className="column",
                     id="top-row-graphs",
                     children=[

                          dcc.Loading(
                            html.Div(
                              id="map",
                              className="row",
                              children=[
                              # dcc Graph here
                                 dcc.Graph(figure=choropleth_map, id='map-graph')
                              ]

                            )
                          )
                     ]
                  ),
               ]
            ),
    html.Div(
      id="bottom-row",
      children=[
          html.Div(
              className="bottom-row",
              id="bottom-row-header",
              children=[
                  html.Div(
                     className="column",
                     id="form-bar-container",
                     children=[
                         build_graph_title("Zip Code Information"),
                         dcc.Graph(id='form-bar-graph'),
                     ]
                  ),
                  html.Div(
                     className="column",
                     id="form-text-container",
                     children=[
                         html.P(
                            id="lower-text-box"),
                     ],
                  ),
              ]
              )
      ]
      ),

          ]
    )



  ]
)

# Update dropdown
@dash_app.callback(
    Output("zip-dropdown", "value"),
    [Input("map-graph", "clickData")],
)
def update_zip_dropdown(clickData):
    if clickData is None:
        return "10001"
    else:
        location = clickData['points'][0]['location']
        selection.clear()
        selection.add(location)
        return list(selection)[0]


# Update bar plot
@dash_app.callback(
    Output("form-bar-graph", "figure"),
    [
        Input("zip-dropdown", "value")
    ],
)
def update_bar(zip_dropdown):
   temp = df[df['zip'] == zip_dropdown]
   fig = px.bar(
     temp,
     x = 'zip',
     y= ["B02008_001E", "B02009_001E", "B02010_001E", "B02011_001E", "B02012_001E", "B02013_001E", "B03001_002E", "B03001_003E"],
     title="Demographics for " + str(zip_dropdown),
     template='simple_white',
     log_y=True
    )

   fig.update_layout(barmode='group')

   return fig


# Running the server
if __name__ == "__main__":
    dash_app.run_server(debug=True)