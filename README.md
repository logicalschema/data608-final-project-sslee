# Data 608 Final Project Dash Application


## Assignment
The final project is to create a public visualization using data relevant to current policy, business, or justice issue. Originally, I wanted to see if there is a correlation between the average income for the district of a borough and the number of tobacco and liquor selling businesses in the same district. It was advised to find a common geographic connection between the data sets and the one that was common was the zip code. Thus, I gathered the number of active licenses for alcohol and tobacco by zip code along with census estimated data. The most recent year that was available for all of the data sets was 2019. 

The visualization looks at NYC zip codes and constructs a bivariate choropleth map using the number of active tobacco and alcohol establishment licneses for 2019. Along with the map, the population, demographic, and percentage below the poverty line are listed for each zip code.

The data sets I used are from the following sources:

* [NYS Liquor Active Licenses](https://data.ny.gov/Economic-Development/Liquor-Authority-Current-List-of-Active-Licenses/hrvs-fxs2)
* [NYC Tobacco Active Licenses](https://data.cityofnewyork.us/Business/Active-Tobacco-Retail-Dealer-Licenses/adw8-wvxb)
* [U.S Census Information](https://www.census.gov/quickfacts/newyorkcitynewyork)
* [NYC Map Boundaries for Zip Codes](https://www1.nyc.gov/site/planning/data-maps/open-data/districts-download-metadata.page)

The data was gathered and cleaned. I was specifically grabbing information for 2019. The data for NYS was conveniently organized by county. For NYC, the 5 boroughs are listed as Bronx County, Queens County, Richmond County (Staten Island), Kings County (Brooklyn), and New York County (Manhattan). 

NYC's data had two notable errors in zip codes: "014" and "694". For this data, I mapped the business addresses and obtained the correct zip codes. 

The Census data was massive and took me a few days to wade through. I also looked at Census Reporter's information to better understand the data.

## Getting Started

The Dash app is hosted at [https://data608-final-project-sslee.azurewebsites.net/](https://data608-final-project-sslee.azurewebsites.net/). You can go here to access the app. 

Click on the zip code and the bar chart and demographic information will populate for that zip code.

### Dependencies

* Python
* Dash
* Plotly
* Venv
* Pip
* Platform to host: Azure was used as a cloud platform service, but Heroku or others can be used.

### Installing

* [GitHub repository](https://github.com/logicalschema/data608-final-project-sslee)

No installation is needed. You only need an active internet connection and a web browser.

### Executing program

* [https://data608-final-project-sslee.azurewebsites.net/](https://data608-final-project-sslee.azurewebsites.net/)

## Authors

Sung Lee 
[@logicalschema](https://twitter.com/logicalschema)

## Version History
* 1.0
    * Editing README, cleaning files, and fixing typos

* 0.9 
    * Committed to Azure
    * Launch

* 0.7-0.8
    * Added the bar plot and textboxes for the Dash app
    * Connected them to the clickData for the map 

* 0.6
    * Added dropdown menu for zip codes and tied the click from the map to update the dropdown menu

* 0.5
    * Created initial Dash app
    * Added choropleth map

* 0.4
    * Compiled data from Census 2019 with censusreporter.org's unemployment information using censusdata
    * censusreporter was able to traverse the census data

* 0.3
    * Identified problematic errors in NYC and NYS data with incorrect zip codes (some had only 3 digits)
    * Cleaned "014" or "694" erroneous zip codes
    * Some zip codes were for PO Boxes
* 0.2
    * Cleaned data
* 0.1
    * Development

## License

This project is licensed under the [mit] License - see the LICENSE file for details

## Acknowledgments

Code snippets and tutorials:
* [Deploy on Azure](https://resonance-analytics.com/blog/deploying-dash-apps-on-azure)
* [Handy for External js files on Dash](https://dash.plotly.com/external-resources)
* [Github for a Dash App with Components](https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-oil-gas-ternary)

