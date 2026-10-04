
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Student data
data = {
    "Name": ["Arya", "Riya", "Sneha", "Priya", "Neha"],
    "Python": [85, 90, 78, 88, 92],
    "DBMS": [80, 85, 75, 90, 88],
    "Maths": [75, 80, 82, 78, 85],
    "English": [90, 88, 85, 92, 87]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total and percentage
subjects = ["Python", "DBMS", "Maths", "English"]

df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = df["Total"] / 4

# Display student records
print("STUDENT SUBJECT-WISE MARKS ANALYSIS")
print("-----------------------------------")
print(df.to_string(index=False))

# Statistical analysis
print("\nSubject-wise Average Marks:")
print(df[subjects].mean())

print("\nHighest Marks:")
print(df[subjects].max())

print("\nLowest Marks:")
print(df[subjects].min())

# Save data to Excel
df.to_excel("Student_Marks.xlsx", index=False)

print("\nExcel file saved successfully!")

# Bar Chart
average = df[subjects].mean()

plt.figure(figsize=(8, 5))
plt.bar(average.index, average.values)
plt.title("Subject-Wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.grid(axis="y")
plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
    average.values,
    labels=average.index,
    autopct="%1.1f%%"
)
plt.title("Subject-Wise Marks Distribution")
plt.show()
