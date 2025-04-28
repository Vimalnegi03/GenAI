
import os
os.environ["HF_TOKEN"]="Insert your hugging face token please"
from transformers import AutoTokenizer,AutoModelForCausalLM
model_name="google/gemma-3-1b-it"
tokenizer=AutoTokenizer.from_pretrained(model_name)
input_prompt=["the capital of inida is"]
detokenized=tokenizer(input_prompt,return_tensors="pt")
print(detokenized)
# import torch-->this works at google collab
model=AutoModelForCausalLM.from_pretrained(
    model_name,
    # torch_dtype=torch.bfloat16-->works well at google collab
)
gen_result=model.generate(detokenized["input_ids"],max_new_tokens=25)
print(gen_result)
output=tokenizer.batch_decode(gen_result)
print(output)