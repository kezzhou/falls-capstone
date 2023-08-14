import pandas as pd
import matplotlib.pyplot as plt

class Helper:
    """
        Helper Class to avoid code repetition
    """
    def __init__(self):
        pass
    
    def display_bar_chart(self, index, values, title, xlabel, ylabel, export_loc, bar_width=0.5, figsize=(10, 7.5)):
        """
            Helper Function to display a Bar chart
        """
        # Convert index to categorical with specified order
        index = pd.Categorical(index, categories=index, ordered=True)

        # Create a DataFrame to plot
        df = pd.DataFrame({'index': index, 'values': values})

        # Plot the bar chart
        ax = df.plot(kind='bar', x='index', y='values', legend=False, width=bar_width, figsize=figsize)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()  # Adjust layout to prevent clipping
        plt.savefig(export_loc)
        plt.close()  # Close the current figure

    def display_pie_chart(self, labels, sizes, title, export_loc, display_percentage=True, figsize=(10, 7.5)):
        """
            Helper Function to display a Pie chart
        """
        # Set the figure size
        plt.figure(figsize=figsize)

        if display_percentage:
            autopct_format = '%1.1f%%'
        else:
            autopct_format = lambda p: '{:.0f}'.format(p * sum(sizes) / 100)

        plt.pie(sizes, labels=labels, autopct=autopct_format, startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(title)
        plt.savefig(export_loc)
        plt.close()  # Close the current figure


