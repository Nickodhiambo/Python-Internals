#!/usr/bin/env python
"""
Provides an inteface that sorts a list of employees by
various criteria
"""

def sort_by_name(employees):
    return sorted(employees, key=lambda x: x['name'])

def sort_by_age(employees):
    return sorted(employees, key=lambda x: x['age'])

def sort_by_salary(employees):
    return sorted(employees, key=lambda x: x['salary'])

class EmployeeSorter:
    """
    Sorts employees by a given strategy: name, age or salary
    """
    def sort(self, employees, strategy):
        return strategy(employees)

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
    print(sorter.sort(employees, sort_by_name))
    print(sorter.sort(employees, sort_by_age))
    print(sorter.sort(employees, sort_by_salary))

