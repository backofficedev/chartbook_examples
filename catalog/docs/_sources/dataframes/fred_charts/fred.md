# Dataframe: `fred_charts:fred` - FRED Economic Data


## Description

This dataframe contains basic economic time series from the Federal Reserve Economic Data (FRED) database, including GDP, Unemployment Rate, CPI, and Federal Funds Rate. These are fundamental macroeconomic indicators used to assess the overall health and direction of the US economy.


## Data Dictionary

- **date**: `datetime64[ns]` Observation date
- **GDP**: `float64` US Nominal Gross Domestic Product (Billions of Dollars)
- **UNRATE**: `float64` Unemployment Rate (Percent)
- **CPIAUCSL**: `float64` Consumer Price Index for All Urban Consumers: All Items (Index 1982-1984=100)
- **FEDFUNDS**: `float64` Effective Federal Funds Rate (Percent)




## DataFrame Glimpse

```
Rows: 947
Columns: 5
$ GDP               <f64> None
$ UNRATE            <f64> 4.6
$ CPIAUCSL          <f64> 325.031
$ FEDFUNDS          <f64> 3.88
$ DATE     <datetime[ns]> 2025-11-01 00:00:00


```

## Dataframe Manifest

| Dataframe Name                 | FRED Economic Data                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [fred](fred_charts/fred.md)                                       |
| Data Sources                   | FRED                                        |
| Data Providers                 | Federal Reserve Bank of St. Louis                                      |
| Links to Providers             | https://fred.stlouisfed.org/                             |
| Topic Tags                     | Macroeconomic, Gdp, Unemployment                                          |
| Type of Data Access            |                                   |
| How is data pulled?            | Web API via Python                                                    |
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
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

