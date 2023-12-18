#X=BUTNARIU=>X%3==2
#Y=STEFAN-ROBERT=>Y/3=4
class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):

    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"D01_{department}"
        Manager.mgr_count += 1

    def display_employee(self):
        print("Department: ", self.department)


managers = []
for i in range(4):
    manager = Manager(f"Manager{i + 1}", 60000 + i * 1000, f"Team{i + 1}")
    managers.append(manager)

print("Manager objects:")
for manager in managers:
    manager.display_employee()

#Testam constructor/destructor __init__ din employee
print("\nEmployee objects:")
employee1 = Employee("Butnariu Robert", 2147483647)
employee1.display_employee()

print("\nEmployee emp_count:", employee1.empCount)
print("Manager mgr_count:", Manager.mgr_count)