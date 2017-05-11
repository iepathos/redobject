#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pickle
import logging
from textblob.classifiers import NaiveBayesClassifier

logger = logging.getLogger('marlowe.redobject.train')


def save_classifier(classifier):
    f = open('objectivity_classifier.pickle', 'wb')
    pickle.dump(classifier, f, -1)
    f.close()


def load_classifier():
    f = open('objectivity_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier


logger.warning('Loading objectivity dataset')
with open('../dataset/objectivity.json', 'r') as fp:
    # split data to train and test data, going with 80/20 to start
    dataset = json.load(fp)
    train_data = dataset[int(len(dataset) * .2):]
    test_data = dataset[:int(len(dataset) * .2)]
logger.warning('Loaded dataset, training classifier')
logger.warning('Length of training data %s' % len(train_data))
cl = NaiveBayesClassifier(train_data)
cl.accuracy(test_data)

save_classifier(cl)
