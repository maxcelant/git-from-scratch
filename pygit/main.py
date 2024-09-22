import sys

USAGE = 'Usage: pygit <command> [<args>]'

def usage():
  print(USAGE)
  exit(1)

def main():
  try:
    cmd, args = sys.argv[1], sys.argv[2:] if sys.argv[2] else None
    print(cmd)
    print(args)
  except:  
    usage()

if __name__ == '__main__':
  main()