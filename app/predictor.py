import numpy as np


def predict(features, model):
    array = np.array(features).reshape(1, -1)
    prediction = model.predict(array)[0]
    return int(prediction)