from sklearn.datasets import fetch_20newsgroups
categories = ["alt.atheism", "talk.religion.misc", "sci.space"]
data_train = fetch_20newsgroups(subset='train', shuffle=True, categories=categories)
data_test = fetch_20newsgroups(subset='test', shuffle=True, categories=categories)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vect = TfidfVectorizer()
X_train = tfidf_vect.fit_transform(data_train.data)
X_test = tfidf_vect.transform(data_test.data)
Y_train = data_train.target

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score

clf = MLPClassifier(solver="adam", learning_rate="constant", learning_rate_init=0.01, max_iter=1000, alpha=0.01)
clf.fit(X_train, Y_train)

predicted = clf.predict(X_test)
print("f1_score: %.2f" % f1_score(data_test.target, predicted, average="macro"))
print("accuracy_score: %.2f" % accuracy_score(data_test.target, predicted))
