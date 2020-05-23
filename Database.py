from prettytable import PrettyTable
#pip install prettable
table=PrettyTable(["name","surname","age"])
table.add_row(["shivam","maniya",21])
table.add_row(["smit","mehta",21])
table.add_row(["abhi","kapopara",21])
table.add_row(["ankit","savaliya",21])
table.add_row(["hardik","singh",21])
print(table)