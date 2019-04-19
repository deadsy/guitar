#!/usr/bin/env python3

import note

ionian = (2,2,1,2,2,2,1) # aka "major"
dorian = (2,1,2,2,2,1,2)
phrygian = (1,2,2,2,1,2,2)
lydian = (2,2,2,1,2,2,1)
mixolydian = (2,2,1,2,2,1,2)
aeolian = (2,1,2,2,1,2,2) # aka "natural minor"
locrian = (1,2,2,1,2,2,2)
harmonic_minor = (2,1,2,2,1,3,1)
melodic_minor = (2,1,2,2,2,2,1)

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


class guitar(object):

  def __init__(self, strings, frets):
    self.frets = frets
    self.string = []
    for n in strings:
      start = note.spn2midi(n)
      self.string.append(range(start, start + frets))

  def fretboard(self, scale):
    """return a string indicating the fret positions that are in the note set"""
    fb = []
    # fret numbering
    s = []
    s.append('    ')
    for i in range(1, self.frets):
      s.append('  %2d' % i)
    fb.append(''.join(s))
    # positions for each string
    for notes in self.string:
      s = []
      # open string
      if notes[0] in scale:
        s.append('O|')
      else:
        s.append('X|')
      # fretted string
      for n in notes[1:]:
        if n in scale:
          s.append('--O|')
        else:
          s.append('---|')
      fb.append('%s %s' % (note.midi2spn(notes[0]), ''.join(s)))
    return '\n'.join(fb)

if __name__ == '__main__':
  #s = scale('d', ionian)
  #s = scale('a', aeolian)
  #s = scale('b', melodic_minor)
  #s = scale('b', harmonic_minor)
  #s = scale('eb', lydian)
  s = scale('bb', dorian)
  g = guitar(('e5', 'b4', 'g4', 'd4', 'a3', 'e3'), 19)
  print(g.fretboard(s.gen_notes()))

