import pandas as pd
import matplotlib.pyplot as plt

# Read test and label files
test = pd.read_csv("psm_test.csv")
label = pd.read_csv("psm_test_label.csv")

test.isnull()

# Convert timestamp columns to datetime objects
test['timestamp'] = pd.to_datetime(test['timestamp_(min)'])

# Plot time series data with anomaly regions
plt.figure(figsize=(10, 6))
plt.plot(test['timestamp_(min)'], test['feature_0'], color='blue', label='Time Series Data')



plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Time Series Data with Anomaly Regions')
plt.legend()
plt.show()