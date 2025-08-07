from scipy.stats import fisher_exact


table = [[a, b],
         [c, d]]

oddsratio, p_value = fisher_exact(table, alternative='two-sided')
