from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

X,Y = make_classification(n_samples=1000,n_features=10,n_classes=2,random_state=42)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y ,random_state=42)


clf = Perceptron(
    max_iter = 1000,
    eta0 = 0.1,
    random_state=42,
    tol=1e-3,
    shuffle=True
)

clf.fit(X_train,Y_train)
accuracy = clf.score(X_test,Y_test)
print(f"Accuracy is {accuracy}")