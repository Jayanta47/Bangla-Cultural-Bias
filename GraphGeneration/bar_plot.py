import matplotlib.pyplot as plt
import numpy as np

# Provided JSON data
data = {
    "GPT - 3.5": {
        "Gender": {
            "Communal Based": 29.0,
            "Occupation Based+Communal Based": 1.6682926829268292,
            "Occupation Based+Outlook Based": 2.661764705882353,
            "Occupation Based+Personality Based": 1.7744107744107744,
            "Outlook Based": 2.7,
            "Personality Based": 1
        },
        "Religion": {
            "Ideology Based": 1.4166666666666667,
            "Occupation Based+Ideology Based": 1.8243243243243243,
            "Occupation Based+Outlook Based": 1.4029850746268657,
            "Outlook Based": 1.4
        }
    },
    "GPT - 4o": {
        "Gender": {
            "Communal Based": 0.7391304347826086,
            "Occupation Based+Communal Based": 0.47757255936675463,
            "Occupation Based+Outlook Based": 0.6521739130434783,
            "Occupation Based+Personality Based": 0.34782608695652173,
            "Outlook Based": 3.2222222222222223,
            "Personality Based": 0.631578947368421
        },
        "Religion": {
            "Ideology Based": 0.6666666666666666,
            "Occupation Based+Ideology Based": 1.1465968586387434,
            "Occupation Based+Outlook Based": 1.515625,
            "Outlook Based": 1.0
        }
    },
    "Llama - 3": {
        "Gender": {
            "Communal Based": 0.21212121212121213,
            "Occupation Based+Communal Based": 0.3805970149253731,
            "Occupation Based+Outlook Based": 0.5289017341040463,
            "Occupation Based+Personality Based": 0.3648,
            "Outlook Based": 0.46153846153846156,
            "Personality Based": 0.2653061224489796
        },
        "Religion": {
            "Ideology Based": 14.0,
            "Occupation Based+Ideology Based": 1.837837837837838,
            "Occupation Based+Outlook Based": 1.24,
            "Outlook Based": 1.4
        }
    }
}

# Models and categories
models = list(data.keys())
categories = ["Gender", "Religion"]

# Define the colors for different categories
colors = {
    "Communal Based": "#8AC926",  # Greenish
    "Occupation Based+Communal Based": "#1982C4",  # Blue
    "Occupation Based+Outlook Based": "#FFCA3A",  # Yellow
    "Occupation Based+Personality Based": "#FF595E",  # Red
    "Outlook Based": "#6A4C93",  # Purple
    "Personality Based": "#4CC9F0",  # Light Blue
    "Ideology Based": "#00AFB9",  # Cyan
    "Occupation Based+Ideology Based": "#F15BB5",  # Pink
}

# Set up the figure and axes
fig, axs = plt.subplots(2, 3, figsize=(15, 10), sharey='row')
fig.subplots_adjust(hspace=0.4, wspace=0.3)

# Iterate through models and categories
for col, model in enumerate(models):
    for row, category in enumerate(categories):
        ax = axs[row, col]
        values = data[model][category]
        
        # Filter out None values
        filtered_values = {k: v for k, v in values.items() if v is not None}
        
        # Plot bars
        bars = ax.bar(filtered_values.keys(), filtered_values.values(),
                      color=[colors[k] for k in filtered_values.keys()])
        ax.set_title(f"{model}", fontsize=14, fontweight='bold')
        
        # Remove x-axis labels
        ax.set_xticks([])

        ax.set_ylim(0, 2)
        
        # Set y-axis label for the first column
        if col == 0:
            ax.set_ylabel('DI score', fontsize=12, fontweight='bold')
        
        # Set x-axis label for the second row
        if row == 1:
            ax.set_xlabel('Categories', fontsize=12, fontweight='bold')
        
        # Add legend only for the first column of each row
        if col == 0:
            ax.legend(filtered_values.keys(), loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Adjust overall layout and show the plot
plt.tight_layout()
plt.show()
