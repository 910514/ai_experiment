import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model(model_path):
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map='auto', torch_dtype=torch.float16, load_in_8bit=True)
    model = model.eval()
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)
    tokenizer.pad_token = tokenizer.eos_token
    return model, tokenizer

def generate_response(model, tokenizer, prompt):
    input_ids = tokenizer([f'<s>Human: {prompt}\n</s><s>Assistant: '], return_tensors="pt", add_special_tokens=False).input_ids.to('cuda')        
    generate_input = {
        "input_ids": input_ids,
        "max_new_tokens": 512,
        "do_sample": True,
        "top_k": 50,
        "top_p": 0.95,
        "temperature": 0.3,
        "repetition_penalty": 1.3,
        "eos_token_id": tokenizer.eos_token_id,
        "bos_token_id": tokenizer.bos_token_id,
        "pad_token_id": tokenizer.pad_token_id
    }
    generate_ids = model.generate(**generate_input)
    text = tokenizer.decode(generate_ids[0])
    return text

if __name__ == "__main__":
    model_path = 'D:\\Atom-7B-Chat'
    model, tokenizer = load_model(model_path)

    while True:
        user_prompt = input("Enter your prompt (type 'exit' to quit): ")
        
        if user_prompt.lower() == 'exit':
            break

        response = generate_response(model, tokenizer, user_prompt)
        print("Assistant:", response)
