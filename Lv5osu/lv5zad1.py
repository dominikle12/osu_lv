import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                           random_state=213, n_clusters_per_class=1, class_sep=1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=5)

xmin, xmax = -5, 5
ymin, ymax = -5, 5

xd = np.array([xmin, xmax])
yd = np.array([ymin, ymax])

plt.plot(xd, yd, 'k', lw=1, ls='--')
plt.fill_between(xd, yd, ymin, color='red', alpha=0.2)
plt.fill_between(xd, yd, ymax, color='blue', alpha=0.2)

plt.scatter(*X_train[y_train == 0].T, s=8, alpha=0.5, c='blue')
plt.scatter(*X_train[y_train == 1].T, s=8, alpha=0.5, c='red')
plt.scatter(*X_test[y_test == 0].T, s=8, alpha=0.5, c='blue', marker='x')
plt.scatter(*X_test[y_test == 1].T, s=8, alpha=0.5, c='red', marker='x')

plt.ylim(ymin, ymax)
plt.ylabel(r'$x_2$')
plt.xlabel(r'$x_1$')

plt.show()

LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)

b = LogRegression_model.intercept_[0]
w1, w2 = LogRegression_model.coef_.T
c = -b/w2
m = -w1/w2
yyd = m*xd + c

plt.plot(xd, yyd, linestyle='--')
plt.fill_between(xd, yyd, ymin, color='red', alpha=0.2)  # 1
plt.fill_between(xd, yyd, ymax, color='blue', alpha=0.2)  # 0

plt.scatter(*X_train[y_train == 0].T, s=8, alpha=0.5, c='blue')
plt.scatter(*X_train[y_train == 1].T, s=8, alpha=0.5, c='red')
plt.scatter(*X_test[y_test == 0].T, s=8, alpha=0.5, c='blue', marker='x')
plt.scatter(*X_test[y_test == 1].T, s=8, alpha=0.5, c='red', marker='x')
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

plt.ylim(ymin, ymax)
plt.ylabel(r'$x_2$')
plt.xlabel(r'$x_1$')
plt.show()

LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_test, y_test)

y_test_pred = LogRegression_model.predict(X_test)

print("Tocnost: ", accuracy_score(y_test, y_test_pred))

cm = confusion_matrix(y_test, y_test_pred)
print("Matrica zabune: ", cm)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_pred))
disp.plot()
plt.show()
print(classification_report(y_test, y_test_pred))

plt.scatter(*X_test[y_test == 0].T, s=8, alpha=0.5, c='blue', marker='x')
plt.scatter(*X_test[y_test == 1].T, s=8, alpha=0.5, c='red', marker='x')

plt.ylabel(r'$x_2$')
plt.xlabel(r'$x_1$')
plt.show()

