#!/usr/bin/env python3

import os

PYGIT_DIR = '.pygit'
OBJ_DIR = f'{PYGIT_DIR}/objects'
REFS_DIR = f'{PYGIT_DIR}/refs'

def init_head():
  with open(os.path.join(PYGIT_DIR, 'head'), 'w+') as f:
    f.write('ref: refs/heads/master')

def init_objects():
  os.mkdir(OBJ_DIR)
  os.mkdir(os.path.join(OBJ_DIR, 'info'))
  os.mkdir(os.path.join(OBJ_DIR, 'pack'))

def init_refs():
  os.mkdir(REFS_DIR)
  os.mkdir(os.path.join(REFS_DIR, 'heads'))
  os.mkdir(os.path.join(REFS_DIR, 'tags'))

def init_repository():
  if os.path.exists(PYGIT_DIR):
    print('Existing pygit project\n')
    exit(1)
  os.mkdir(PYGIT_DIR)
  init_head()
  init_objects()
  init_refs()
  print(f'Pygit initialized in {os.getcwd()}/{PYGIT_DIR}')

if __name__ == '__main__':
  init_repository()

