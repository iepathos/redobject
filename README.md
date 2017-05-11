# Marlowe Objectivity


[![wercker status](https://app.wercker.com/status/87bd743ddc37806e1b9171071d727b59/s/master "wercker status")](https://app.wercker.com/project/byKey/87bd743ddc37806e1b9171071d727b59)


This API uses a NaiveBayes approach trained on reddit comments to determine the relative objectivity of text.  This is an open source part of [Project Marlowe](https://github.com/iepathos/marlowe_devops)

JSON API Server accepts text and returns an objectivity score.

API hosted at [https://secure-basin-62593.herokuapp.com](https://secure-basin-62593.herokuapp.com)


## Testing
````shell
pip install -r requirements.txt
nose
````