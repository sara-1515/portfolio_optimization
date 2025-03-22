import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_efficient_frontier(results, weights_record, returns):
    """Plot the efficient frontier with optimal portfolios."""
    # Convert results array to DataFrame
    columns = ['Return', 'Volatility', 'Sharpe']
    results_df = pd.DataFrame(results, columns=columns)
    
    # Filter out rows with NaN values
    valid_results = results_df.dropna()
    
    # If we have no valid results, raise an error
    if valid_results.empty:
        raise ValueError("No valid portfolios were generated. Please check your input data.")
    
    # Find portfolios with highest Sharpe ratio, lowest volatility, and highest return
    max_sharpe_idx = valid_results['Sharpe'].idxmax()
    min_vol_idx = valid_results['Volatility'].idxmin()
    max_ret_idx = valid_results['Return'].idxmax()
    
    # Get weights for these optimal portfolios
    max_sharpe_weights = weights_record[max_sharpe_idx]
    min_vol_weights = weights_record[min_vol_idx]
    max_ret_weights = weights_record[max_ret_idx]
    
    # Plot efficient frontier
    plt.figure(figsize=(12, 8))
    plt.scatter(valid_results['Volatility'], valid_results['Return'], 
                c=valid_results['Sharpe'], cmap='viridis', alpha=0.3)
    plt.colorbar(label='Sharpe Ratio')
    
    # Plot optimal portfolios
    plt.scatter(valid_results.loc[max_sharpe_idx, 'Volatility'], 
                valid_results.loc[max_sharpe_idx, 'Return'], 
                color='red', marker='*', s=200, label='Max Sharpe')
    plt.scatter(valid_results.loc[min_vol_idx, 'Volatility'], 
                valid_results.loc[min_vol_idx, 'Return'], 
                color='green', marker='*', s=200, label='Min Volatility')
    plt.scatter(valid_results.loc[max_ret_idx, 'Volatility'], 
                valid_results.loc[max_ret_idx, 'Return'], 
                color='blue', marker='*', s=200, label='Max Return')
    
    plt.title('Portfolio Optimization - Efficient Frontier')
    plt.xlabel('Volatility (Risk)')
    plt.ylabel('Expected Return')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Return optimal portfolio weights
    optimal_portfolios = {
        'max_sharpe': {ticker: weight for ticker, weight in zip(returns.columns, max_sharpe_weights)},
        'min_volatility': {ticker: weight for ticker, weight in zip(returns.columns, min_vol_weights)},
        'max_return': {ticker: weight for ticker, weight in zip(returns.columns, max_ret_weights)}
    }
    
    return optimal_portfolios, valid_results
# Add this to visualization.py
def display_allocation_tables(optimal_portfolios):
    """Display allocation tables for the optimal portfolios."""
    print("\nOptimal Portfolio Allocations:")
    
    print("\nMaximum Sharpe Ratio Portfolio:")
    max_sharpe_df = pd.DataFrame({'Allocation': optimal_portfolios['max_sharpe']}).sort_values(by='Allocation', ascending=False)
    max_sharpe_df['Allocation'] = max_sharpe_df['Allocation'] * 100  # Convert to percentage
    print(max_sharpe_df)
    
    print("\nMinimum Volatility Portfolio:")
    min_vol_df = pd.DataFrame({'Allocation': optimal_portfolios['min_volatility']}).sort_values(by='Allocation', ascending=False)
    min_vol_df['Allocation'] = min_vol_df['Allocation'] * 100  # Convert to percentage
    print(min_vol_df)
    
    print("\nMaximum Return Portfolio:")
    max_ret_df = pd.DataFrame({'Allocation': optimal_portfolios['max_return']}).sort_values(by='Allocation', ascending=False)
    max_ret_df['Allocation'] = max_ret_df['Allocation'] * 100  # Convert to percentage
    print(max_ret_df)