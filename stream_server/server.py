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

nodes = []

#
#	Node:
#	{
#		"IP": IP Addr,
#		"Name": Name,
#		"InitialTime": Local time when request sent
#	}
#

@app.route('/add_node', methods=['POST'])
def salesforce():
	if request.headers['Content-Type'] == 'application/json':
		new_node = request.json['NewNode']

		for node in nodes:
			if node['IP'] = new_node['IP']:
				return Response("Node already exists in system", 403)

		nodes.append(new_node)

		return Response("Successfully added node with IP:" + str(new_node['IP'])), 200)
	else:
		return Response("Incorrect Header Type",417)

@app.route('/get_nodes', methods=['GET'])
def salesforce():
	data = {}
	data['Nodes'] = nodes

	return Response(json.dumps(data), 200)

@app.route('/clear_nodes', methods=['GET'])
def salesforce():
	del nodes[:]

	return Response("Nodes cleared", 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9694)
