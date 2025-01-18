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
    Perform KS tests for normality on the compliant and non-compliant groups with verbose output.

    Parameters:
        feature (str): Name of the feature to test.
    """
    # Generate dynamic group names
    feature_name = feature.replace('_', ' ').title()
    group1_name = f"{feature_name} - Compliant"
    group0_name = f"{feature_name} - Non-Compliant"

    group1 = self.data[self.data[self.compliance_column] == 1][feature].dropna()
    group0 = self.data[self.data[self.compliance_column] == 0][feature].dropna()
    
    # KS test for group1
    mean1, std1 = np.mean(group1), np.std(group1)
    stat1, p_value1 = kstest(group1, 'norm', args=(mean1, std1))
    
    # KS test for group0
    mean0, std0 = np.mean(group0), np.std(group0)
    stat0, p_value0 = kstest(group0, 'norm', args=(mean0, std0))
    
    # Verbose output
    print(f"\n=== Kolmogorov-Smirnov Normality Test for {feature} ===")
    print(f"{group1_name} Results:")
    print(f"  KS Statistic: {stat1:.4f}")
    print(f"  P-Value: {p_value1:.4f}")
    if p_value1 > 0.05:
        print(f"  Conclusion: Fail to reject the null hypothesis. {group1_name} appears normally distributed.")
    else:
        print(f"  Conclusion: Reject the null hypothesis. {group1_name} does not appear normally distributed.")
    
    print(f"\n{group0_name} Results:")
    print(f"  KS Statistic: {stat0:.4f}")
    print(f"  P-Value: {p_value0:.4f}")
    if p_value0 > 0.05:
        print(f"  Conclusion: Fail to reject the null hypothesis. {group0_name} appears normally distributed.")
    else:
        print(f"  Conclusion: Reject the null hypothesis. {group0_name} does not appear normally distributed.")

def mann_whitney_test(self, feature, alternative='two-sided'):
    """
    Perform a Mann-Whitney U test with verbose output.

    Parameters:
        feature (str): Name of the feature to test.
        alternative (str): Alternative hypothesis ('two-sided', 'less', 'greater').
    """
    # Generate dynamic group names
    feature_name = feature.replace('_', ' ').title()
    group1_name = f"{feature_name} - Compliant"
    group0_name = f"{feature_name} - Non-Compliant"

    group1 = self.data[self.data[self.compliance_column] == 1][feature].dropna()
    group0 = self.data[self.data[self.compliance_column] == 0][feature].dropna()
    stat, p_value = mannwhitneyu(group1, group0, alternative=alternative)
    
    print(f"\n=== Mann-Whitney U Test for {feature} ===")
    print(f"Testing {group1_name} vs {group0_name} (Alternative Hypothesis: '{alternative}')")
    print(f"  U Statistic: {stat:.4f}")
    print(f"  P-Value: {p_value:.4f}")
    if p_value < 0.05:
        if alternative == 'two-sided':
            print(f"  Conclusion: Significant difference found between {group1_name} and {group0_name}.")
        elif alternative == 'less':
            print(f"  Conclusion: {group1_name} is significantly smaller (distribution-wise) than {group0_name}.")
        elif alternative == 'greater':
            print(f"  Conclusion: {group1_name} is significantly larger (distribution-wise) than {group0_name}.")
    else:
        print(f"  Conclusion: No significant difference found between {group1_name} and {group0_name}.")

def plot_side_by_side_kde(self, feature):
    """
    Generate side-by-side KDE plots for compliant and non-compliant groups with normal distribution overlays.

    Parameters:
        feature (str): Name of the feature to plot.
    """
    # Generate dynamic group names
    feature_name = feature.replace('_', ' ').title()
    group1_name = f"{feature_name} - Compliant"
    group0_name = f"{feature_name} - Non-Compliant"

    group1 = self.data[self.data[self.compliance_column] == 1][feature].dropna()
    group0 = self.data[self.data[self.compliance_column] == 0][feature].dropna()

    # Calculate mean and standard deviation for normal distribution overlay
    mean1, std1 = np.mean(group1), np.std(group1)
    mean0, std0 = np.mean(group0), np.std(group0)

    # Side-by-side plots
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Compliant group plot
    sns.kdeplot(group1, fill=True, label=f"{group1_name} Data", color="blue", alpha=0.6, ax=ax[0])
    x1 = np.linspace(mean1 - 4 * std1, mean1 + 4 * std1, 1000)
    ax[0].plot(x1, norm.pdf(x1, mean1, std1), label="Normal Distribution", color="red", linestyle="--")
    ax[0].set_title(f"{group1_name} Distribution with Normal Fit")
    ax[0].set_xlabel(feature)
    ax[0].set_ylabel("Density")
    ax[0].legend()

    # Non-compliant group plot
    sns.kdeplot(group0, fill=True, label=f"{group0_name} Data", color="orange", alpha=0.6, ax=ax[1])
    x0 = np.linspace(mean0 - 4 * std0, mean0 + 4 * std0, 1000)
    ax[1].plot(x0, norm.pdf(x0, mean0, std0), label="Normal Distribution", color="red", linestyle="--")
    ax[1].set_title(f"{group0_name} Distribution with Normal Fit")
    ax[1].set_xlabel(feature)
    ax[1].set_ylabel("Density")
    ax[1].legend()

    plt.tight_layout()
    plt.show()

def plot_combined_kde(self, feature):
    """
    Generate a single KDE plot showing both groups' distributions.

    Parameters:
        feature (str): Name of the feature to plot.
    """
    # Generate dynamic group names
    feature_name = feature.replace('_', ' ').title()
    group1_name = f"{feature_name} - Compliant"
    group0_name = f"{feature_name} - Non-Compliant"

    group1 = self.data[self.data[self.compliance_column] == 1][feature].dropna()
    group0 = self.data[self.data[self.compliance_column] == 0][feature].dropna()

    # Combined KDE plot
    plt.figure(figsize=(8, 6))
    sns.kdeplot(group1, label=f"{group1_name} Data", fill=True, color="blue", alpha=0.6)
    sns.kdeplot(group0, label=f"{group0_name} Data", fill=True, color="orange", alpha=0.6)
    plt.title(f"Combined KDE Plot for {feature} by Compliance")
    plt.xlabel(feature)
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.show()

    def test_feature(self, feature, alternative='two-sided'):
        """
        Perform all tests and visualizations for a specific feature.

        Parameters:
            feature (str): Name of the feature to test.
            alternative (str): Alternative hypothesis for the Mann-Whitney test.
        """
        print(f"\n=== Testing Feature: {feature} ===")
        self.ks_test_normality(feature)
        self.plot_side_by_side_kde(feature)
        self.mann_whitney_test(feature, alternative)
        self.plot_combined_kde(feature)
        self.summarize_stats(feature)