# Portfolio Optimization Tool

## Overview

This Portfolio Optimization Tool implements the Modern Portfolio Theory (Markowitz model) to find optimal asset allocations based on historical data. It helps investors determine how to distribute their investments across multiple assets to maximize returns for a given level of risk or minimize risk for a desired level of return.

## Features

- Downloads historical stock data automatically using Yahoo Finance
- Calculates thousands of potential portfolio allocations through Monte Carlo simulation
- Identifies optimal portfolios:
  - Maximum Sharpe Ratio (best risk-adjusted return)
  - Minimum Volatility (lowest risk)
  - Maximum Return (highest expected return)
- Visualizes the efficient frontier with color-coded portfolios
- Provides detailed allocation recommendations as percentages

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone this repository or download the source files
2. Install required dependencies:

```bash
pip install numpy pandas matplotlib yfinance
```

## File Structure

```
portfolio_optimization/
│
├── portfolio_optimizer.py       # Main module with optimization functions
├── data_handler.py              # Functions for fetching and processing stock data
├── visualization.py             # Plotting and visualization functions
├── utils.py                     # Utility functions and helpers
├── config.py                    # Configuration settings
└── run_optimization.py          # Script to execute the optimization
```

## Usage

### Basic Usage

Run the tool with default settings (AAPL, MSFT, GOOGL, AMZN, META stocks):

```bash
python run_optimization.py
```

### Custom Stock Selection

Specify your own list of stock tickers:

```bash
python run_optimization.py --tickers AAPL TSLA NFLX DIS NVDA
```

### Adjusting Simulation Parameters

Change the number of simulated portfolios:

```bash
python run_optimization.py --num-portfolios 20000
```

## Understanding the Results

### The Efficient Frontier Graph

The main output is the "Efficient Frontier" plot:

![Efficient Frontier Example](https://example.com/efficient_frontier.png)

- **Scatter Points**: Each dot represents a unique portfolio allocation
  - **X-axis**: Portfolio volatility (risk)
  - **Y-axis**: Expected annualized return
  - **Color**: Sharpe ratio (risk-adjusted return) - brighter/warmer colors indicate better risk-adjusted returns
  
- **Key Portfolios** (marked with stars):
  - **Red star**: Maximum Sharpe ratio portfolio
  - **Green star**: Minimum volatility portfolio
  - **Blue star**: Maximum return portfolio

### What the Colorful Dots Mean

Each colored dot on the scatter plot represents a different possible portfolio allocation. The tool generates thousands of these portfolios by randomly assigning different weights to each stock.

- **Position**: Shows the risk-return profile (volatility vs. expected return)
- **Color**: Indicates the Sharpe ratio (return per unit of risk)
  - Darker blue dots: Lower Sharpe ratios (less efficient portfolios)
  - Brighter/yellow dots: Higher Sharpe ratios (more efficient portfolios)

The "cloud" of dots shows all possible portfolios, while the curved upper boundary (the efficient frontier) shows the optimal portfolios.

### Allocation Tables

Below the graph, you'll see the recommended percentage allocations for each stock in the three optimal portfolios.

## Limitations

- Results are based on historical data and do not guarantee future performance
- The tool assumes normal distribution of returns and no transaction costs
- Default optimization uses random sampling rather than quadratic programming

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
