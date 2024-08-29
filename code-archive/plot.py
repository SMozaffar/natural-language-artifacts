import numpy as np
import matplotlib.pyplot as plt

# Example data points
fine_tuning_examples = np.array([0, 25, 50, 75, 106])
ft_electra = np.array([89.68, 89.23, 89.73, 89.96, 90.17])

# Plotting the data
plt.figure(figsize=(10, 8))
plt.ylim(85, 95)

plt.plot(fine_tuning_examples, ft_electra, 'o-', label='Fine-tuned ELECTRA-small', markersize=8, linewidth=3)

# Adding titles and labels
plt.title('Accuracies of Fine-tuned model')
plt.xlabel('# of Fine-Tuning Examples')
plt.ylabel('Accuracy')
plt.legend(fontsize=14, loc='lower right')

# Show the plot
plt.tight_layout()
plt.show()
