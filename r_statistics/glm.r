model <- glm(pcnt ~ Year, data = df, weights=All, family = binomial)
