import pandas as pd
import shap

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv(
    "final_feature_engineered_churn.csv"
)

X = df.drop(
    "Churn",
    axis=1
)

y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier(
    eval_metric="logloss"
)

model.fit(
    X_train,
    y_train
)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)

shap.summary_plot(
    shap_values,
    X_test
)