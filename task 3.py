import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["ramya", "harini", "sakthi", "maran", "sura"],
    "Age": [24, 18, 22, 21, 23],
    "Department": ["CS", "IT", "CS", "ECE", "IT"],
    "Marks": [87, 72, 90, 65, 80]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMarks > 80:")
print(df[df["Marks"] > 80])

print("\nCS Department:")
print(df[df["Department"] == "CS"])

print("\nAge > 21:")
print(df[df["Age"] > 21])

print("\nIT Department with Marks > 75:")
print(df[(df["Department"] == "IT") & (df["Marks"] > 75)])

print("\nSelected students (Name and Marks):")
print(df.loc[df["Marks"] > 70, ["Name", "Marks"]])
