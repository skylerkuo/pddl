pip install pyperplan

if you want to run only pddl planner, please download problem2.pddl and doamin.pddl and pddl.py. then, edit the path of the domain file and problem file in the pddl.py

input of pddl format:
1. (holding A) ex: (holding red_wire)
2. (locked A B) ex: (locked red_wire power_supply_5)
3. (inserted A B) ex: (inserted red_wire power_supply_5)
4. (on A B) ex: (on red_wire table)

output of pddl format:
1. (pickup ?arm A B) ex: (pickup arm1 red_wire table)
2. (lock ?arm A B) ex: (lock arm2 red_wirepower_supply_5)
3. (inserted ?arm A B) ex: (insert arm1 red_wire power_supply_5)
4. (putdown ?arm A B) ex: (putdown arm1 red_wire power_supply_5)
