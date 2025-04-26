def get_predictions(model, input_data):

    # returns the probability for both classes
    probabilities = model.predict_proba(input_data)

    # Probability for heart disease
    probability_heart_disease = probabilities[:, 1]

    return probability_heart_disease
