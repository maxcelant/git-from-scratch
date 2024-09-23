#!/usr/bin/env python3

import hashlib
import os
import sys
import zlib

PYGIT_DIR = '.pygit'
OBJ_DIR = f'{PYGIT_DIR}/objects'

def generate_sha(contents):
  sha1_hash = hashlib.sha1()
  sha1_hash.update(contents)
  return sha1_hash.hexdigest()

def generate_blob(contents):
  return zlib.compress(contents)

def generate_sha_and_blob(file):
  with open(file, 'rb') as f:
    contents = f.read()
    sha  = generate_sha(contents)
    blob = generate_blob(contents)
    return sha, blob
  
def save_blob_to_objects_dir(sha, blob):
    obj_path  = os.path.join(OBJ_DIR, sha[:2])
    blob_path = os.path.join(obj_path, sha[2:])
    os.mkdir(obj_path)
    with open(blob_path, 'wb') as f:
      f.write(blob)
  
def add(file):
  try:
    if not os.path.exists(file):
      raise FileNotFoundError(file)
    sha, blob = generate_sha_and_blob(file)
    save_blob_to_objects_dir(sha, blob)
  except FileNotFoundError as e:
    print(e)

def add_files():
  args = sys.argv[1:]
  for arg in args:
    add(arg)

if __name__ == '__main__':
  add_files()