#!/usr/bin/env python
"""
Provides an interface that sorts employees by various
metrics
"""

class EmployeeSorter:
    """
    Sorts employees by name, salary, age

    Example:
        sorter = EmployeeSorter()
        sorter.sort(employees, 'age')
    """

    def sort(self, employees: dict[str, str | int], method: str) -> list[str | int]:
        # Sort by name
        if method == "name":
            return sorted(employees, key=lambda x: x['name'])
        if method == "age":
            return sorted(employees, key=lambda x: x['age'])
        if method == "salary":
            return sorted(employees, key=lambda x: x['salary'])

if __name__ == '__main__':
    employees = [
            {
                'name': 'Nick',
                'age': 29,
                'salary': 3500
            },
            {
                'name': 'Steve',
                'age': 30,
                'salary': 3000
            },
            {
                'name': 'Frank',
                'age': 32,
                'salary': 2500
            }
        ]
    sorter = EmployeeSorter()
    #  Sort by age
    print(sorter.sort(employees, 'age'))
    # Sort by name
    print(sorter.sort(employees, 'name'))
    # Sort by salary
    print(sorter.sort(employees, 'salary'))
