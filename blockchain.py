import hashlib
import json
import time

def __init__(self):
  self.chain = []
  self.current_transactions = []
  self.new_block(previous_hash=1, proof=100)

def new_block(self, proof, previous_hash=None):
  block = {
    'index': len(self.chain) + 1,
    'timestamp': time(),
    'proof': proof,
    previous_hash: previous_hash or self.hash(self.chain[-1])
  }

  self.current_transactions = []
  self.chain.append(block)
  return block
  

def new_transaction(self):
  self.current_transactions.append({
    'sender': sender,
    'recipient': recipient,
    'amount': amount,
  })
  return self.last_block['index'] + 1

@staticmethod
def hash(block):
  """The follow code will create a SHA-256 block hash and also ensure that the dictionary is ordered"""
  block_string = json.dumps(block, sort_keys=True).encode()
  return hashlib.sha256(block_string).hexdigest()

@property
def last_block(self):
  return self.chain[-1]