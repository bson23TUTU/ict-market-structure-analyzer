import yfinance as yf
import pandas as pd

# CONFIGURATION
TICKER = "SPY"  # The asset to analyze
PERIOD = "1mo"  # Look back 1 month
INTERVAL = "1h" # 1-hour candles

def fetch_data(ticker):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period=PERIOD, interval=INTERVAL, progress=False)
    
    # Checks if yfinance gave us a complex "MultiIndex" table and simplifies it.
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    
    return data

def find_fair_value_gaps(data):
    #Scans for Bullish and Bearish Fair Value Gaps (FVG).

    fvg_list = []
    
    # Iterate through the candles (skipping the first 2 to have enough data)
    for i in range(2, len(data)):
        # Access rows using iloc to get the data at specific positions
        current_candle = data.iloc[i]
        prev_candle = data.iloc[i-1]
        prev_2_candle = data.iloc[i-2]

        # Convert values to simple floats to avoid "Ambiguous Series" errors
        c_high = float(current_candle['High'])
        c_low = float(current_candle['Low'])
        
        p2_high = float(prev_2_candle['High'])
        p2_low = float(prev_2_candle['Low'])

        # BEARISH FVG Logic:
        # Candle 1 Low > Candle 3 High (Bearish gap exists downwards)
        if p2_low > c_high:
            gap_size = p2_low - c_high
            timestamp = data.index[i]
            fvg_list.append({
                "Type": "Bearish FVG",
                "Time": str(timestamp),
                "Top_Range": p2_low,
                "Bottom_Range": c_high,
                "Gap_Size": round(gap_size, 2)
            })

        # BULLISH FVG Logic:
        # Candle 1 High < Candle 3 Low (Bullish FVG gap exists upwards)
        if p2_high < c_low:
            gap_size = c_low - p2_high
            timestamp = data.index[i]
            fvg_list.append({
                "Type": "Bullish FVG",
                "Time": str(timestamp),
                "Bottom_Range": p2_high,
                "Top_Range": c_low,
                "Gap_Size": round(gap_size, 2)
            })

    return fvg_list

def main():
    print("--- ICT Market Structure Analyzer (PoC) ---")
    
    # Get Data
    df = fetch_data(TICKER)
    
    if df.empty:
        print("No data found.")
        return

    # Analyze Structure
    gaps = find_fair_value_gaps(df)
    
    # Output Results
    print(f"\nAnalyzed {len(df)} candles for {TICKER}.")
    print(f"Found {len(gaps)} potential Fair Value Gaps.\n")
    
    # Print the last 5 gaps found
    for gap in gaps[-5:]: 
        print(f"[{gap['Time']}] {gap['Type']} | Range: {gap['Bottom_Range']:.2f} - {gap['Top_Range']:.2f}")

if __name__ == "__main__":
    main()