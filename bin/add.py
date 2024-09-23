#!/usr/bin/env python3

import hashlib
import os
import sys
import zlib

PYGIT_DIR = '.pygit'
OBJ_DIR = f'{PYGIT_DIR}/objects'
INDEX_PATH = f'{PYGIT_DIR}/index'

def generate_sha(contents):
  sha1_hash = hashlib.sha1()
  sha1_hash.update(contents)
  return sha1_hash.hexdigest()

def generate_blob(contents):
  return zlib.compress(contents)

def generate_sha_and_blob(file_path):
  with open(file_path, 'rb') as f:
    contents = f.read()
    sha  = generate_sha(contents)
    blob = generate_blob(contents)
    return sha, blob
  
def save_blob_to_objects_dir(sha, blob):
    obj_path  = os.path.join(OBJ_DIR, sha[:2])
    blob_path = os.path.join(obj_path, sha[2:])
    if os.path.exists(obj_path): return
    os.mkdir(obj_path)
    with open(blob_path, 'wb') as f:
      f.write(blob)

def add_entry_to_index(file_path, sha):
  with open(INDEX_PATH, 'a+') as f:
    f.write(f'{sha.ljust(20)} {file_path}\n')
  
def add(file_path):
  try:
    if not os.path.exists(file_path):
      raise FileNotFoundError(file_path)
    sha, blob = generate_sha_and_blob(file_path)
    save_blob_to_objects_dir(sha, blob)
    add_entry_to_index(file_path, sha)
  except FileNotFoundError as e:
    print(e)

def add_files():
  args = sys.argv[1:]
  for arg in args:
    add(arg)

if __name__ == '__main__':
  add_files()