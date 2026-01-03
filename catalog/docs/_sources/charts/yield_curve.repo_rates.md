---
date: 2026-01-01 12:27:11
tags: FRED, Office of Financial Research
category: Short Term Funding, Repo
---

# Chart: Repo Rates
SOFR, the Effective Funds Rate, and the Fed's Target Range

## Chart
```{raw} html
<iframe src="../_static/yield_curve/repo_rates.html" height="500px" width="100%"></iframe>

<p style="text-align: center;">Sources: FRED, Office of Financial Research</p>
```
[Full Screen Chart](../download_chart/yield_curve/repo_rates.html)






**Description:** This chat plots repo rates over time. It uses the Secured Overnight Financing Rate (SOFR), a broad measure of the cost of borrowing cash overnight collateralized by Treasury securities via repurchase agreements, often exceeded the upper limit of the Federal Funds target range. Since SOFR does not extend back further than 2017, we use the average repo rate in the triparty repo market whenever SOFR is unavailable.

**Relevance for Financial Stability:** SOFR is a broad measure of the cost of borrowing cash overnight collateralized by Treasury securities via repurchase agreements, often exceeded the upper limit of the Federal Funds target range.

**Direction of Risk:** When repo rates exceed the fed funds target range, risk is higher. Higher relative repo rates are likely more risky that lower relative rates.

**Formulas Used:** N/A

**Data Cleaning Information:** N/A

**Relation to a chart in an OFR public monitor:** N/A

**What does this add that other charts might not?** It is helpful to visualize repo rates in the context of the fed fund's target range.





## Chart Specs

| Chart Name             | Repo Rates                                             |
|------------------------|------------------------------------------------------------|
| Chart ID               | repo_rates                                               |
| Topic Tags             | Short Term Funding, Repo                                |
| Data Series Start Date |                                  |
| Data Frequency         | Daily                                         |
| Observation Period     | Weekday                                     |
| Lag in Data Release    | One day                                    |
| Data Release Timing    | Weekday                                    |
| Seasonal Adjustment    |                                     |
| Units                  | Percent                                                  |
| HTML Chart             | [HTML](../download_chart/yield_curve/repo_rates.html)    |


## Dataframe Manifest

| Dataframe Name                 | Public Repo Data                                                   |
|--------------------------------|--------------------------------------------------------------------------------------|
| Dataframe ID                   | [repo_public](../dataframes/yield_curve/repo_public.md)                                       |
| Data Sources                   | FRED, Office of Financial Research                                        |
| Data Providers                 | FRED, Office of Financial Research                                      |
| Links to Providers             | https://fred.stlouisfed.org/, https://www.financialresearch.gov/short-term-funding-monitor/api/                             |
| Topic Tags                     | Short Term Funding, Repo                                          |
| Type of Data Access            |                                   |
| How is data pulled?            | Web API via Python                                                    |
| Data available up to (min)     |                                                              |
| Data available up to (max)     |                                                              |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/chartbase/examples/yield_curve/_data/repo_public.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/yield_curve/repo_public.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/yield_curve/repo_public.xlsx)              |
| Linked Charts                  |   [yield_curve:repo_rates](../../charts/yield_curve.repo_rates.md)<br>   |

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

