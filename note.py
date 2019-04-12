
import math

def spn2midi(n):
  """convert an SPN note to a MIDI note"""
  n = n.upper()
  x = list(n)
  if len(x) == 1:
    name = x[0]
    accidental = None
    octave = '0'
  elif len(x) == 2:
    name = x[0]
    accidental = None
    octave = x[1]
  elif len(x) == 3:
    name = x[0]
    accidental = x[1]
    octave = x[2]
  else:
    assert False, 'bad note length'
  # octave
  if octave in ('0','1','2','3','4','5','6','7','8'):
    # note: midi octave numbering is +1 on SPN octave numbering
    midi = (ord(octave) - ord('0') + 1) * 12
  else:
    assert False, 'bad octave number'
  # note
  if name in ('A','B','C','D','E','F','G'):
    idx = ord(name) - ord('A')
    midi += (9,11,0,2,4,5,7)[idx]
  else:
    assert False, 'bad note name'
  # accidental
  if accidental == '#':
    midi += 1
  elif accidental == 'B':
    midi -= 1
  elif accidental is not None:
    assert False, 'bad accidental name'
  return midi

def midi2spn(n):
  """convert a MIDI note to an SPN note"""
  return ''

def freq(n):
  """return the frequency of the (midi) note"""
  return 440.0 * math.pow(2.0, float(n - 69) / 12.0)

