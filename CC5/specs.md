# Optimal Assignment Problem

A company has a set of N employees to be assigned to N different projects. Each employee has ranked their preferences for which projects they wish to join, and each project has ranked their preferences for which employees they prefer.

Given these preferences, assign 1 employee to each project. These assignments should be *optimal*, meaning that there is no unmatched pair of an employee and a project such that both that employee and that project would prefer they be matched with each other.

In the case there are multiple valid optimal matchings, the solution that is most favorable for the employees should be chosen (i.e. every employee should be matched with the best project possible for them).

## Function Signature

Your function should take in 2 2-dimensional lists, one for employees and one for projects. Each inner list represents a single employee or project’s preferences, ranked from most preferable to least preferable. These lists will always be of length N, with integers as elements. Each of these integers corresponds to the index of the project/employee being ranked. Your function should return a 2-dimensional list of matchings in no particular order. Each matching should be in the format `[EmployeeIndex, ProjectIndex]`.


## Function Signature

```python
def stable_assignments(employees: list[list[int]], projects: list[list[int]]) -> list[list[int]]:
    pass
```

- **Parameters:**  
  `employees`: A 2D list where each sublist represents an employee’s ranked preferences for projects (most to least preferred).  
  `projects`: A 2D list where each sublist represents a project’s ranked preferences for employees (most to least preferred).

- **Returns:**  
  A list of matchings, where each matching is in the format `[EmployeeIndex, ProjectIndex]`.

---

## Example 1

**Input:**

```python
employees = [
  [0, 1, 2],
  [1, 0, 2],
  [1, 2, 0]
]

projects = [
  [2, 1, 0],
  [1, 2, 0],
  [0, 2, 1]
]
```

**Output:**

```python
[
  [0, 0],
  [1, 1],
  [2, 2]
]
```

**Explanation:**  
This is the most optimal solution for the employees, where each employee gets one of their top choices.

---

## Example 2

**Input:**

```python
employees = [
    [2, 0, 1, 3],
    [1, 3, 2, 0],
    [0, 1, 2, 3],
    [3, 2, 1, 0]
]

projects = [
    [1, 2, 0, 3],
    [0, 3, 2, 1],
    [2, 1, 3, 0],
    [3, 0, 1, 2]
]
```

**Output:**

```python
[
    [0, 2],
    [1, 1],
    [2, 0],
    [3, 3]
]
```

**Explanation:**  
All employees are matched with their top-choice projects, and no unmatched pair would prefer each other over their current assignment.

---

## Example 3

**Input:**

```python
employees = [
    [1, 0, 2],
    [0, 2, 1],
    [2, 1, 0]
]

projects = [
    [1, 0, 2],
    [0, 2, 1],
    [2, 1, 0]
]
```

**Output:**

```python
[
    [0, 1],
    [1, 0],
    [2, 2]
]
```

**Explanation:**  
This is the most optimal solution, as each employee is matched to their top preference, and no employee-project pair would prefer to be matched with each other over their current assignment.

---

## Notes

- The function implements a variant of the Gale-Shapley algorithm to ensure stable and optimal assignments.
- Time Complexity: **O(N^2)**, where **N** is the number of employees/projects.
- Space Complexity: **O(N^2)**, due to the storage of preferences and intermediate data structures.

Happy coding!

