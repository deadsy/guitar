#!/usr/bin/env python3

import note

class scale(object):

  def __init__(self, root, steps):
    self.spn = root
    self.midi = note.spn2midi(root)
    self.steps = steps
    self.check()

  def check(self):
    n = 0
    for s in self.steps:
      n += s
    assert n == 12, 'total scale steps != 12'

  def __str__(self):
    s = []
    s.append('%s: ' % self.spn)
    s.append('%s' % str(self.steps))
    return ''.join(s)

ionian = (2,2,1,2,2,2,1)
dorian = (2,1,2,2,2,1,2)
phrygian = (1,2,2,2,1,2,2)
lydian = (2,2,2,1,2,2,1)
mixolydian = (2,2,1,2,2,1,2)
aeolian = (2,1,2,2,1,2,2)
locrian = (1,2,2,1,2,2,2)

def main():
  print('%s' % scale('c', ionian))

main()
