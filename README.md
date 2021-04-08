# RKI

Use Dashboard.xlsx to scrape the current estimates for the number of active coronavirus cases in Germany,
as well as the current estimates for the basic reproduction number R.
Source: https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Projekte_RKI/Nowcasting.html

![](\dashboard.png)

These estimates are scraped using Power Query, a forecast for  is calculated and then visualized within a dashboard:
  1. A line graph plots the developement of the basic reproduction number R over time. 
  2. A bar chart that plots the growth in case numbers for the Kent Variant within Germany over time.
  
Filters can be applied from within the Dashboard.

Alternatively you can use the Python script to get the relevant data. 
This might be easier because the RKI keeps changing their column names in unpredictable way. 
However, you'd need to rebuild the query and make sure that everything is being calculated accurately.

Note: This is a very simple proof of concept project and not a publication that meets scientific standards.
But it is accurate enough to get a feel for the trajectory of the pandemic and to communicate it to relatives and/or friends.
