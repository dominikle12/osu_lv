import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . linear_model import LogisticRegression
import sklearn
from sklearn . metrics import accuracy_score
from sklearn . metrics import confusion_matrix , ConfusionMatrixDisplay

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)


plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train,
            cmap='bwr', label='Training data', s=2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test,
            cmap='bwr', marker='x', label='Testing data', s=12)

LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)
y_test_p = LogRegression_model.predict(X_test)


w = LogRegression_model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (LogRegression_model.intercept_[0]) / w[1]

plt.plot(xx, yy, 'k-')

disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()

print (" Tocnost : " , accuracy_score ( y_test , y_test_p ) )
print (sklearn.metrics.classification_report(y_test , y_test_p))

plt.figure()
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test_p,
            cmap='bwr', marker='o', label='Testing data', s=12)

plt.show()
