import re

valid_objects = ['red_wire', 'blue_wire', 'green_wire','black_wire','yellow_wire']
valid_locations = [f'power_supply_{i}' for i in range(1, 10)]
valid_workspace = ['table']



def check_action(input_text,a):
    match = re.match(r'\((\w+)\s+(\w+)(?:\s+(\w+_\d+|\w+))?\)', input_text)
    error = []
    if not match:
        error.append(f"Invalid format: {input_text}")
        a=1

    action, obj, loc = match.groups()
    
    
    if action == 'holding':
        if obj not in valid_objects:
            error.append(f"There is no object: {obj}. But there are objects: {valid_objects}")
            a=1
    elif action in ['locked', 'inserted']:
        if obj not in valid_objects:
            error.append(f"There is no object: {obj}. But there are objects: {valid_objects}")
            a=1
        if loc not in valid_locations:
            error.append(f"There is no location: {loc}. But there are connection points of a power supply: {valid_locations} ")
            a=1
    elif action in ['on']:
        if obj not in valid_objects:
            error.append(f"There is no object: {obj}. But there are objects: {valid_objects}")
            a=1
        if loc not in valid_workspace:
            error.append(f"There is no: {obj}. But there are workspace: {valid_workspace}")
            a=1
    else:
        error.append(f"There is no function {action}")
        a=1
    return error , a

def check_multiple_actions(combined_input):
    actions = re.findall(r'\(.*?\)', combined_input)
    results = []
    a=0
    for action in actions:
        result,a = check_action(action,a)
        results.append(result)
    return results,a

