from functools import reduce
employees = {
    "Ravi": 45000,
    "Anita": 72000,
    "Karthik": 52000,
    "Priya": 38000,
    "Suresh": 61000
}
updated = dict(map(lambda x: (x[0], int(x[1]*1.1)), employees.items()))
eligible = dict(filter(lambda x: x[1] >= 50000, updated.items()))
total = reduce(lambda a, b: a + b, updated.values())

print(updated)
print(eligible)
print("Total Salary:", total)

def deposit(bal, amt):
    return bal + amt

def withdraw(bal, amt):
    return bal - amt if amt <= bal else bal

acc_no = 1001
name = "Suresh"
balance = 25000

balance = deposit(balance, 5000)
balance = withdraw(balance, 3000)
print(acc_no, name, balance)
