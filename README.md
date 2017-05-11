# Marlowe Objectivity


[![wercker status](https://app.wercker.com/status/c99eaec92cfe7bf8bd10050fc568d62c/s/master "wercker status")](https://app.wercker.com/project/byKey/c99eaec92cfe7bf8bd10050fc568d62c)


This API uses a NaiveBayes approach trained on reddit comments to determine the relative objectivity of text.  This is an open source part of [Project Marlowe](https://github.com/iepathos/marlowe_devops)

JSON API Server accepts text and returns an objectivity score.

API hosted at [https://secure-basin-62593.herokuapp.com/](https://secure-basin-62593.herokuapp.com/)


## Testing
````shell
pip install -r requirements.txt
nose
````