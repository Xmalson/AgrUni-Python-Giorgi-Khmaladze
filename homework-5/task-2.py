employees = [
    {"name": "Alice", "tasks": [5, 7, 9], "department": "IT"},
    {"name": "Bob", "tasks": [2, 3, 4], "department": "Sales"},
    {"name": "Charlie", "tasks": [8, 7, 6], "department": "IT"},
    {"name": "Diana", "tasks": [9, 8, 10], "department": "Marketing"},
    {"name": "George", "tasks": [2, 7, 6], "department": "IT"}
]

# task 1
average_list = list(map(lambda e: {
    "name": e["name"],
    "department": e["department"],
    "average_tasks": sum(e["tasks"]) / len(e["tasks"])
}, employees))

#task 2
sorted_average_list = sorted(average_list, key = lambda e: e["average_tasks"], reverse = True)

#task 3
top_employee = max(average_list, key = lambda e: e["average_tasks"])

#task 4
it_above_6 = list(filter(lambda e: e["department"] == "IT" and e["average_tasks"] > 6, average_list))

print("average list: ", average_list)
print("sored: ",sorted_average_list)
print("Top employee: ", top_employee)
print("IT above 6: ", it_above_6)