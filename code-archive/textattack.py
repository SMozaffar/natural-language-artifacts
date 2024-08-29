from transformers import AutoTokenizer, AutoModelForSequenceClassification, \
    AutoModelForQuestionAnswering, Trainer, TrainingArguments, HfArgumentParser
from textattack.models.wrappers import HuggingFaceModelWrapper


tokenizer = AutoTokenizer.from_pretrained('/content/drive/MyDrive/fp-dataset-artifacts-main/aug100_trained_model', use_fast=True) 
model = HuggingFaceModelWrapper(AutoModelForSequenceClassification.from_pretrained('/content/drive/MyDrive/fp-dataset-artifacts-main/aug100_trained_model'), tokenizer)

