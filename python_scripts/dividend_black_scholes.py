import math
from scipy.stats import norm

# Cumulative normal distribution function
def cumulative_normal_distribution(x):
    return norm.cdf(x)

# Black-Scholes formula for call option with dividends
def black_scholes_call_div(S, K, T, r, sigma, q):
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call_price = S * math.exp(-q * T) * cumulative_normal_distribution(d1) - K * math.exp(-r * T) * cumulative_normal_distribution(d2)
    return call_price

# Black-Scholes formula for put option with dividends
def black_scholes_put_div(S, K, T, r, sigma, q):
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    put_price = K * math.exp(-r * T) * cumulative_normal_distribution(-d2) - S * math.exp(-q * T) * cumulative_normal_distribution(-d1)
    return put_price

# Parameters
S = 100     # Current stock price
K = 100     # Strike price
T = 30 / 365  # Time to expiry in years
r = 0.05    # Risk-free interest rate
sigma = 0.2  # Volatility (standard deviation)
q = 0.03    # Dividend yield

# Calculate option prices with dividends
call_price_div = black_scholes_call_div(S, K, T, r, sigma, q)
put_price_div = black_scholes_put_div(S, K, T, r, sigma, q)

print(f"Call Option Price with Dividends: {call_price_div}")
print(f"Put Option Price with Dividends: {put_price_div}")
