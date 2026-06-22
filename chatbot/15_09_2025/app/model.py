from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"  

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    return model, tokenizer

def generate_response(prompt, model, tokenizer):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
