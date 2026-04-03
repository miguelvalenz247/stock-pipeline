import pandas as pd
import yfinance as yf
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Define your 3 stocks
tickers = {
    'PLTR': '2020-09-30',  # Palantir IPO date
    'JPM':  '2019-01-01',  # JPMorgan
    'MS':   '2019-01-01',  # Morgan Stanley
}

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-1'
)

for ticker, start_date in tickers.items():
    print(f"Processing {ticker}...")
    
    # Pull data
    df = yf.download(ticker, 
                     start=start_date,
                     end='2023-02-03', 
                     progress=False)
    
    # Add metrics
    df['Daily_Return'] = df['Close'].pct_change()
    df['MA_30'] = df['Close'].rolling(window=30).mean()
    df['MA_7'] = df['Close'].rolling(window=7).mean()
    
    # Save CSV locally
    filename = f'{ticker.lower()}_stock_data.csv'
    df.to_csv(filename)
    print(f"✅ {ticker} CSV saved locally!")
    
    # Upload to S3
    s3.upload_file(filename, 'stockdatapltr', filename)
    print(f"✅ {ticker} uploaded to S3!")

print("🎉 All stocks processed!")
