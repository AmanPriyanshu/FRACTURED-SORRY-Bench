from datasets import load_dataset
import json
from huggingface_hub import login
import pandas as pd

# Login to HuggingFace
with open("data.key", "r") as f:
    keys = json.load(f)
    login(keys['huggingface'])

# Load Datasets
ds = load_dataset("sorry-bench/sorry-bench-202406")
data = ds['train']

# Parsing out only Vanilla prompts
vanilla_questions, vanilla_categories = [], []
for category, turns, prompt_style in zip(data['category'], data['turns'], data['prompt_style']):
    if prompt_style!='base':
        continue
    if len(turns)!=1:
        print(category, len(turns), prompt_style)
    vanilla_questions.append(turns[0])
    vanilla_categories.append(category)

# Saving the questions in a CSV
pd.DataFrame({"categories": vanilla_categories, "questions": vanilla_questions}).to_csv("vanilla_questions.csv", index=False)