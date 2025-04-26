import pandas as pd


def risk_level(probability):
    bins = [0.0, 0.2, 0.5, 1.0]
    labels = ["It is unlikely that you are at risk of heart disease.",
              "It is possible that you are at risk of heart disease.",
              "It is likely that you are at risk of heart disease."]
    
    # Bin the probabilities into risk categories
    risk_category = pd.cut(probability, bins=bins, labels=labels, include_lowest=True)
    return risk_category[0]
