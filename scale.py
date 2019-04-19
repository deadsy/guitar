#!/usr/bin/env python3

import note

ionian = (2,2,1,2,2,2,1) # aka "major"
dorian = (2,1,2,2,2,1,2)
phrygian = (1,2,2,2,1,2,2)
lydian = (2,2,2,1,2,2,1)
mixolydian = (2,2,1,2,2,1,2)
aeolian = (2,1,2,2,1,2,2) # aka "natural minor"
locrian = (1,2,2,1,2,2,2)

class scale(object):

  def __init__(self, root, steps):
    self.root = note.spn2midi(root)
    self.steps = steps
    self.check()

  def check(self):
    """check the the scale has 12 steps in it"""
    n = 0
    for s in self.steps:
      n += s
    assert n == 12, 'total scale steps != 12'

  def gen_notes(self):
    """generate the set of midi notes making up the scale"""
    note = self.root
    # start at a root note < 0 so we have all possible midi notes
    while note > 0:
      note -= 12
    # step through the scale adding the notes
    notes = []
    i = 0
    while note < 128:
      if note >= 0:
        notes.append(note)
      note += self.steps[i]
      i += 1
      if i == len(self.steps):
        i = 0
    return notes

  def __str__(self):
    s = []
    s.append('%s: ' % note.midi2spn(self.root))
    s.append('%s' % str(self.steps))
    return ''.join(s)


class guitar_string(object):

  def __init__(self, n, frets):
    start = note.spn2midi(n)
    self.notes = range(start, start + frets)  

  def positions(self, notes):
    """return a string indicating the fret positions that are in the note set"""
    s = []
    # open string
    if self.notes[0] in notes:
      s.append('O|')
    else:
      s.append('X|')
    # fretted string
    for n in self.notes[1:]:
      if n in notes:
        s.append('--O|')
      else:
        s.append('---|')
    return ''.join(s)

if __name__ == '__main__':
  #s = scale('c', ionian)
  s = scale('a', aeolian)
  notes = s.gen_notes()
  #print(' '.join(note.midi2spn(n) for n in s.gen_notes()))
  frets = 19
  s = []
  s.append('    ')
  for i in range(1, frets):
    s.append('  %2d' % i)
  print(''.join(s))
  for n in ('e5', 'b4', 'g4', 'd4', 'a3', 'e3'):
    gs = guitar_string(n, frets)
    print('%s %s' % (n, gs.positions(notes)))
