import argparse

class ArgParser:

  def __init__(self):
    self.parser = argparse.ArgumentParser(description="A csv file!")
    self.__addArguments()
  
  def __addArguments(self):
    self.parser.add_argument(
      '-f', '--file',
      type=str,
      help='Path to csv file'
    )

  def parse_args(self):
    return self.parser.parse_args()