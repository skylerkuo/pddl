pip install pyperplan

if you want to gemma2+pddl, you need prompt_template and domain.pddl and problem.pddl and problem2.pddl
please check the path of the pddl and prompt file

domain file : actions, rule of actions
problem file : initial state, goal state

ex:
goal:
(locked yellow_wire power_supply_6) (locked blue_wire power_supply_5)
output:
(pickup arm1 blue_wire)
(insert arm1 blue_wire power_supply_5)
(lock arm2 blue_wire power_supply_5)
(pickup arm1 yellow_wire)
(insert arm1 yellow_wire power_supply_6)
(lock arm2 yellow_wire power_supply_6)
