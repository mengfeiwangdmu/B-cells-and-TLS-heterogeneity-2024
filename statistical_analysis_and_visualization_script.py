
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data
df_groups = pd.read_excel('F:/paper/paper2/original data/Total Area/sum area two groups.xlsx')

# Correcting the dataframe's headers
df_groups.columns = df_groups.iloc[0]
df_groups = df_groups[1:]

# Converting data to numeric, errors='coerce' converts non-numeric values to NaN
df_groups['LN no meta'] = pd.to_numeric(df_groups['LN no meta'], errors='coerce')
df_groups['LN meta'] = pd.to_numeric(df_groups['LN meta'], errors='coerce')

# Dropping NaN values
df_groups.dropna(inplace=True)

# Statistical analysis: Mann-Whitney U test
mann_whitney_test_result = stats.mannwhitneyu(df_groups['LN no meta'], df_groups['LN meta'], alternative='two-sided')

# Visualization
sns.set(style="ticks", font_scale=1.2)
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(data=df_groups, ax=ax, palette="Set2")
ax.set_title('Mann-Whitney U Test Results', fontsize=18, fontweight='bold')
ax.set_xlabel('Group', fontsize=16, fontweight='bold')
ax.set_ylabel('Total Area (µm²)', fontsize=16, fontweight='bold')
ax.text(0.5, max(df_groups.max())*0.9, f'Mann-Whitney U test\np = {mann_whitney_test_result.pvalue:.4f}', 
        ha='center', va='center', fontsize=14, fontweight='bold', color='red', 
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))
ax.set_xticklabels(['LN no meta', 'LN meta'], fontweight='bold')
sns.despine()
plt.tight_layout()

# Save the figure as a PDF
fig.savefig('Mann_Whitney_U_Test_Results.pdf', format='pdf')
