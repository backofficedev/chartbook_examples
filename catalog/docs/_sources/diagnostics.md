# Diagnostics

This page provides metadata quality diagnostics for all pipelines, dataframes, and charts in the system.

## Download Report

[Download CSV Report](_static/diagnostics/chartbook_metadata_diagnostics.csv)

## Metadata Completeness Report

```{raw} html

<div style="overflow-x: auto; margin: 20px 0;">
<table border="1" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f0f0f0;">
      <th style="padding: 8px; text-align: left;">Name</th>
      <th style="padding: 8px; text-align: center;">Complete</th>
      <th style="padding: 8px; text-align: left;">Object Type</th>
      <th style="padding: 8px; text-align: left;">Identifier</th>
      <th style="padding: 8px; text-align: left;">Pipeline</th>
      <th style="padding: 8px; text-align: left;">Missing Fields</th>
      <th style="padding: 8px; text-align: left;">URL</th>
    </tr>
  </thead>
  <tbody>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Example Charts from FRED</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>fred_charts</code></a>

      </td>
      <td style="padding: 8px;"><code>fred_charts</code></td>
      <td style="padding: 8px; font-size: 0.9em;">git_repo_URL</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">FRED Economic Data</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/fred_charts/fred.html"><code>fred</code></a>

      </td>
      <td style="padding: 8px;"><code>fred_charts</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/fred_charts/fred.html">./dataframes/fred_charts/fred.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">GDP Over Time</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">chart</td>
      <td style="padding: 8px;">

        <a href="./charts/fred_charts.gdp_chart.html"><code>gdp_chart</code></a>

      </td>
      <td style="padding: 8px;"><code>fred_charts</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./charts/fred_charts.gdp_chart.html">./charts/fred_charts.gdp_chart.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Unemployment Rate Over Time</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">chart</td>
      <td style="padding: 8px;">

        <a href="./charts/fred_charts.unemployment_chart.html"><code>unemployment_chart</code></a>

      </td>
      <td style="padding: 8px;"><code>fred_charts</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./charts/fred_charts.unemployment_chart.html">./charts/fred_charts.unemployment_chart.html</a>

      </td>
    </tr>

    <tr style="background-color: #fff3cd;">
      <td style="padding: 8px;">Yield Curve</td>
      <td style="padding: 8px; text-align: center;">
❌
      </td>
      <td style="padding: 8px;">pipeline</td>
      <td style="padding: 8px;">

        <a href="./index.html"><code>yield_curve</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">build_commands, os_compatibility, git_repo_URL</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./index.html">./index.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Public Repo Data</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/yield_curve/repo_public.html"><code>repo_public</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/yield_curve/repo_public.html">./dataframes/yield_curve/repo_public.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Fed Yield Curve</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/yield_curve/fed_yield_curve.html"><code>fed_yield_curve</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/yield_curve/fed_yield_curve.html">./dataframes/yield_curve/fed_yield_curve.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Term Premium</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">dataframe</td>
      <td style="padding: 8px;">

        <a href="./dataframes/yield_curve/term_premium.html"><code>term_premium</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./dataframes/yield_curve/term_premium.html">./dataframes/yield_curve/term_premium.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Repo Rates</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">chart</td>
      <td style="padding: 8px;">

        <a href="./charts/yield_curve.repo_rates.html"><code>repo_rates</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./charts/yield_curve.repo_rates.html">./charts/yield_curve.repo_rates.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Current Yield Curve</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">chart</td>
      <td style="padding: 8px;">

        <a href="./charts/yield_curve.yield_curve_current.html"><code>yield_curve_current</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./charts/yield_curve.yield_curve_current.html">./charts/yield_curve.yield_curve_current.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Term Premium (10Y-1Y)</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">chart</td>
      <td style="padding: 8px;">

        <a href="./charts/yield_curve.term_premium_10y_1y.html"><code>term_premium_10y_1y</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./charts/yield_curve.term_premium_10y_1y.html">./charts/yield_curve.term_premium_10y_1y.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Term Premium (10Y-2Y)</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">chart</td>
      <td style="padding: 8px;">

        <a href="./charts/yield_curve.term_premium_10y_2y.html"><code>term_premium_10y_2y</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./charts/yield_curve.term_premium_10y_2y.html">./charts/yield_curve.term_premium_10y_2y.html</a>

      </td>
    </tr>

    <tr >
      <td style="padding: 8px;">Term Premium (10Y-3Y)</td>
      <td style="padding: 8px; text-align: center;">
✅
      </td>
      <td style="padding: 8px;">chart</td>
      <td style="padding: 8px;">

        <a href="./charts/yield_curve.term_premium_10y_3y.html"><code>term_premium_10y_3y</code></a>

      </td>
      <td style="padding: 8px;"><code>yield_curve</code></td>
      <td style="padding: 8px; font-size: 0.9em;">nan</td>
      <td style="padding: 8px; font-size: 0.9em;">

        <a href="./charts/yield_curve.term_premium_10y_3y.html">./charts/yield_curve.term_premium_10y_3y.html</a>

      </td>
    </tr>

  </tbody>
</table>
</div>

```

## What This Report Contains

- **Pipeline Diagnostics**: Checks for missing required fields in pipeline metadata
- **Dataframe Diagnostics**: Validates dataframe documentation completeness
- **Chart Diagnostics**: Ensures all charts have complete metadata

## Required Fields by Object Type

### Pipeline Fields (9 required)
- Pipeline name and description
- Lead developer and contributors
- Git repository URL
- Software modules/dependencies
- README file path

### Dataframe Fields (9 required)
- Data sources and providers
- Topic tags and data access info
- License information
- File paths (Parquet, Excel, docs)
- Date column specification

### Chart Fields (10 required)
- Chart name and description
- Legal clearance information
- Data characteristics (frequency, units, etc.)
- File paths for HTML and Excel outputs
- Associated dataframe reference

## How to Use This Report

1. **Identify Incomplete Metadata**: Rows highlighted in yellow indicate incomplete metadata
2. **Check Missing Fields**: Review the "Missing Fields" column for specific gaps
3. **Update Configuration**: Add missing fields to your pipeline's `chartbook.toml` file
4. **Verify Changes**: Rebuild the documentation to see updated diagnostics

## Summary Statistics


- **Total Objects**: 13
- **Complete**: 11 (84.6%)
- **Incomplete**: 2 (15.4%)
