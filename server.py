#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk.data

from train import load_classifier

logger = logging.getLogger('marlowe.redobject.server')
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def index():
    text = request.form.get('text')
    if text is not None:
        cl = load_classifier()
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
    app.run(debug=debug, host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))
