#!/usr/bin/env python3.2

# edrn
#
# Editor-assisted rename. Passes a list of filenames to the
# standard editor for easy mass renaming.
#
# Copyright 2012 Sijmen Mulder <sjmulder@gmail.com>.
# Licensed under the 3-claused BSD licence.

import os
import sys
import tempfile
import subprocess

if __name__ == '__main__':
  filenames = sys.argv[1:]
  if len(filenames) < 1:
    print('edrn: usage: edrn <filenames>', file=sys.stderr)
    sys.exit(1)
  editor = os.environ.get('EDITOR', 'vim')
  with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt') as handle:
    for filename in filenames:
      print(filename, file=handle)
    handle.flush()
    if os.system(editor + ' ' + handle.name) != 0:
      system.exit(0)
    with open(handle.name, 'r') as infile:
      new_filenames = [fn.rstrip('\n') for fn in infile.readlines()]
  if len(new_filenames) != len(filenames):
    print('edrn: different number of filenames, aborting', file=sys.stderr)
    sys.exit(1)
  for old_filename, new_filename in zip(filenames, new_filenames):
    print(old_filename + ' -> ' + new_filename)
    os.rename(old_filename, new_filename)
