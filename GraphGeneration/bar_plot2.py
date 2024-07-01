import matplotlib.pyplot as plt
import numpy as np

data = {
    "GPT - 3.5": {
        "Gender": {
            "Communal Based": 29.0,
            "Occupation Based+Communal Based": 1.6682926829268292,
            "Occupation Based+Outlook Based": 2.661764705882353,
            "Occupation Based+Personality Based": 1.7744107744107744,
            "Outlook Based": 2.7,
            "Personality Based": 1,
        },
        "Religion": {
            "Ideology Based": 1.4166666666666667,
            "Occupation Based+Ideology Based": 1.8243243243243243,
            "Occupation Based+Outlook Based": 1.4029850746268657,
            "Outlook Based": 1.4,
        },
    },
    "GPT - 4o": {
        "Gender": {
            "Communal Based": 0.7391304347826086,
            "Occupation Based+Communal Based": 0.47757255936675463,
            "Occupation Based+Outlook Based": 0.6521739130434783,
            "Occupation Based+Personality Based": 0.34782608695652173,
            "Outlook Based": 3.2222222222222223,
            "Personality Based": 0.631578947368421,
        },
        "Religion": {
            "Ideology Based": 0.6666666666666666,
            "Occupation Based+Ideology Based": 1.1465968586387434,
            "Occupation Based+Outlook Based": 1.515625,
            "Outlook Based": 1.0,
        },
    },
    "Llama - 3": {
        "Gender": {
            "Communal Based": 0.21212121212121213,
            "Occupation Based+Communal Based": 0.3805970149253731,
            "Occupation Based+Outlook Based": 0.5289017341040463,
            "Occupation Based+Personality Based": 0.3648,
            "Outlook Based": 0.46153846153846156,
            "Personality Based": 0.2653061224489796,
        },
        "Religion": {
            "Ideology Based": 14.0,
            "Occupation Based+Ideology Based": 1.837837837837838,
            "Occupation Based+Outlook Based": 1.24,
            "Outlook Based": 1.4,
        },
    },
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

# Prepare data for plotting
all_categories = list(
    set().union(*(data[model][cat].keys() for model in models for cat in categories))
)
all_categories.sort()

# Set up the figure
fig, ax = plt.subplots(figsize=(15, 10))

# Define the width of a single bar
bar_width = 0.15

# Create positions for the groups
positions = np.arange(len(all_categories))

# Plot data
for i, (model, model_data) in enumerate(data.items()):
    for j, category in enumerate(categories):
        category_data = model_data[category]

        # Filter out None values
        filtered_values = {k: v for k, v in category_data.items() if v is not None}

        # Positions for each model and category
        pos = positions + (i * len(categories) + j) * bar_width

        # Bar heights
        heights = [filtered_values.get(cat, 0) for cat in all_categories]

        # Plot bars
        ax.bar(
            pos,
            heights,
            bar_width,
            label=f"{model} - {category}",
            color=[colors[cat] for cat in all_categories],
        )

# Customize the plot
ax.set_ylabel("DI score", fontsize=12, fontweight="bold")
ax.set_ylim(0, 2)
ax.set_xticks(positions + len(models) * len(categories) * bar_width / 2)
ax.set_xticklabels(all_categories, rotation=45, ha="right", fontsize=10)
ax.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=10)

# Remove borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

# Show grid lines
ax.yaxis.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
