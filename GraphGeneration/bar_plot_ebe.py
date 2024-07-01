# sort_order = {
#     "Communal": 3,
#     "Occupation+Communal": 7,
#     "Occupation+Outlook": 6,
#     "Occupation+Personality": 4,
#     "Outlook": 2,
#     "Personality": 1,
#     "Occupation+Ideology": 5,
#     "Ideology": 0,
# }

data = {
    "GPT - 4o": {"Gender": 4.28, "Religion": 0.64},
    "GPT - 3.5": {"Gender": 1.18, "Religion": 0.95},
    "Llama - 3": {"Gender": 0.64, "Religion": 0.77},
}

# Models and categories
models = list(data.keys())
categories = ["Gender", "Religion"]

# Define the colors for different categories
# colors = {
#     "Communal Based": "#8AC926",  # Greenish
#     "Occupation Based+Communal Based": "#1982C4",  # Blue
#     "Occupation Based+Outlook Based": "#FFCA3A",  # Yellow
#     "Occupation Based+Personality Based": "#FF595E",  # Red
#     "Outlook Based": "#6A4C93",  # Purple
#     "Personality Based": "#4CC9F0",  # Light Blue
#     "Ideology Based": "#00AFB9",  # Cyan
#     "Occupation Based+Ideology Based": "#F15BB5",  # Pink
# }

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the seaborn style
sns.set(style="whitegrid")

# Colors for each model
model_colors = {
    "GPT - 3.5": sns.color_palette("muted")[0],  # Blue
    "GPT - 4o": sns.color_palette("muted")[2],  # Red
    "Llama - 3": sns.color_palette("muted")[3],  # Green
}

# Set up the figure
fig, ax = plt.subplots(figsize=(6, 6))

# Define the width of a single bar
bar_width = 0.2

key = "Religion"

# Prepare data for plotting
all_gender_categories = list(set().union(*(data[model].keys() for model in models)))
all_gender_categories.sort()
print(all_gender_categories)

# Create positions for the groups
num_models = len(models)
num_categories = len(all_gender_categories)
positions = np.arange(num_categories) * (bar_width * (num_models + 1))

# Plot data
for i, model in enumerate(models):
    category_data = data[model]

    # Filter out None values
    filtered_values = {k: v for k, v in category_data.items() if v is not None}

    # Bar heights
    heights = [filtered_values.get(cat, 0) for cat in all_gender_categories]

    # Plot bars
    ax.bar(
        positions + i * bar_width,
        heights,
        bar_width,
        label=model,
        color=model_colors[model],
        edgecolor="black",  # Add borders
    )

# Customize the plot
ax.set_ylabel("DI score", fontsize=14, fontweight="bold")
ax.set_ylim(0, 2)
ax.set_xticks(positions + (num_models - 1) * bar_width / 2)
ax.set_xticklabels(all_gender_categories, rotation=30, ha="right", fontsize=14)
ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, 1.15),
    fontsize=12,
    ncol=num_models,
    frameon=True,
)

# Remove vertical gridlines and keep horizontal gridlines
ax.grid(axis="y", linestyle="--", linewidth=0.7)
ax.grid(axis="x", visible=False)

# Make the horizontal line at y=1 bold
ax.axhline(y=1, color="cyan", linewidth=2)

# Tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
