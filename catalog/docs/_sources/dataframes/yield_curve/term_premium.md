# Dataframe: `yield_curve:term_premium` - Term Premium


**Description:** Term premium measures derived from the U.S. Treasury zero-coupon yield curve. The term premium represents the extra compensation investors require for holding longer-term bonds instead of rolling over short-term bonds.

**Data Source:** Derived from Federal Reserve Board yield curve data

**Columns:**

| Column | Description |
|--------|-------------|
| 10Y 1Y Spread | 10-year yield minus 1-year yield (percentage points) |
| 10Y 2Y Spread | 10-year yield minus 2-year yield (percentage points) |
| 10Y 3Y Spread | 10-year yield minus 3-year yield (percentage points) |

**Methodology:**

These are simple measures of the term premium calculated as yield spreads:

- **10Y-1Y Spread**: SVENY10 - SVENY01
- **10Y-2Y Spread**: SVENY10 - SVENY02
- **10Y-3Y Spread**: SVENY10 - SVENY03

**Interpretation:**

- **Positive spread**: Normal yield curve where long-term rates exceed short-term rates
- **Negative spread**: Inverted yield curve, often associated with recession expectations
- **Steepening**: Increasing spread, may indicate expectations of rising rates or inflation
- **Flattening**: Decreasing spread, may indicate expectations of falling rates or economic slowdown

**Note:** These simple spread measures differ from model-based term premium estimates (such as the Adrian-Crump-Moench model from the NY Fed) which attempt to decompose yields into expected short-term rates and a pure term premium component.




## DataFrame Glimpse

```
Rows: 16838
Columns: 4
$ 10Y 1Y Spread          <f64> 0.7061999999999995
$ 10Y 2Y Spread          <f64> 0.7376999999999998
$ 10Y 3Y Spread          <f64> 0.7086999999999994
$ date          <datetime[ns]> 2025-12-26 00:00:00


```

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
| Data available up to (min)     | 2025-12-26 00:00:00                                                             |
| Data available up to (max)     | 2025-12-26 00:00:00                                                             |
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


