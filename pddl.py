import subprocess
import os

domain_file = 'C:/Users/User/Desktop/gai_code/ex1_domain.pddl'
problem_file = 'C:/Users/User/Desktop/gai_code/ex1_problem.pddl'

cmd = [
    'pyperplan',
    '-s', 'gbf', #'astar'、'gbf'
    '-H', 'hadd', #'hmax'、'hadd'
    domain_file,
    problem_file
]

try:
    result = subprocess.run(cmd, capture_output=True, text=True)
    # print(result.stdout)
    if result.returncode == 0:
        solution_file = problem_file + '.soln'
        if os.path.exists(solution_file):
            with open(solution_file, 'r') as f:
                solution = f.read()
                print("task plan：")
                print(solution)

            with open(solution_file, 'w') as f:
                f.write('')
        else:
            print("can not find file")
    else:
        print("Pyperplan error:")
        print(result.stderr)

except FileNotFoundError:
    print("uninstall Pyperplan。")
