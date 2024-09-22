import sys
import os
import subprocess

USAGE = 'Usage: pygit <command> [<args>]'

class InvalidCommandException(Exception):
    def __init__(self, command):
        self.command = command
        self.message = f"'{self.command}' is not a valid command."
        super().__init__(self.message)

def usage():
  print(USAGE)

def main():
  try:
    cmd, args = sys.argv[1], sys.argv[2:] if len(sys.argv) > 2 else []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_command = os.path.join(script_dir, "bin", f"{cmd}.py")
    if not os.path.exists(path_to_command):
      raise InvalidCommandException(cmd)
    subprocess.run([path_to_command, *args])
  except Exception as e:
    print(e)
    usage()

if __name__ == '__main__':
  main()