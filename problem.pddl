(define (problem install-multiple-wires)
  (:domain robot-arm)
  (:objects
    arm1 arm2 - robot
    red_wire blue_wire green_wire black_wire yellow_wire - wire
    power_supply table - location
  )
  (:init ;you can change the initial state here
    (arm-empty arm1)
    (available red_wire)
    (available blue_wire)
    (available green_wire)
    (available black_wire)
    (available yellow_wire)
    (is-arm2 arm2)
    (is-arm1 arm1)
  )
  (:goal ;you can change the goal here
    (and
    (locked yellow_wire power_supply)
    (locked blue_wire power_supply)
    )
  )
)


    ;(arm-empty arm)
