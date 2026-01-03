---
date: 2026-01-02 19:47:21
tags: FRED
category: Macroeconomic, Gdp
---

# Chart: GDP Over Time
Interactive line chart showing US Gross Domestic Product over time.

## Chart
```{raw} html
<iframe src="../_static/fred_charts/gdp_chart.html" height="500px" width="100%"></iframe>

<p style="text-align: center;">Sources: FRED</p>
```
[Full Screen Chart](../download_chart/fred_charts/gdp_chart.html)






**Description:** This chart plots US Gross Domestic Product (GDP) over time. GDP is the total monetary value of all goods and services produced within a country's borders in a specific time period and is a broad measure of overall economic activity.

**Relevance for Economic Analysis:** GDP is the primary indicator used to gauge the health of a country's economy. It represents the size and growth rate of the economy.

**Direction of Risk:** Declining GDP indicates economic contraction, which may signal recession risk. Sustained GDP growth indicates a healthy, expanding economy.

**Formulas Used:** N/A

**Data Cleaning Information:** Data is sourced directly from FRED without additional transformations.

**What does this add that other charts might not?** Provides a clear visualization of long-term economic growth trends in the United States.




## Chart Specs

| Chart Name             | GDP Over Time                                             |
|------------------------|------------------------------------------------------------|
| Chart ID               | gdp_chart                                               |
| Topic Tags             | Macroeconomic, Gdp                                |
| Data Series Start Date |                                  |
| Data Frequency         | Quarterly                                         |
| Observation Period     | Quarter                                     |
| Lag in Data Release    | One month                                    |
| Data Release Timing    | Quarterly                                    |
| Seasonal Adjustment    |                                     |
| Units                  | Billions of Dollars                                                  |
| HTML Chart             | [HTML](../download_chart/fred_charts/gdp_chart.html)    |


## Dataframe Manifest

| Dataframe Name                 | FRED Economic Data                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [fred](../dataframes/fred_charts/fred.md)                                       |
| Data Sources                   | FRED                                        |
| Data Providers                 | Federal Reserve Bank of St. Louis                                      |
| Links to Providers             | https://fred.stlouisfed.org/                             |
| Topic Tags                     | Macroeconomic, Gdp, Unemployment                                          |
| Type of Data Access            |                                   |
| How is data pulled?            | Web API via Python                                                    |
| Data available up to (min)     |                                                              |
| Data available up to (max)     |                                                              |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/backofficedev/chartbook_examples/fred_charts/_data/fred.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/fred_charts/fred.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/fred_charts/fred.xlsx)              |
| Linked Charts                  |   [fred_charts:gdp_chart](../../charts/fred_charts.gdp_chart.md)<br>  [fred_charts:unemployment_chart](../../charts/fred_charts.unemployment_chart.md)<br>   |

## Pipeline Manifest

| Pipeline Name                   | Example Charts from FRED                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [fred_charts](../pipelines/fred_charts_README.md)              |
| Lead Pipeline Developer         | backofficedev             |
| Contributors                    | backofficedev           |
| Git Repo URL                    |                         |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/backofficedev/chartbook_examples/fred_charts/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-02 19:47:21           |
| OS Compatibility                | Windows, Linux, macOS |
| Linked Dataframes               |  [fred_charts:fred](../dataframes/fred_charts/fred.md)<br>  |


**Build Commands:**
```
doit
```
