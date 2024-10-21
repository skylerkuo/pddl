import subprocess
import os

domain_file = 'your domain.pddl'
problem_file = 'your problem.pddl'

#since pddl would not put the action "lock" after "insert" so need to use the following function

def process_solution(solution):
    actions = solution.strip().split('\n')
    
    reordered_actions = []
    pending_installations = [] 
    
    for i, action in enumerate(actions):
        if action.startswith("(insert"):
            wire_name = action.split()[2]
            
            for j in range(i + 1, len(actions)):
                if actions[j].startswith("(lock") and wire_name in actions[j]:
                    reordered_actions.append(action) 
                    reordered_actions.append(actions[j])  
                    pending_installations.append(j) 
                    break
            else:
                reordered_actions.append(action)
        elif i not in pending_installations:
            reordered_actions.append(action)
    
    return '\n'.join(reordered_actions)

cmd = ['pyperplan', domain_file, problem_file]

try:
    result = subprocess.run(cmd, capture_output=True, text=True)

    solution_file = problem_file + '.soln'
    
    if os.path.exists(solution_file):
        with open(solution_file, 'r') as f:
            solution = f.read()
            solution = process_solution(solution)
            print(solution)

    
except FileNotFoundError:
    print("pyperplan uninstall")

