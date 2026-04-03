SELECT
    ticker,
    DATE_TRUNC('month', date) as month,
    AVG(close) as avg_close,
    MAX(close) as max_close,
    MIN(close) as min_close,
    AVG(daily_return) as avg_daily_return,
    SUM(volume) as total_volume
FROM {{ ref('stg_stock_data') }}
GROUP BY ticker, DATE_TRUNC('month', date)
ORDER BY ticker, month
