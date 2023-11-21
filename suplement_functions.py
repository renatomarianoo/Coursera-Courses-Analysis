import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def group_column(df, column1, column2=None):
    """Function to group the values of column1 in relation column2
    In case no values are passed to column2, a value_count() will be made
    """
    if column2 == None:
        df_local = df[column1].value_counts()
        df_local = pd.DataFrame({column1: df_local.index, "count": df_local.values})
    else:
        df_local = df.groupby(column1)[column2].sum().sort_values(ascending=False)
        df_local = pd.DataFrame({column1: df_local.index, column2: df_local.values})
    return df_local


def clear_barplot(plot_title="", plot_xlabel="", plot_ylabel=""):
    """Docstrings are very important!!
    """
    plt.title(plot_title, fontsize="18")
    plt.xlabel(plot_xlabel)
    plt.ylabel(plot_ylabel)
    plt.xticks([])

    # remove the frame of the chart
    for spine in plt.gca().spines.values():
        spine.set_visible(False)


def clear_scatterplot(plot_title="", plot_xlabel="", plot_ylabel=""):

    plt.title(plot_title, fontsize="18")
    plt.xlabel(plot_xlabel)
    plt.ylabel(plot_ylabel)

    plt.grid(False)

    plt.tick_params(
        axis="both",
        bottom=True,
        left=True,
        width=2,
        color="lightgrey",
        labelcolor="black",
    )

    for spine in plt.gca().spines.values():
        spine.set_edgecolor("lightgrey")


def clear_countplot(plot_title='', plot_xlabel='', plot_ylabel=''):
    
    plt.title(plot_title, fontsize='18')
    plt.xlabel(plot_xlabel)
    plt.ylabel(plot_ylabel)
    
    plt.legend(loc='upper right')
    
    # remove the frame of the chart
    for spine in plt.gca().spines.values():
        spine.set_visible(False)