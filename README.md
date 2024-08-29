# Investigation and Mitigation of Dataset Artifacts in Natural Language Inference (NLI)

## Abstract

This project investigates dataset artifacts in Natural Language Inference (NLI) using model ablations and adversarial challenge sets. We explore how state-of-the-art NLP models can unintentionally learn and rely on unintended dataset artifacts, leading to biased results. The study employs the TextAttack framework and an ELECTRA-small model to identify and quantify these artifacts. We propose data augmentation and model fine-tuning as methods to improve model robustness, particularly towards neutral-labeled examples, enhancing accuracy and generalizability in NLI tasks.

## Introduction

### Background

Natural Language Inference (NLI) focuses on determining the relationship between a premise and a hypothesis in natural language. If the hypothesis is supported by the premise, the relationship is classified as entailment; if it opposes, as contradiction; and if the relationship is uncertain, as neutral.

### The SNLI Dataset

The Stanford Natural Language Inference (SNLI) dataset, created by Bowman et al. (2015), is a large-scale dataset consisting of 570K human-labeled premise-hypothesis pairs. These pairs are categorized into entailment, neutral, or contradiction, providing a comprehensive resource for training and evaluating NLI models.

### Dataset Artifacts

While NLP models can achieve high performance on datasets like SNLI, they may inadvertently learn certain unintended patterns or biases known as dataset artifacts. These artifacts can skew the model’s learning process, reducing generalizability and leading to an overestimation of the model's understanding of natural language.

### Adversarial Challenge Sets

Adversarial challenge sets are crafted inputs designed to expose vulnerabilities in models by revealing their reliance on dataset-specific cues rather than true language understanding. By creating minimal pairs or counterfactuals, these sets test the robustness of models to subtle variations in input.

### TextAttack Framework

The TextAttack framework allows for structured adversarial attacks on NLP models to identify and quantify the influence of dataset artifacts. By introducing subtle input variations that maintain semantic meaning, TextAttack helps assess whether a model is overfitting to specific lexical patterns or genuinely understanding the underlying semantics.

## Investigation of Dataset Artifacts

### Detection of Artifacts

We utilized the ELECTRA-small model, which is computationally efficient and designed to replace input tokens with plausible alternatives during training. We trained the model on the full SNLI dataset and also on a hypothesis-only dataset to detect the presence of dataset artifacts.

### Exploratory Analysis of SNLI

Our analysis revealed that the model struggled most with neutral-labeled examples, often misclassifying them as entailment or contradiction. This finding led us to focus on improving the model's accuracy in predicting neutral labels.

## Mitigation of Dataset Artifacts

### TextAttack Recipes and Perturbations

We applied 14 different TextAttack recipes to 100 examples from the SNLI train set, each designed to perturb the input text and challenge the model's robustness. The attack success rate for each recipe was recorded, with a higher rate indicating greater model sensitivity to that perturbation.

### Improving Accuracy with Augmentation

To mitigate dataset artifacts, we implemented a data augmentation strategy using TextAttack perturbations to create an adversarial challenge set. We fine-tuned the model on this augmented dataset, leading to a 0.49% improvement in accuracy on the SNLI test set.

## Results

### Evaluation of Models

We evaluated both the base ELECTRA-small model and the fine-tuned model on the SNLI test set, analyzing the types of incorrect predictions made by each. The fine-tuned model showed a notable improvement in accuracy, particularly in predicting neutral labels and contradictions.

### Analysis of Errors

The fine-tuned model demonstrated increased robustness to neutral-labeled examples and improved sensitivity to contradiction-labeled examples. This suggests that our data augmentation strategy effectively addressed the dataset artifacts present in the original training data.

## Discussion

The results indicate that the fine-tuned model is more accurate in predicting neutral and contradiction labels, reflecting an improved understanding of the nuances in NLI tasks. The data augmentation process helped the model learn to avoid overfitting to superficial patterns, resulting in better generalization to new inputs.

## References

- Bowman, S. R., Angeli, G., Potts, C., & Manning, C. D. (2015). A large annotated corpus for learning natural language inference. In *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing*, pages 632–642.
- Clark, K., Luong, M.-T., Le, Q. V., & Manning, C. D. (2020). ELECTRA: Pretraining text encoders as discriminators rather than generators. In *Proceedings of the International Conference on Learning Representations* (ICLR).
- Gururangan, S., Swayamdipta, S., Levy, O., Schwartz, R., Bowman, S., & Smith, N. A. (2018). Annotation artifacts in natural language inference data. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies*, Volume 1 (Long Papers), pages 107–112.
- Jia, R., & Liang, P. (2017). Adversarial examples for evaluating reading comprehension systems. In *Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing* (EMNLP).
- Morris, J., Lifland, E., Yoo, J. Y., Grigsby, J., Jin, D., & Qi, Y. (2020). TextAttack: A framework for adversarial attacks, data augmentation, and adversarial training in NLP. arXiv preprint arXiv:2005.05909.
- Wallace, E., Wang, Y., Li, S., Singh, S., & Gardner, M. (2019). Do NLP models know numbers? Probing numeracy in embeddings. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing* (EMNLP).
