import math
from scipy.stats import norm

# Cumulative normal distribution function
def cumulative_normal_distribution(x):
    return norm.cdf(x)

# Black-Scholes formula for call option
def black_scholes_call(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call_price = S * cumulative_normal_distribution(d1) - K * math.exp(-r * T) * cumulative_normal_distribution(d2)
    return call_price

# Black-Scholes formula for put option
def black_scholes_put(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    put_price = K * math.exp(-r * T) * cumulative_normal_distribution(-d2) - S * cumulative_normal_distribution(-d1)
    return put_price

# Parameters
S = 100     # Current stock price
K = 100     # Strike price
T = 30 / 365  # Time to expiry in years
r = 0.05    # Risk-free interest rate
sigma = 0.2  # Volatility (standard deviation)

# Calculate option prices
call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)

print(f"Call Option Price: {call_price}")
print(f"Put Option Price: {put_price}")
