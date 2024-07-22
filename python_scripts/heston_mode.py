import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def heston_call_price(S, K, T, r, kappa, theta, sigma, rho, v0):
    dt = T / 100
    prices = np.zeros(100)
    volatilities = np.zeros(100)
    volatilities[0] = v0
    
    for t in range(1, 100):
        dW1 = np.random.normal() * np.sqrt(dt)
        dW2 = rho * dW1 + np.sqrt(1 - rho**2) * np.random.normal() * np.sqrt(dt)
        volatilities[t] = max(0, volatilities[t-1] + kappa * (theta - volatilities[t-1]) * dt + sigma * np.sqrt(volatilities[t-1]) * dW2)
        prices[t] = prices[t-1] * np.exp((r - 0.5 * volatilities[t-1]) * dt + np.sqrt(volatilities[t-1]) * dW1)
    
    call_price = np.exp(-r * T) * max(0, np.mean(prices) - K)
    return call_price

# Parameters
S = 100
K = 100
T = 1
r = 0.05
kappa = 2.0
theta = 0.02
sigma = 0.3
rho = -0.5
v0 = 0.02

# Calculate Heston model call price
call_price = heston_call_price(S, K, T, r, kappa, theta, sigma, rho, v0)
print(f"Heston Model Call Option Price: {call_price}")
