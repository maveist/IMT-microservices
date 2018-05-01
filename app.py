import os

from flask import Flask, request, render_template
import requests

import settings

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def hello():
    return "Hello World "+request.args.get('test', 'nono')


@app.route("/boutons", methods=['GET'])
def boutons():
    payload = {'demandeType': request.args.get('demandeType', '')}
    r = requests.get(settings.URL_CONFIG, params=payload)
    vote_options = r.json()
    demande_id = request.args.get('demandeId')
    return render_template('buttons.html', vote_options=vote_options["voteOptions"], url_vote=settings.URL_VOTE,
                           demande_id=demande_id)
