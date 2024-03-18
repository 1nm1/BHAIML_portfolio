import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import squarify

# Helper Functions
def print_df_information(
        df: pd.DataFrame, 
        df_name: str) -> None:
    print(f" === Inspecting {df_name} DataFrame ===")
    print(f'-------------\n{df.info(verbose=True)}')
    print(f'-------------\n Head: \n{df.head()}')
    print(f'-------------\n Columns: {df.columns}')
    print(f'-------------\n Numerical Description: \n{df.describe()}')
    print('-------------')
    for col in df.columns:
        nulls = df[col].isnull().sum()
        unique_values = df[col].nunique()
        print(f"{col}:")
        print(f"  {str(nulls).ljust(8)} null values")
        print(f"  {str(unique_values).ljust(8)} unique values")
    return

def plot_categorical_count_plot(
        df: pd.DataFrame, 
        df_name: str, 
        col: str) -> None:
    filename = f"{df_name}_{col}_count.png"
    title = f"{str(col).capitalize()} Countplot"
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title(title)
    plt.xlabel(col)
    plt.ylabel(f"{col}_count")
    plt.xticks(rotation=90)
    plt.savefig(f"./crop_yield/images/{filename}")
    plt.show()
    return

def plot_numerical_distribution_plot(
        df: pd.DataFrame, 
        df_name: str, 
        col: str) -> None:
    filename = f"{df_name}_{col}_dist.png"
    title = f"{str(col).capitalize()} Distribution Plot"
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=col, kde=True, bins=50)
    plt.title(title)
    plt.xlabel(col)
    plt.ylabel(f"{col}_count")
    plt.savefig(f"./crop_yield/images/{filename}")
    plt.show()
    return

def plot_tree_viz(
        df: pd.DataFrame,
        df_name: str,
        col: str,
        smallest: bool = True,
        amount: int = 10) -> None:
    row_counts = df[col].value_counts()
    row_counts=row_counts.reset_index(name='Row_count')
    row_counts.sort_values(by='Row_count', ascending=False, inplace=True)

    if smallest:
        graph_counts = row_counts[-amount:]
    else:
        graph_counts = row_counts[:amount]

    squarify.plot(sizes=graph_counts['Row_count'], label=graph_counts[col], alpha=.7)

    plt.axis('off')
    plt.title(f"{df_name} Tree Map of {col} Counts")
    plt.savefig(f"./crop_yield/images/{df_name}_{col}_tree.png")
    plt.show()

