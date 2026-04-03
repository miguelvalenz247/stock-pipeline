SELECT
    date,
    ticker,
    open,
    high,
    low,
    close,
    volume,
    daily_return,
    ma_30,
    ma_7
FROM {{ source('stock_data', 'raw_stock_data') }}
WHERE close IS NOT NULL
