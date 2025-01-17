import numpy as np
from scipy.stats import kstest, norm, mannwhitneyu
import matplotlib.pyplot as plt
import seaborn as sns


def ks_test_normality(group1, group0, group1_name="Compliant Group", group0_name="Non-Compliant Group"):
    """
    Perform KS tests for normality on two groups and visualize their distributions side by side.

    Parameters:
        group1 (array-like): Data for the first group. Must be 1-dimensional.
        group0 (array-like): Data for the second group. Must be 1-dimensional.
        group1_name (str, optional): Name of the first group for labeling purposes. Default is "Compliant Group".
        group0_name (str, optional): Name of the second group for labeling purposes. Default is "Non-Compliant Group".

    Returns:
        None: Displays the KS test results and visualizes the distributions.

    Notes:
        - Assumes the input groups are continuous variables.
        - The test checks if the data in each group follows a normal distribution.

    Example:
        >>> import numpy as np
        >>> from scipy.stats import norm
        >>> group1 = np.random.normal(loc=5, scale=1, size=100)
        >>> group0 = np.random.normal(loc=3, scale=1.5, size=100)
        >>> ks_test_normality(group1, group0, group1_name="Group A", group0_name="Group B")
    """
    # Validate input dimensions
    if not np.ndim(group1) == 1 or not np.ndim(group0) == 1:
        raise ValueError("Both group1 and group0 must be 1-dimensional arrays.")
    
    # Perform KS test for group1
    mean1, std1 = np.mean(group1), np.std(group1)
    stat1, p_value1 = kstest(group1, 'norm', args=(mean1, std1))
    
    # Perform KS test for group0
    mean0, std0 = np.mean(group0), np.std(group0)
    stat0, p_value0 = kstest(group0, 'norm', args=(mean0, std0))
    
    # Print results
    print(f"{group1_name} KS Test for Normality:")
    print(f"KS Statistic: {stat1:.4f}, P-Value: {p_value1:.4f}")
    if p_value1 > 0.05:
        print(f"Fail to reject the null hypothesis: {group1_name} is normally distributed.\n")
    else:
        print(f"Reject the null hypothesis: {group1_name} is not normally distributed.\n")
    
    print(f"{group0_name} KS Test for Normality:")
    print(f"KS Statistic: {stat0:.4f}, P-Value: {p_value0:.4f}")
    if p_value0 > 0.05:
        print(f"Fail to reject the null hypothesis: {group0_name} is normally distributed.\n")
    else:
        print(f"Reject the null hypothesis: {group0_name} is not normally distributed.\n")
    
    # Plotting side by side
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    
    # Group 1 Plot
    sns.kdeplot(group1, fill=True, label=f"{group1_name} Data", color="blue", alpha=0.6, ax=ax[0])
    x1 = np.linspace(mean1 - 4*std1, mean1 + 4*std1, 1000)
    ax[0].plot(x1, norm.pdf(x1, mean1, std1), label="Normal Distribution", color="red", linestyle="--")
    ax[0].set_title(f"{group1_name} Distribution with Normal Fit")
    ax[0].set_xlabel("Values")
    ax[0].set_ylabel("Density")
    ax[0].legend()
    
    # Group 0 Plot
    sns.kdeplot(group0, fill=True, label=f"{group0_name} Data", color="orange", alpha=0.6, ax=ax[1])
    x0 = np.linspace(mean0 - 4*std0, mean0 + 4*std0, 1000)
    ax[1].plot(x0, norm.pdf(x0, mean0, std0), label="Normal Distribution", color="red", linestyle="--")
    ax[1].set_title(f"{group0_name} Distribution with Normal Fit")
    ax[1].set_xlabel("Values")
    ax[1].set_ylabel("Density")
    ax[1].legend()
    
    plt.tight_layout()
    plt.show()


