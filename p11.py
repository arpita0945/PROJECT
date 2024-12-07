import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
print("First Five Row Of Dataset")
print(tips.head())

#scatter plot
plt.figure(figure=(8,6))
sns.scatterplot(x='total_bill',y='tip',data=tips,hue='day',style='sex',palette='coolwarm')
plt.title("scatter plot of total bill vs tips")
plt.grid(True)
plt.show()

#box plot
plt.figure(figure=(8,6))
sns.countplot(x='day',y='total-bill',data=tips,palette='coolwarm')
plt.title("box plot of total bill by day")
plt.grid(True)
plt.show()

#count plot
plt.figure(figure=(8,6))
sns.countplot(x='smoker',data=tips,palette='coolwarm')
plt.title("count plot of smoker vs non-smoker")
plt.grid(True)
plt.show()

#pair plot
plt.figure(figure=(8,6))
sns.pairplot(data=tips,hue='sex',palette='coolwarm')
plt.show()