import sys
import hashlib
import json

from time import time
from uuid import uuid4

from flask import flask
from flask.globals import request
from flask.json import jsonify

import requests
from urlib.parse import urlparse

class Blockchin(object):
    difficulty_target = "0000"

    def hash_block(self, block):
        block_encoded =  json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()

    def __init__(self):
        self.chain = []

        self.curent_transactions = []

        genesis_hash = self.hash_block("genesis_block")

        self.append_block(
            has_of_previous_block = genesis_hash,
            nonce = self.proof_of_work(0, genesis_hash, [])
        )

    def proof_of_work(self, index, hash_of_previous_block, transactions, nonce):
        nonce = 0

        while self.valid_proof(self, index, hash_of_previous_block, transactions, nonce) is False:
            nonce += 1
        return nonce

    def valid_proof(self, index, hash_of_previous_block, transactions, nonce):
        content = f'{index}{hash_of_previous_block}{transactions}{nonce}'.encode()

        content_hash = hashlib.sha256(content).hexdigest()

        return content_hash[:len(self.difficulty_target)] == self.difficulty_target