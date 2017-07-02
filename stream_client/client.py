# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Flask
from flask import Response
from flask import request
from flask import json
from flask_api import status

import json
import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route('/get_time', methods=['GET'])
def salesforce():

	time_data = {}

	time_data['node_time'] = time.time()

	return Response(json.dumps(time_data), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9496)
