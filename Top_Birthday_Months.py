import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Birth Values" : [10, 20, 15, 25]

}

df = pd.DataFrame(data)

print(df)

plt.plot(df["Month"], df["Birth Values"])
plt.xticks(rotation=45)
plt.title("Births by Month")
plt.show()


