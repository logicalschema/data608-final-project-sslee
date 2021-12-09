import json
import dash

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


# https://data.cityofnewyork.us/Business/Zip-Code-Boundaries/i8iw-xf4u
# https://plotly.com/python/choropleth-maps/
# https://api.census.gov/data/2019/acs/acs5/variables.html
# https://www.joshuastevens.net/cartography/make-a-bivariate-choropleth-map/

# B02001_001E TOTAL Population 
# B02008_001E WHITE ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
# B02009_001E BLACK OR AFRICAN AMERICAN ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
# B02010_001E AMERICAN INDIAN AND ALASKA NATIVE ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
# B02011_001E ASIAN ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
# B02012_001E NATIVE HAWAIIAN AND OTHER PACIFIC ISLANDER ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
# B02013_001E SOME OTHER RACE ALONE OR IN COMBINATION WITH ONE OR MORE OTHER RACES
# B03001_002E Not HISPANIC OR LATINO ORIGIN BY SPECIFIC ORIGIN
# B03001_003E HISPANIC OR LATINO ORIGIN BY SPECIFIC ORIGIN

# Classes and color
# A3: #be64ac B3: #8c62aa C3: #3b4994
# A2: #dfb0d6 B2: #a5add3 C2: #5698b9
# A1: #e8e8e8 B1: #ace4e4 C1: #5ac8c8

colormap = {
    'A1': '#e8e8e8', 'B1': '#ace4e4', 'C1': '#5ac8c8',
    'A2': '#dfb0d6', 'B2': '#a5add3', 'C2': '#5698b9',
    'A3': '#be64ac', 'B3': '#8c62aa', 'C3': '#3b4994'
}

## JSON for NYC zip code boundaries
with open('assets/nyc-zip-code.geojson') as f:
       mapdata = json.load(f)

df = pd.read_csv("assets/combined_final.csv",
                   dtype={"zip": str, "percentage": float,
                          "tobacco": int, "alcohol": int,
                          "B02001_001E": int, "B02008_001E": int,
                          "B02009_001E": int, "B02010_001E": int,
                          "B02011_001E": int, "B02012_001E": int,
                          "B02013_001E": int, "B03001_002E": int,
                          "B03001_003E": int
                })


# Setup the classifications for tobacco and alcohol numbers
tobaccoLabels = ['A', 'B', "C"]
df['tobacco_classification'] = pd.qcut(df['tobacco'], 3, labels = tobaccoLabels)
alcoholLabels = ['1', '2', '3']
df['alcohol_classification'] = pd.qcut(df['alcohol'], 3, labels = alcoholLabels)
df['class'] = df['tobacco_classification'].astype(str) + df['alcohol_classification'].astype(str)


# Setup hover text
df['Information'] = 'Tobacco Licenses: ' + df['tobacco'].astype(str) + '<br>' + \
    'Alcohol Licenses: ' + df['alcohol'].astype(str) + '<br>' + \
    'Population: ' + df['B02001_001E'].astype(str) + '<br>' + \
    'Persons Below Poverty Line: ' + df['percentage'].astype(str) + '% <br>'



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
              height=800
              )

# fig.show()
print(district_lookup)
