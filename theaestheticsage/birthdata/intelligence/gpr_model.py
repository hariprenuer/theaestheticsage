import numpy as np
from datetime import datetime, timedelta
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def date_to_ordinal(d):
    return parse_date(d).toordinal()

def ordinal_to_date(o):
    return datetime.fromordinal(o).strftime("%Y-%m-%d")

def gpr_adjusted_curve(original_data, edited_points, x_range, step=1):
    # Convert date strings to ordinal numbers
    def to_xy(data):
        X = np.array([date_to_ordinal(d["date"]) for d in data]).reshape(-1, 1)
        y = np.array([d["value"] for d in data])
        return X, y

    X_orig, y_orig = to_xy(original_data)
    start_ord = date_to_ordinal(x_range[0])
    end_ord = date_to_ordinal(x_range[1])
    x_pred_ord = np.arange(start_ord, end_ord + 1, step).reshape(-1, 1)

    # Original curve GP
    gpr_orig = GaussianProcessRegressor(
        kernel=RBF(length_scale=60.0) + WhiteKernel(noise_level=1.0),
        normalize_y=True
    )
    gpr_orig.fit(X_orig, y_orig)
    y_orig_pred = gpr_orig.predict(x_pred_ord)

    # If no edits, return the original curve
    if not edited_points:
        return [{"date": ordinal_to_date(int(x[0])), "value": float(y)} for x, y in zip(x_pred_ord, y_orig_pred)]

    # Edited GP
    X_edit, y_edit = to_xy(edited_points)
    gpr_edit = GaussianProcessRegressor(
        kernel=RBF(length_scale=10.0) + WhiteKernel(noise_level=0.1),
        normalize_y=True
    )
    gpr_edit.fit(X_edit, y_edit)
    y_edit_pred = gpr_edit.predict(x_pred_ord)

    # Blend using Gaussian weights around edit points
    weights = np.zeros(len(x_pred_ord))
    for x_e in X_edit.flatten():
        weights += np.exp(-0.5 * ((x_pred_ord.flatten() - x_e) / 20) ** 2)
    weights = np.clip(weights / np.max(weights), 0, 1)

    # Final blend
    y_blend = (1 - weights) * y_orig_pred + weights * y_edit_pred

    return [{"date": ordinal_to_date(int(x[0])), "value": float(y)} for x, y in zip(x_pred_ord, y_blend)]
