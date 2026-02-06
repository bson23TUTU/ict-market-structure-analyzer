# TradeFlow: ICT Market Structure Analyzer

## Overview
**TradeFlow** is a Python-based algorithmic trading tool designed to identify "Inner Circle Trader" (ICT) market structure concepts programmatically. 

This Proof of Concept focuses on detecting **Fair Value Gaps (FVG)** a key signature of institutional order flow using historical price data from the Yahoo Finance API. Different ICT concepts other than FVG will be implemented in the future.

## Features
- **Automated Data Fetching:** Retrieves hourly candle data for any ticker (default: SPY).
- **Algorithmic Pattern Recognition:** Scans for:
  - **Bearish FVGs:** (Candle 1 Low > Candle 3 High)
  - **Bullish FVGs:** (Candle 1 High < Candle 3 Low)
- **Console Reporting:** Outputs a list of detected inefficiencies with precise timestamps and price ranges.

## Installation

1. Clone the repository:

    git clone https://github.com/YOUR_USERNAME/ict-market-structure-analyzer.git

2. Install dependencies:

    pip install -r requirements.txt

## Usage

Run the main script to analyze the S&P 500 (SPY) for the last month:

    python main.py

## Future Roadmap
- Integration with live broker APIs for real-time alerts.
- Detection of strong DOL (Draws on liquidity) such as Swing highs/lows, NWOG (New week opening gap), session highs/lows, etc.
- Detection of strong displacement candles for entry models


## Course Information
**CIS 3296: Software Design**  
Spring 2026  
*Proof of Concept Submission*