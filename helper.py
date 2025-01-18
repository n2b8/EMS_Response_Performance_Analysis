import numpy as np
from scipy.stats import kstest, norm, mannwhitneyu
import matplotlib.pyplot as plt
import seaborn as sns


class ComplianceTester:
    def __init__(self, data, compliance_column='compliance'):
        """
        Initialize the tester with a dataset and compliance column.

        Parameters:
            data (DataFrame): The dataset containing the features to test.
            compliance_column (str): The column name indicating compliance status.
        """
        self.data = data
        self.compliance_column = compliance_column

    def ks_test_normality(self, feature):
        """
        Perform KS tests for normality on the compliant and non-compliant groups.

        Parameters:
            feature (str): Name of the feature to test.
        """
        group1 = self.data[self.data[self.compliance_column] == 1][feature].dropna()
        group0 = self.data[self.data[self.compliance_column] == 0][feature].dropna()
        
        # KS test for group1
        mean1, std1 = np.mean(group1), np.std(group1)
        stat1, p_value1 = kstest(group1, 'norm', args=(mean1, std1))
        
        # KS test for group0
        mean0, std0 = np.mean(group0), np.std(group0)
        stat0, p_value0 = kstest(group0, 'norm', args=(mean0, std0))
        
        print(f"\nKolmogorov-Smirnov Normality Test for {feature}:")
        print(f"Compliant Group: KS Statistic = {stat1:.4f}, P-Value = {p_value1:.4f}")
        print(f"Non-Compliant Group: KS Statistic = {stat0:.4f}, P-Value = {p_value0:.4f}")

    def mann_whitney_test(self, feature, alternative='two-sided'):
        """
        Perform the Mann-Whitney U test.

        Parameters:
            feature (str): Name of the feature to test.
            alternative (str): Alternative hypothesis ('two-sided', 'less', 'greater').
        """
        group1 = self.data[self.data[self.compliance_column] == 1][feature].dropna()
        group0 = self.data[self.data[self.compliance_column] == 0][feature].dropna()
        stat, p_value = mannwhitneyu(group1, group0, alternative=alternative)
        
        print(f"\nMann-Whitney U Test for {feature}:")
        print(f"U Statistic = {stat:.4f}, P-Value = {p_value:.4f}")
        if p_value < 0.05:
            print("Result: Significant difference.")
        else:
            print("Result: No significant difference.")

    def plot_kde(self, feature):
        """
        Plot KDE for compliant and non-compliant groups.

        Parameters:
            feature (str): Name of the feature to plot.
        """
        group1 = self.data[self.data[self.compliance_column] == 1][feature].dropna()
        group0 = self.data[self.data[self.compliance_column] == 0][feature].dropna()
        
        sns.kdeplot(group1, label="Compliant", fill=True, color="blue", alpha=0.6)
        sns.kdeplot(group0, label="Non-Compliant", fill=True, color="orange", alpha=0.6)
        plt.title(f"KDE Plot for {feature} by Compliance")
        plt.xlabel(feature)
        plt.ylabel("Density")
        plt.legend()
        plt.show()

    def summarize_stats(self, feature):
        """
        Display summary statistics for compliant and non-compliant groups.

        Parameters:
            feature (str): Name of the feature to summarize.
        """
        group1 = self.data[self.data[self.compliance_column] == 1][feature].dropna()
        group0 = self.data[self.data[self.compliance_column] == 0][feature].dropna()
        
        print(f"\nSummary Statistics for {feature}:")
        print(f"Compliant Median: {group1.median():.4f}, Mean: {group1.mean():.4f}")
        print(f"Non-Compliant Median: {group0.median():.4f}, Mean: {group0.mean():.4f}")

    def test_feature(self, feature, alternative='two-sided'):
        """
        Perform all tests and visualizations for a specific feature.

        Parameters:
            feature (str): Name of the feature to test.
            alternative (str): Alternative hypothesis for the Mann-Whitney test.
        """
        self.ks_test_normality(feature)
        self.mann_whitney_test(feature, alternative)
        self.plot_kde(feature)
        self.summarize_stats(feature)