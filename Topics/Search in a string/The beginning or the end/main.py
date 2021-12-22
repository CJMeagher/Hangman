text = input()

first_index = text.find("old")
last_index = text.rfind("old")
print(last_index if last_index > first_index else first_index)
