import matplotlib.pyplot as plt
import pandas as pd

#getting data
obama = pd.read_csv("obama.csv", parse_dates=["year_month"])



#getting data_mean of each month

data_mean = obama.groupby("year_month").mean()
print(data_mean)

#getting data_median of each month

data_median = obama.groupby("year_month").median()
# print(data_median)

# plotting

plt.plot(obama.year_month, obama.approve_percent, "o", markersize=3, alpha=0.4) #markersize for size of dot and alpha for opacity
plt.plot(data_mean.index, data_mean.approve_percent, "red")
plt.plot(data_median.index, data_median.approve_percent, "yellow")
plt.title("Obama's approval rating over the past years")
plt.xlabel("Years")
plt.ylabel("Approval rating")
plt.legend(["Approval rating", "Mean", "Median"])
plt.savefig("aggregated data.png")
plt.show()

data_25 = obama.groupby("year_month").quantile(0.25)
data_75 = obama.groupby("year_month").quantile(0.75)

plt.plot(data_75.index, data_75.approve_percent, "red")
plt.plot(data_median.index, data_median.approve_percent, "yellow")
plt.plot(data_25.index, data_25.approve_percent, "green")
plt.plot(obama.year_month, obama.approve_percent, "o", markersize=3, alpha=0.4) #markersize for size of dot and alpha for opacity
plt.legend(["75% data", "Median", "25% Data", "Approval rating"])
plt.show()