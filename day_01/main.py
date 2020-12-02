from day_01.data import expense_report

def findEntry(list):
    for entry in expense_report:
        for entry2 in expense_report:
            for entry3 in expense_report:
                if entry + entry2 + entry3 == 2020:
                    return (entry * entry2 * entry3)

print(findEntry(expense_report))