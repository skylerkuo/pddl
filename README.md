pip install pyperplan

domain file : actions, rule of actions
problem file : initial state, goal state

ex:
goal:
(locked yellow_wire power_supply) (locked blue_wire power_supply)
output:
(pickup arm1 blue_wire)
(insert arm1 blue_wire power_supply)
(lock arm2 blue_wire power_supply)
(pickup arm1 yellow_wire)
(insert arm1 yellow_wire power_supply)
(lock arm2 yellow_wire power_supply)
