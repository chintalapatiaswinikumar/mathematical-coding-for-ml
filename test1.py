import numpy as np
import pandas as pd
import matplotlib.pyplot as pt

sample_data = np.array([1.6,2.0,2.6,3.0,3.5,
                        3.9,4.5,4.6,4.8,5.0,
                        5.1,5.3,5.4,5.6,5.8,
                        6.0,6.0,6.1,6.3,6.5,
                        6.5,6.7,7.0,7.1,7.3,
                        7.3,7.3,7.7,7.8,7.9,
                        8.0,8.1,8.3,8.4,8.4,
                        8.5,8.7,8.8,9.0,7.7])

print("count:",len(sample_data))
print("Mean:",sample_data.mean())
print("Minimum:",sample_data.min())
print("Maximum:",sample_data.max())
print("StDev:",np.std(sample_data))
print("Q1:",np.percentile(sample_data,25))
print("Q3:",np.percentile(sample_data,75))
print("IQR:",np.percentile(sample_data,75)-np.percentile(sample_data,25))
IQR = np.percentile(sample_data,75)-np.percentile(sample_data,25)
outlier1 = np.percentile(sample_data,25) - 1.5*IQR
outlier2 = np.percentile(sample_data,75) + 1.5*IQR

print("Outliers:",outlier1,outlier2)

df = pd.DataFrame(sample_data,columns=["time_before_failure"])
print(df)

pt.figure(figsize=(10,8))
pt.hist(df['time_before_failure'],bins=40)
pt.xlabel("time_before_failure")
pt.ylabel("frequency")
pt.savefig("images/test1 image")
