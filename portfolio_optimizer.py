import numpy as np
import pandas as pd

def calculate_portfolio_performance(weights, returns):
    """Calculate portfolio performance metrics with proper error handling."""
    try:
        # Expected portfolio return
        portfolio_return = np.sum(returns.mean() * weights) * 252  # Annualized
        
        # Portfolio volatility (risk)
        cov_matrix = returns.cov() * 252
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        
        # Sharpe ratio (assuming risk-free rate of 0% for simplicity)
        # Add a small number to avoid division by zero
        sharpe_ratio = portfolio_return / (portfolio_volatility + 1e-10)
        
        # Check for NaN or infinite values
        if (np.isnan(portfolio_return) or np.isnan(portfolio_volatility) or 
            np.isnan(sharpe_ratio) or np.isinf(sharpe_ratio)):
            return np.nan, np.nan, np.nan
            
        return portfolio_return, portfolio_volatility, sharpe_ratio
    
    except Exception as e:
        print(f"Error calculating portfolio performance: {e}")
        return np.nan, np.nan, np.nan

def monte_carlo_optimization(returns, num_portfolios=10000):
    """Generate random portfolios and find the optimal one."""
    results = np.zeros((num_portfolios, 3))  # Return, Volatility, Sharpe Ratio
    weights_record = []
    
    num_assets = len(returns.columns)
    
    # Check if we have enough data
    if returns.empty or num_assets < 2:
        raise ValueError("Not enough valid stock data for optimization. Need at least 2 stocks with valid returns.")
    
    for i in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights = weights / np.sum(weights)  # Normalize to sum to 1
        
        portfolio_return, portfolio_volatility, sharpe_ratio = calculate_portfolio_performance(weights, returns)
        
        results[i, 0] = portfolio_return
        results[i, 1] = portfolio_volatility
        results[i, 2] = sharpe_ratio
        
        weights_record.append(weights)
    
    # Check if we have valid results
    valid_results = ~np.isnan(results[:, 2])
    if not np.any(valid_results):
        raise ValueError("No valid portfolios could be generated. Please check your input data.")
    
    return results, weights_record