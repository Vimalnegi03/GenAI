# import os
# os.environ["HF_TOKEN"]="Insert your hugging token"
# model_name="google/gemma-3-1b-it"
# from transformers import AutoTokenizer
# tokenizer=AutoTokenizer.from_pretrained(model_name)
# print(tokenizer("Hello,how are you"))
# from transformers import AutoModelForCausalLM
#  import torch -->this works at google collab
# model=AutoModelForCausalLM.from_pretrained(model_name,torch_dtype=torch.bfloat16)
# from transformers import pipeline
# gen_pipeline=pipeline("text-generation",model=model,tokenizer=tokenizer)
# gen_pipeline("heyThere",max_new_tokens=25)

# This code is for google collab