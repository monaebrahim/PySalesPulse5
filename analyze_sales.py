import pandas as pd
import matplotlib.pyplot as plt

# قراءة البيانات من ملف CSV
df = pd.read_csv("sales_data.csv")

# تحليل البيانات
print("ملخص البيانات:\n", df.describe())

# رسم البيانات
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Sales"], marker="o", linestyle="-", color="b", label="Sales")
plt.xlabel("Date")
plt.ylabel("Sales Amount")
plt.title("Sales Data Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
