import pandas as pd

# Step 1: Dummy Data
data = {
    'Name': ['Sonu', 'Mangal', 'Vishal', 'Abhishek', 'Kamlesh', 'Ravina', 'Khushi'],
    'Maths': [85, 40, 78, 55, 85, 90, 78],
    'Science': [90, 35, 82, 58, 78, 85, 76],
    'English': [88, 30, 80, 60, 89, 80, 74],
    'Attendance': [95, 60, 90, 75, 69, 75, 72],
    'Logins': [50, 10, 45, 20, 30, 20, 15]
}

# Step 2: Create and Save CSV File
df = pd.DataFrame(data)
df.to_csv("student_data.csv", index=False)
print("✅ student_data.csv file saved.")

# Step 3: Load CSV File
df = pd.read_csv("student_data.csv")
print("\n📄 Loaded Data:")
print(df)

# Step 4: Average Marks
df['Average_Marks'] = df[['Maths', 'Science', 'English']].mean(axis=1)
print("\n📊 Average Marks:")
print(df[['Name', 'Average_Marks']])

# Step 5: Top 3 Students
top_students = df.sort_values(by='Average_Marks', ascending=False).head(3)
print("\n🏆 Top 3 Students:")
print(top_students[['Name', 'Average_Marks']])

# Step 6: Weak Students
weak_students = df[df['Average_Marks'] < 40]
print("\n⚠️ Weak Students:")
print(weak_students[['Name', 'Average_Marks']])

# Step 7: Correlation
print("\n📈 Correlation Matrix:")
print(df.corr(numeric_only=True))

import matplotlib.pyplot as plt
import seaborn as sns

# 📊 1. Bar Chart: Har student ke average marks
plt.figure(figsize=(8,5))
sns.barplot(x='Name', y='Average_Marks', data=df)
plt.title("Student-wise Average Marks")
plt.ylabel("Average Marks")
plt.xlabel("Student Name")
plt.show()

# 🔥 2. Heatmap: Kis factor ka kya impact hai
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Attendance, Logins, Marks)")
plt.savefig("average_marks.png")
plt.savefig("correlation_headmap.png")
plt.show()