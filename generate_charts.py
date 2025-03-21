import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
df = pd.read_csv('covid_data.csv')

# Create a directory to save the charts
if not os.path.exists('charts'):
    os.makedirs('charts')

# Function to save plots
def save_plot(fig, filename):
    fig.savefig(f'charts/{filename}.png')
    plt.close(fig)

# Generate and save charts
def generate_charts():
    # Age Distribution
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['AGE'], bins=30, kde=True, ax=ax)
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    save_plot(fig, 'age_distribution')

    # Death Ratio
    df['DIED'] = df['DATE_DIED'].apply(lambda x: 1 if x != '9999-99-99' else 0)
    died_counts = df['DIED'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(died_counts, labels=['Alive', 'Died'], autopct='%1.1f%%', colors=['green', 'red'])
    ax.set_title('Death Ratio')
    save_plot(fig, 'death_ratio')

    # Comorbidities vs Death
    comorbidities = ['DIABETES', 'COPD', 'ASTHMA', 'HIPERTENSION', 'OTHER_DISEASE', 'CARDIOVASCULAR', 'OBESITY', 'RENAL_CHRONIC', 'TOBACCO']
    fig, ax = plt.subplots(figsize=(10, 8))
    for i, comorbidity in enumerate(comorbidities):
        plt.subplot(3, 3, i + 1)
        sns.countplot(x=comorbidity, hue='DIED', data=df, palette='Set2')
        plt.title(f'{comorbidity} vs Death')
    plt.tight_layout()
    save_plot(fig, 'comorbidities_vs_death')

    # Sex vs Death
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='SEX', hue='DIED', data=df, palette='Set1', ax=ax)
    ax.set_title('Sex vs Death')
    ax.set_xlabel('Sex (1 = Male, 2 = Female)')
    ax.set_ylabel('Count')
    save_plot(fig, 'sex_vs_death')

    # Age vs ICU Admission
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='ICU', y='AGE', data=df, palette='Set3', ax=ax)
    ax.set_title('Age vs ICU Admission')
    ax.set_xlabel('ICU Admission')
    ax.set_ylabel('Age')
    save_plot(fig, 'age_vs_icu')

# Run the chart generation
if __name__ == "__main__":
    generate_charts()
    print("Charts generated and saved in the 'charts' folder.")