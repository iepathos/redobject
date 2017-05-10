#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk.data
from textblob.classifiers import NaiveBayesClassifier

logger = logging.getLogger('marlowe.objectivity.server')

app = Flask(__name__)
CORS(app)


with open('dataset/objectivity.json', 'r') as fp:
    # split data to train and test data, going with 80/20 to start
    dataset = json.load(fp)

    train_data = dataset[int(len(dataset) * .2):]
    test_data = dataset[:int(len(dataset) * .2)]
cl = NaiveBayesClassifier(train_data)


@app.route('/', methods=['POST'])
def index():
    text = request.form.get('text')
    if text is not None:
        # split into sentences, evaluate each sentence, then average the scores
        # the classifier and dataset is by sentence so best to only give
        # it one sentence at a time
        text = str(request.form.get('text').encode("utf8")).strip()
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(text)
        scores = []
        for s in sentences:
            prob_dist = cl.prob_classify(s)
            objectivity = float(round(prob_dist.prob("objective"), 2))
            scores.append(objectivity)
        average = sum(scores) / len(scores)
        data = {'objectivity': round(average, 2)}
    else:
        data = {'objectivity': 1.0}
    return jsonify(data)


if __name__ == '__main__':
    debug = os.environ.get('DEBUG')
    if debug is not None:
        debug = True
    else:
        debug = False
    app.run(debug=debug, host='0.0.0.0')
