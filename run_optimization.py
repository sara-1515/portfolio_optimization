from data_handler import get_stock_data, calculate_returns, get_default_dates
from portfolio_optimizer import monte_carlo_optimization
from visualization import plot_efficient_frontier, display_allocation_tables
from config import DEFAULT_TICKERS, DEFAULT_NUM_PORTFOLIOS
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Portfolio Optimization Tool')
    parser.add_argument('--tickers', nargs='+', default=DEFAULT_TICKERS,
                        help='List of stock tickers to include in the portfolio')
    parser.add_argument('--num-portfolios', type=int, default=DEFAULT_NUM_PORTFOLIOS,
                        help='Number of portfolios to simulate')
    return parser.parse_args()

def run_portfolio_optimization(tickers, num_portfolios=10000):
    """Run the full portfolio optimization process."""
    try:
        # Get default dates
        start_date, end_date = get_default_dates()
            
        # Get stock data
        print(f"Downloading stock data for {tickers}...")
        prices = get_stock_data(tickers, start_date, end_date)
        
        if prices.empty:
            print("Error: No stock data was retrieved. Please check your ticker symbols.")
            return None, None
            
        # Calculate returns
        returns = calculate_returns(prices)
        
        if returns.empty:
            print("Error: Could not calculate returns from the price data.")
            return None, None
        
        # Run Monte Carlo simulation
        print(f"Optimizing portfolio with {num_portfolios} simulations...")
        results, weights_record = monte_carlo_optimization(returns, num_portfolios)
        
        # Plot efficient frontier and get optimal portfolios
        optimal_portfolios, results_df = plot_efficient_frontier(results, weights_record, returns)
        
        # Display allocation tables
        display_allocation_tables(optimal_portfolios)
        
        return optimal_portfolios, results_df
        
    except Exception as e:
        print(f"An error occurred during portfolio optimization: {e}")
        return None, None

if __name__ == "__main__":
    args = parse_arguments()
    try:
        optimal_portfolios, results = run_portfolio_optimization(args.tickers, args.num_portfolios)
        if optimal_portfolios is None:
            print("Portfolio optimization failed. Please try again with different parameters.")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)