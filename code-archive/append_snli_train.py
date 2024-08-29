from datasets import load_dataset, Dataset 
import pandas as pd

snli = load_dataset("snli")

df = pd.DataFrame(snli['train'])

adv_examples = pd.read_json("/Users/shawyan/Desktop/MSDS/NLP/Homework/Final-Project/Adversarial-challenge/adversarial_challenge.json", orient="list")

for index, row in adv_examples[:len(adv_examples) - 25].iterrows():
	df = pd.concat([df, pd.DataFrame([row])], ignore_index = True)


df.to_json("augmented_snli_75.json", orient='records', indent=4)


