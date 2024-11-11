from transformers import logging as hf_logging
from llm_module import load_model_and_tokenizer, generate_response  
from pddl_module import update_pddl_problem, execute_planner
from validator_module import check_action, check_multiple_actions
from itertools import chain

hf_logging.set_verbosity_error()

def main():
    prompt_generate_goal_template_file = 'C:/Users/User/Desktop/gai_code/generate_goal_prompt.txt'
    prompt_reply_user_ok_template_file = 'C:/Users/User/Desktop/gai_code/reply_user_ok_prompt.txt'
    prompt_error_qa_template_file = 'C:/Users/User/Desktop/gai_code/error_qa_prompt.txt'
    with open(prompt_generate_goal_template_file, 'r', encoding='utf-8') as f:
        prompt_generate_goal_template = f.read()
    with open(prompt_reply_user_ok_template_file, 'r', encoding='utf-8') as f:
        prompt_reply_user_ok_template = f.read()
    with open(prompt_error_qa_template_file, 'r', encoding='utf-8') as f:
        prompt_error_qa_template = f.read()
    model, tokenizer = load_model_and_tokenizer()
    while True:
        user_input = input("command（you can enter'exit'）：")
        if user_input.lower() == 'exit':
            print("end")
            break
        prompt_generate_goal = prompt_generate_goal_template.replace('#', user_input)
        goal_conditions = generate_response(model, tokenizer, prompt_generate_goal)
        #print("goal state（from LLM）:", goal_conditions)
        errordescribe,a = check_multiple_actions(goal_conditions)
        if a==0:
            goal_conditions2 = goal_conditions.replace("_", " ")
            prompt_reply_user_ok = prompt_reply_user_ok_template.replace('#', goal_conditions2)
            reply_ok = generate_response(model, tokenizer, prompt_reply_user_ok)
            print(reply_ok)
            update_pddl_problem(goal_conditions)
            solution = execute_planner()
            print(solution)
        else:
            errordescribe = ", ".join(chain.from_iterable(errordescribe))
            errordescribe = errordescribe.replace("power_supply_", "")
            errordescribe = errordescribe.replace("_", " ")
            errordescribe = errordescribe.replace("[", " ")
            errordescribe = errordescribe.replace("]", " ")
            prompt_error_qa = prompt_error_qa_template.replace('#', errordescribe)
            prompt_error_qa = prompt_error_qa.replace('@', user_input)
            error_qa = generate_response(model,tokenizer,prompt_error_qa)
            print(error_qa)
        

if __name__ == "__main__":
    main()
