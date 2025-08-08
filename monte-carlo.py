import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
simulations = 100
sim_days = 5
data = (yf.download("SPLG",period="max",interval="1d",auto_adjust=False))

data["Returns"] = data["Adj Close"].pct_change()
last_price = float(data["Adj Close"].iloc[-1] )

simulations_df = np.zeros((sim_days,simulations)) 

sigma = data["Returns"].std() * 252
mu = data["Returns"].mean() * np.sqrt(252)
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
plt.xlabel("Days")
plt.ylabel("price")
plt.show()
