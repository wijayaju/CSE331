def stable_assignments(employees, projects):
    """
    Solves the stable assignment problem using a variant of the Gale-Shapley algorithm.

    The problem is to assign each employee to a project such that the matching
    is stable. A matching is stable if there is no unmatched pair of an employee and a project
    such that both the employee and the project prefer each other over their current assignment.

    Parameters:
    employees (list[list[int]]): A 2D list where each sublist represents an employee's preference
                                 ranking for projects, with the index representing the project and the
                                 integer value representing their rank (lower is more preferred).
                                 Each employee must rank all projects.
    projects (list[list[int]]): A 2D list where each sublist represents a project's preference ranking
                                for employees, with the index representing the employee and the
                                integer value representing their rank (lower is more preferred).
                                Each project must rank all employees.

    Returns:
    list[list[int]]: A list of pairs [employee_index, project_index], where each pair represents an
                     optimal assignment of employee to project, ensuring no blocking pairs exist
                     (i.e., no employee and project both prefer each other over their current match).

    Time Complexity: O(n^2), where n is the number of employees and projects.
    Space Complexity: O(n^2), where n is the number of employees and projects.

    Example:

    # >>> employees = [
    # >>>   [0, 1, 2],
    # >>>   [0, 2, 1],
    # >>>   [1, 2, 0]
    # >>> ]
    # >>> projects = [
    # >>>   [2, 1, 0],
    # >>>   [0, 1, 2],
    # >>>   [0, 1, 2]
    # >>> ]
    # >>> stable_assignments(employees, projects)
    [[0, 1], [1, 0], [2, 2]]
    """
    initial_assignment = dict()
    no_assignment = list()
    optimized_assignment = list()
    for employee in range(len(employees)):
        no_assignment.append(employee)

    while no_assignment:  # until no assignment is empty
        employee = no_assignment.pop(0)
        employee_prefs = employees[employee]
        for project in employee_prefs:
            if project not in initial_assignment:
                initial_assignment[project] = employee
                break
            else:  # check if current employee is more preferred than assigned employee
                cur_employee = initial_assignment[project]
                proj_prefs = projects[project]
                if proj_prefs.index(employee) < proj_prefs.index(cur_employee):  # compare indices
                    initial_assignment[project] = employee
                    no_assignment.append(cur_employee)
                    break
    for project in initial_assignment:  # format return data
        optimized_assignment.append([initial_assignment[project], project])
    return optimized_assignment
