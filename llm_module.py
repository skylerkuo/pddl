from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

nf4_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)

def load_model_and_tokenizer(model_name="google/gemma-2-9b-it"):
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=nf4_config,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def generate_response(model, tokenizer, prompt):
    prompt_tokens = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    
    outputs = model.generate(
        prompt_tokens,
        max_new_tokens=200,
        pad_token_id=tokenizer.eos_token_id 
    )
    output_tokens = outputs[0].tolist()
    prompt_tokens_list = prompt_tokens[0].tolist()
    
    if len(output_tokens) > len(prompt_tokens_list):
        output_tokens = output_tokens[len(prompt_tokens_list):]
    response_cleaned = tokenizer.decode(output_tokens, skip_special_tokens=True).strip()
    
    return response_cleaned
