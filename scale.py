#!/usr/bin/env python3

scale_set = {}

class scale(object):

  def __init__(self, name, steps):
    global scale_Set
    self.name = name
    self.steps = steps
    scale_set[name] = self

  def check(self):
    n = 0
    for s in self.steps:
      n += s
    assert n == 12, 'total scale steps != 12'

  def __str__(self):
    s = []
    s.append('%s: ' % self.name)
    s.append('%s' % str(self.steps))
    return ''.join(s)

scale('ionian', (2,2,1,2,2,2,1))
scale('dorian', (2,1,2,2,2,1,2))
scale('phrygian', (1,2,2,2,1,2,2))
scale('lydian', (2,2,2,1,2,2,1))
scale('mixolydian', (2,2,1,2,2,1,2))
scale('aeolian', (2,1,2,2,1,2,2))
scale('locrian', (1,2,2,1,2,2,2))

def main():
  print('%s' % scale_set['ionian'])

main()
