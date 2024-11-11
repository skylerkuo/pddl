import subprocess
import os

domain_file = 'C:/Users/User/Desktop/gai_code/domain.pddl'
problem_file = 'C:/Users/User/Desktop/gai_code/problem.pddl'
problem2_file = 'C:/Users/User/Desktop/gai_code/problem2.pddl'

def update_pddl_problem(goal_conditions):
    with open(problem_file, 'r') as f:
        problem_content = f.read()
    updated_problem = problem_content.replace('#', goal_conditions)
    with open(problem2_file, 'w') as f:
        f.write(updated_problem)

def execute_planner():
    cmd = ['pyperplan', '-s', 'gbf', '-H', 'hadd', domain_file, problem2_file]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.stderr:
            print("error:")
            print(result.stderr)
            return None 

        solution_file = problem2_file + '.soln'
        if os.path.exists(solution_file):
            print("task plan（by PDDL）:")
            with open(solution_file, 'r') as f:
                solution = f.read()
                #print(solution)
            return solution 
        else:
            print("can not find the file")
            return None
    except FileNotFoundError:
        print("pyperplan not installed")
        return None