import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

simulations = int(input("Enter number of simulations: "))
sim_days = int(input("Enter number of days you want to simulate: "))
ticker = input("Enter a ticker: ")
data = (yf.download(ticker,period="max",interval="1d",auto_adjust=False))

data["Returns"] = data["Adj Close"].pct_change()
last_price = float(data["Adj Close"].iloc[-1] )

simulations_df = np.zeros((sim_days,simulations)) 

sigma = data["Returns"].std() * np.sqrt(252)
mu = data["Returns"].mean() * 252
t = 1/252
for sim in range(simulations):
    price_list = [last_price]
    for day in range(sim_days):
        price_list.append(price_list[-1] * np.exp((mu - 0.5 * sigma**2) * t + sigma * np.random.normal() * np.sqrt(t)))
    simulations_df[:, sim] = price_list[1:]
final_prices = simulations_df[-1:]
median_final = np.median(final_prices)

print(f"The median final price is: {(np.median(final_prices)):.2f}")
print(f"The mean final price is: {(np.mean(final_prices)):.2f}")

plt.plot(simulations_df)
plt.title(f"Monte Carlo simulation for {ticker}")
plt.xlabel("Days-1")
plt.ylabel("Price")
plt.show()

#np.percentile(final_price, 5) #Shows 5th percentile, higher the better