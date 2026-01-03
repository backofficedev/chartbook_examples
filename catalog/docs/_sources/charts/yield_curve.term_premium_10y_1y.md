---
date: 2026-01-01 12:27:11
tags: Federal Reserve Board
category: Yield Curve, Term Premium
---

# Chart: Term Premium (10Y-1Y)
10-year minus 1-year Treasury yield spread over time

## Chart
```{raw} html
<iframe src="../_static/yield_curve/term_premium_10y_1y.html" height="500px" width="100%"></iframe>

<p style="text-align: center;">Sources: Federal Reserve Board</p>
```
[Full Screen Chart](../download_chart/yield_curve/term_premium_10y_1y.html)






**Description:** These charts display term premium measures over time, calculated as the spread between the 10-year Treasury yield and shorter-term yields (1-year, 2-year, and 3-year). The term premium represents the additional compensation investors demand for holding longer-term bonds.

**Charts in this series:**
- **10Y-1Y Spread**: 10-year minus 1-year yield
- **10Y-2Y Spread**: 10-year minus 2-year yield
- **10Y-3Y Spread**: 10-year minus 3-year yield

**Relevance for Financial Stability:**
- Term premium is a key indicator of investor risk appetite and economic expectations
- An inverted yield curve (negative spread) has historically preceded recessions
- Changes in term premium affect borrowing costs across the economy

**Direction of Risk:**
- **Positive and rising**: Normal conditions, expectations of economic growth
- **Positive and falling**: Flattening curve, growing uncertainty
- **Near zero**: Very flat curve, elevated recession risk
- **Negative**: Inverted curve, historically associated with impending recessions

**Formulas Used:**
- 10Y-1Y Spread = SVENY10 - SVENY01
- 10Y-2Y Spread = SVENY10 - SVENY02
- 10Y-3Y Spread = SVENY10 - SVENY03

**Data Cleaning Information:** Data is sourced directly from the Federal Reserve yield curve dataset with no additional cleaning.

**What does this add?** Provides a long historical perspective on yield curve slope and term premium evolution, useful for understanding current market conditions in historical context.




## Chart Specs

| Chart Name             | Term Premium (10Y-1Y)                                             |
|------------------------|------------------------------------------------------------|
| Chart ID               | term_premium_10y_1y                                               |
| Topic Tags             | Yield Curve, Term Premium                                |
| Data Series Start Date |                                  |
| Data Frequency         | Daily                                         |
| Observation Period     | Weekday                                     |
| Lag in Data Release    | One day                                    |
| Data Release Timing    | Weekday                                    |
| Seasonal Adjustment    |                                     |
| Units                  | Percentage Points                                                  |
| HTML Chart             | [HTML](../download_chart/yield_curve/term_premium_10y_1y.html)    |


## Dataframe Manifest

| Dataframe Name                 | Term Premium                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [term_premium](../dataframes/yield_curve/term_premium.md)                                       |
| Data Sources                   | Federal Reserve Board                                        |
| Data Providers                 | Federal Reserve Board                                      |
| Links to Providers             | https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv                             |
| Topic Tags                     | Yield Curve, Term Premium                                          |
| Type of Data Access            |                                   |
| How is data pulled?            | Derived from Fed yield curve data                                                    |
| Data available up to (min)     |                                                              |
| Data available up to (max)     |                                                              |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/chartbase/examples/yield_curve/_data/term_premium.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/yield_curve/term_premium.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/yield_curve/term_premium.xlsx)              |
| Linked Charts                  |   [yield_curve:term_premium_10y_1y](../../charts/yield_curve.term_premium_10y_1y.md)<br>  [yield_curve:term_premium_10y_2y](../../charts/yield_curve.term_premium_10y_2y.md)<br>  [yield_curve:term_premium_10y_3y](../../charts/yield_curve.term_premium_10y_3y.md)<br>   |

## Pipeline Manifest

| Pipeline Name                   | Yield Curve                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [yield_curve](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    |                         |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/chartbase/examples/yield_curve/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-01 12:27:11           |
| OS Compatibility                |  |
| Linked Dataframes               |  [yield_curve:repo_public](../dataframes/yield_curve/repo_public.md)<br>  [yield_curve:fed_yield_curve](../dataframes/yield_curve/fed_yield_curve.md)<br>  [yield_curve:term_premium](../dataframes/yield_curve/term_premium.md)<br>  |

