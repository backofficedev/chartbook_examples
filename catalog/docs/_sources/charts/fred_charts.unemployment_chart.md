---
date: 2026-01-01 12:26:42
tags: FRED
category: Macroeconomic, Unemployment
---

# Chart: Unemployment Rate Over Time
Interactive line chart showing US Unemployment Rate over time.

## Chart
```{raw} html
<iframe src="../_static/fred_charts/unemployment_chart.html" height="500px" width="100%"></iframe>

<p style="text-align: center;">Sources: FRED</p>
```
[Full Screen Chart](../download_chart/fred_charts/unemployment_chart.html)






**Description:** This chart plots the US Unemployment Rate over time. The unemployment rate represents the percentage of the labor force that is jobless and actively seeking employment.

**Relevance for Economic Analysis:** The unemployment rate is a key indicator of labor market health and economic conditions. High unemployment indicates economic weakness, while low unemployment suggests a strong economy.

**Direction of Risk:** Rising unemployment indicates increasing economic stress and potential recession. Sustained high unemployment can lead to reduced consumer spending and slower economic growth.

**Formulas Used:** N/A

**Data Cleaning Information:** Data is sourced directly from FRED without additional transformations.

**What does this add that other charts might not?** Provides a clear visualization of labor market conditions and business cycle dynamics over time.




## Chart Specs

| Chart Name             | Unemployment Rate Over Time                                             |
|------------------------|------------------------------------------------------------|
| Chart ID               | unemployment_chart                                               |
| Topic Tags             | Macroeconomic, Unemployment                                |
| Data Series Start Date |                                  |
| Data Frequency         | Monthly                                         |
| Observation Period     | Month                                     |
| Lag in Data Release    | One week                                    |
| Data Release Timing    | Monthly                                    |
| Seasonal Adjustment    |                                     |
| Units                  | Percent                                                  |
| HTML Chart             | [HTML](../download_chart/fred_charts/unemployment_chart.html)    |


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
| Dataframe Path                 | /Users/jbejarano/GitRepositories/chartbase/examples/fred_charts/_data/fred.parquet                                                   |
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
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/chartbase/examples/fred_charts/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-01 12:26:42           |
| OS Compatibility                | Windows, Linux, macOS |
| Linked Dataframes               |  [fred_charts:fred](../dataframes/fred_charts/fred.md)<br>  |


**Build Commands:**
```
doit
```
