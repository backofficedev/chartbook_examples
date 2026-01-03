---
date: 2026-01-02 20:12:44
tags: Federal Reserve Board
category: Yield Curve, Treasury
---

# Chart: Current Yield Curve
Most recent U.S. Treasury zero-coupon yield curve

## Chart
```{raw} html
<iframe src="../_static/yield_curve/yield_curve_current.html" height="500px" width="100%"></iframe>

<p style="text-align: center;">Sources: Federal Reserve Board</p>
```
[Full Screen Chart](../download_chart/yield_curve/yield_curve_current.html)






**Description:** This chart displays the most recent U.S. Treasury zero-coupon yield curve, showing yields across maturities from 1 to 30 years. The yields are derived from the Gurkaynak, Sack, and Wright (2007) model published by the Federal Reserve.

**Relevance for Financial Analysis:** The yield curve is a fundamental indicator for:
- Monetary policy expectations
- Economic growth outlook
- Fixed income valuation
- Interest rate risk management

**Direction of Risk:**
- **Normal curve (upward sloping)**: Positive outlook for economic growth
- **Flat curve**: Uncertainty about economic direction
- **Inverted curve (downward sloping)**: Often precedes economic recessions

**Formulas Used:** N/A (direct visualization of yield curve data)

**Data Cleaning Information:** The chart shows the most recent available observation from the Fed's yield curve dataset.

**What does this add?** Provides a snapshot of the current term structure of interest rates across all available maturities.




## Chart Specs

| Chart Name             | Current Yield Curve                                             |
|------------------------|------------------------------------------------------------|
| Chart ID               | yield_curve_current                                               |
| Topic Tags             | Yield Curve, Treasury                                |
| Data Series Start Date |                                  |
| Data Frequency         | Daily                                         |
| Observation Period     | Weekday                                     |
| Lag in Data Release    | One day                                    |
| Data Release Timing    | Weekday                                    |
| Seasonal Adjustment    |                                     |
| Units                  | Percent                                                  |
| HTML Chart             | [HTML](../download_chart/yield_curve/yield_curve_current.html)    |


## Dataframe Manifest

| Dataframe Name                 | Fed Yield Curve                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [fed_yield_curve](../dataframes/yield_curve/fed_yield_curve.md)                                       |
| Data Sources                   | Federal Reserve Board                                        |
| Data Providers                 | Federal Reserve Board                                      |
| Links to Providers             | https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv                             |
| Topic Tags                     | Yield Curve, Treasury                                          |
| Type of Data Access            |                                   |
| How is data pulled?            | Web API via Python                                                    |
| Data available up to (min)     |                                                              |
| Data available up to (max)     |                                                              |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/backofficedev/chartbook_examples/yield_curve/_data/fed_yield_curve.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/yield_curve/fed_yield_curve.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/yield_curve/fed_yield_curve.xlsx)              |
| Linked Charts                  |   [yield_curve:yield_curve_current](../../charts/yield_curve.yield_curve_current.md)<br>   |

## Pipeline Manifest

| Pipeline Name                   | Yield Curve Analysis                       |
|---------------------------------|--------------------------------------------------------|
| Pipeline ID                     | [yield_curve](../index.md)              |
| Lead Pipeline Developer         | Jeremy Bejarano             |
| Contributors                    | Jeremy Bejarano           |
| Git Repo URL                    |                         |
| Pipeline Web Page               | <a href="file:///Users/jbejarano/GitRepositories/backofficedev/chartbook_examples/yield_curve/docs/index.html">Pipeline Web Page      |
| Date of Last Code Update        | 2026-01-02 20:12:44           |
| OS Compatibility                |  |
| Linked Dataframes               |  [yield_curve:repo_public](../dataframes/yield_curve/repo_public.md)<br>  [yield_curve:fed_yield_curve](../dataframes/yield_curve/fed_yield_curve.md)<br>  [yield_curve:term_premium](../dataframes/yield_curve/term_premium.md)<br>  |

