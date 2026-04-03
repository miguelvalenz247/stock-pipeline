# Stock Market Data Pipeline

An end-to-end data pipeline that ingests, transforms, and visualizes stock market data for JPM, MS, and PLTR.

## Tech Stack
- **Python & yfinance** — data ingestion
- **AWS S3** — cloud storage
- **Snowflake** — cloud data warehouse
- **dbt** — data transformation
- **Tableau** — visualization

## Dashboard
[View Live Tableau Dashboard](https://public.tableau.com/views/StockPriceAnalysis-JPMMSPLTR/Sheet2)

## Pipeline Architecture
yfinance → S3 → Snowflake → dbt → Tableau
