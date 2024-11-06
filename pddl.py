import subprocess
import os

domain_file = 'C:/Users/User/Desktop/pddlfile/domain.pddl'
problem_file = 'C:/Users/User/Desktop/pddlfile/problem2.pddl'

cmd = ['pyperplan', '-s', 'gbf', '-H', 'hadd', domain_file, problem_file]

try:
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        #print("success!")
        solution_file = problem_file + '.soln'
        
        if os.path.exists(solution_file):
            #print(f"solution file location: {solution_file}")
            with open(solution_file, 'r') as f:
                solution = f.read()
                print("task plan:")
                print(solution)
            
            with open(solution_file, 'w') as f:
                f.write('')

except FileNotFoundError:
    print("pyperplan not install correctly。")