def mann_whitney_test(group1, group0, alternative='two-sided', group1_name="Compliant", group0_name="Non-Compliant"):
    """
    Perform a Mann-Whitney U test between two groups, produce a verbose output,
    and visualize the distributions with KDE plots.

    Parameters:
        group1 (array-like): Data for the first group (e.g., compliant cases). Must be 1-dimensional.
        group0 (array-like): Data for the second group (e.g., non-compliant cases). Must be 1-dimensional.
        alternative (str, optional): Defines the alternative hypothesis. Options are:
            - 'two-sided' (default): Tests for a difference in distributions.
            - 'less': Tests if group1 is stochastically less than group0.
            - 'greater': Tests if group1 is stochastically greater than group0.
        group1_name (str, optional): Label for the first group. Default is "Compliant".
        group0_name (str, optional): Label for the second group. Default is "Non-Compliant".

    Returns:
        None: Displays the Mann-Whitney U test results and visualizes the distributions.

    Notes:
        - Assumes the input groups are continuous variables.
        - Does not assume normality of the data.

    Example:
        >>> import numpy as np
        >>> group1 = np.random.normal(loc=5, scale=1, size=100)
        >>> group0 = np.random.normal(loc=3, scale=1.5, size=100)
        >>> mann_whitney_test(group1, group0, alternative='greater', group1_name="Group A", group0_name="Group B")
    """

    # Validate input dimensions
    if not np.ndim(group1) == 1 or not np.ndim(group0) == 1:
        raise ValueError("Both group1 and group0 must be 1-dimensional arrays.")
    
    # Perform the Mann-Whitney U test
    stat, p_value = mannwhitneyu(group1, group0, alternative=alternative)
    
    # Print a detailed report
    print(f"=== Mann-Whitney U Test Results ===")
    print(f"Testing Distribution of {group1_name} vs {group0_name}")
    print(f"Alternative Hypothesis: '{alternative}'")
    print(f"U Statistic: {stat:.4f}")
    print(f"P-Value: {p_value:.4f}")
    
    # Interpret results
    if p_value < 0.05:
        if alternative == 'two-sided':
            print(f"Conclusion: There is a significant difference between {group1_name} and {group0_name}.")
        elif alternative == 'less':
            print(f"Conclusion: {group1_name} is significantly smaller (distribution-wise) than {group0_name}.")
        elif alternative == 'greater':
            print(f"Conclusion: {group1_name} is significantly larger (distribution-wise) than {group0_name}.")
    else:
        print(f"Conclusion: No significant difference found between {group1_name} and {group0_name}.")

def plot_kde_with_groups(group1, group0, group1_name="Group 1", group0_name="Group 0", title="Distribution by Group", xlabel="Values", ylabel="Density"):
    """
    Plot KDE for two groups with labeled distributions.

    Parameters:
        group1 (array-like): Data for the first group. Must be 1-dimensional.
        group0 (array-like): Data for the second group. Must be 1-dimensional.
        group1_name (str, optional): Name of the first group for labeling purposes. Default is "Group 1".
        group0_name (str, optional): Name of the second group for labeling purposes. Default is "Group 0".
        title (str, optional): Title of the plot. Default is "Distribution by Group".
        xlabel (str, optional): Label for the x-axis. Default is "Values".
        ylabel (str, optional): Label for the y-axis. Default is "Density".

    Returns:
        None: Displays the KDE plot for the two groups.

    Example:
        >>> import numpy as np
        >>> group1 = np.random.normal(loc=5, scale=1, size=100)
        >>> group0 = np.random.normal(loc=3, scale=1.5, size=100)
        >>> plot_kde_with_groups(group1, group0, group1_name="Group A", group0_name="Group B")
    """
    # Validate input dimensions
    if not np.ndim(group1) == 1 or not np.ndim(group0) == 1:
        raise ValueError("Both group1 and group0 must be 1-dimensional arrays.")
    
    # Create the KDE plot
    sns.kdeplot(group1, label=group1_name, fill=True, color="blue", alpha=0.6)
    sns.kdeplot(group0, label=group0_name, fill=True, color="orange", alpha=0.6)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()