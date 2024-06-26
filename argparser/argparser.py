import argparse

class CustomArgumentParser(argparse.ArgumentParser):
  def __init__(self, *args, **kwargs):
    
    super().__init__(*args, **kwargs)
  
    self.add_argument(
      '--file',
      type=str,
      help='Path to csv file'
    )
    self.add_argument(
      '--city',
      type=str,
      help='city station '
    )
    self.add_argument(
      '--start',
      type=str,
      help='range start'
    )
    self.add_argument(
      '--end',
      type=str,
      help='range till'
    )
    self.add_argument(
      '--stats',
      type=str,
      help='the value i.e max/min '
    )
    self.add_argument(
      '--col',
      type=str,
      help='what to find '
    )
    