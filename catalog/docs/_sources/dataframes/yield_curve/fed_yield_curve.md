# Dataframe: `yield_curve:fed_yield_curve` - Fed Yield Curve


**Description:** Zero-coupon Treasury yield curve from the Federal Reserve based on the Gurkaynak, Sack, and Wright (2007) model.

**Data Source:** Federal Reserve Board

**URL:** https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv

**Date Range:** 1961-06-14 to present (updated daily)

**Columns:**

| Column | Description |
|--------|-------------|
| SVENY01 | 1-year zero-coupon yield (percent) |
| SVENY02 | 2-year zero-coupon yield (percent) |
| SVENY03 | 3-year zero-coupon yield (percent) |
| SVENY04 | 4-year zero-coupon yield (percent) |
| SVENY05 | 5-year zero-coupon yield (percent) |
| SVENY06 | 6-year zero-coupon yield (percent) |
| SVENY07 | 7-year zero-coupon yield (percent) |
| SVENY08 | 8-year zero-coupon yield (percent) |
| SVENY09 | 9-year zero-coupon yield (percent) |
| SVENY10 | 10-year zero-coupon yield (percent) |
| SVENY11 | 11-year zero-coupon yield (percent) |
| SVENY12 | 12-year zero-coupon yield (percent) |
| SVENY13 | 13-year zero-coupon yield (percent) |
| SVENY14 | 14-year zero-coupon yield (percent) |
| SVENY15 | 15-year zero-coupon yield (percent) |
| SVENY16 | 16-year zero-coupon yield (percent) |
| SVENY17 | 17-year zero-coupon yield (percent) |
| SVENY18 | 18-year zero-coupon yield (percent) |
| SVENY19 | 19-year zero-coupon yield (percent) |
| SVENY20 | 20-year zero-coupon yield (percent) |
| SVENY21 | 21-year zero-coupon yield (percent) |
| SVENY22 | 22-year zero-coupon yield (percent) |
| SVENY23 | 23-year zero-coupon yield (percent) |
| SVENY24 | 24-year zero-coupon yield (percent) |
| SVENY25 | 25-year zero-coupon yield (percent) |
| SVENY26 | 26-year zero-coupon yield (percent) |
| SVENY27 | 27-year zero-coupon yield (percent) |
| SVENY28 | 28-year zero-coupon yield (percent) |
| SVENY29 | 29-year zero-coupon yield (percent) |
| SVENY30 | 30-year zero-coupon yield (percent) |

**Reference:** Gurkaynak, Refet S., Brian Sack, and Jonathan H. Wright (2007). "The U.S. Treasury Yield Curve: 1961 to the Present." Journal of Monetary Economics, 54(8): 2291-2304.




## DataFrame Glimpse

```
Rows: 16838
Columns: 31
$ SVENY01          <f64> 3.5131
$ SVENY02          <f64> 3.4816
$ SVENY03          <f64> 3.5106
$ SVENY04          <f64> 3.5786
$ SVENY05          <f64> 3.6707
$ SVENY06          <f64> 3.7763
$ SVENY07          <f64> 3.8882
$ SVENY08          <f64> 4.0014
$ SVENY09          <f64> 4.1125
$ SVENY10          <f64> 4.2193
$ SVENY11          <f64> 4.3203
$ SVENY12          <f64> 4.4146
$ SVENY13          <f64> 4.5016
$ SVENY14          <f64> 4.5812
$ SVENY15          <f64> 4.6532
$ SVENY16          <f64> 4.718
$ SVENY17          <f64> 4.7755
$ SVENY18          <f64> 4.8262
$ SVENY19          <f64> 4.8703
$ SVENY20          <f64> 4.9082
$ SVENY21          <f64> 4.9401
$ SVENY22          <f64> 4.9665
$ SVENY23          <f64> 4.9877
$ SVENY24          <f64> 5.0041
$ SVENY25          <f64> 5.0159
$ SVENY26          <f64> 5.0234
$ SVENY27          <f64> 5.0271
$ SVENY28          <f64> 5.0271
$ SVENY29          <f64> 5.0238
$ SVENY30          <f64> 5.0174
$ Date    <datetime[ns]> 2025-12-26 00:00:00


```

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
| Data available up to (min)     | None                                                             |
| Data available up to (max)     | None                                                             |
| Dataframe Path                 | /Users/jbejarano/GitRepositories/chartbase/examples/yield_curve/_data/fed_yield_curve.parquet                                                   |
| Download Data as Parquet       | [Parquet](../../download_dataframe/yield_curve/fed_yield_curve.parquet)         |
| Download Data as Excel         | [Excel](../../download_dataframe/yield_curve/fed_yield_curve.xlsx)              |
| Linked Charts                  |   [yield_curve:yield_curve_current](../../charts/yield_curve.yield_curve_current.md)<br>   |

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


