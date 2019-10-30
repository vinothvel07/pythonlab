import pandas as pd

user_usage = pd.read_csv("user_usage.csv")

user_device = pd.read_csv("user_device.csv")

result = pd.merge(user_usage[['use_id','outgoing_sms_per_month','monthly_mb']], user_device[['use_id', 'platform', 'device']], on='use_id')

result.to_csv("test.csv")

print(result.shape)