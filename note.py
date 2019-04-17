
import math

def spn2midi(n):
  """convert an SPN note to a MIDI note"""
  n = n.upper()
  name = n[0]
  if len(n) == 1:
    accidental = None
    octave = 0
  elif len(n) == 2:
    if n[1] in ('#', 'B'):
      accidental = n[1]
      octave = 0
    else:
      accidental = None
      octave = int(n[1])
  else:
    if n[1] in ('#', 'B'):
      accidental = n[1]
      octave = int(n[2:])
    else:
      accidental = None
      octave = int(n[1:])
  # octave
  # Note: C5 = midi 60 == middle-C
  midi = octave * 12
  # note
  assert name in ('A', 'B', 'C', 'D', 'E', 'F', 'G'), 'bad note name'
  idx = ord(name) - ord('A')
  midi += (9, 11, 0, 2, 4, 5, 7)[idx]
  # accidental
  if accidental:
    assert accidental in ('#', 'B'), 'bad accidental name'
    midi += (-1, 1)[accidental == '#']
  return midi

notesInOctave = 12
sharpNotes = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
flatNotes = ("C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B")

def midi2spn(n, flat=False):
  """convert a MIDI note to an SPN note"""
  if flat:
    s = flatNotes[n % notesInOctave]
  else:
    s = sharpNotes[n % notesInOctave]
  octave = int(n / notesInOctave)
  return '%s%d' % (s, octave)

def freq(n):
  """return the frequency of the (midi) note"""
  return 440.0 * math.pow(2.0, float(n - 69) / 12.0)

if __name__ == "__main__":
  tests = (
    (21, 'A1'),
    (60, 'C5'),
    (67, 'G5'),
    (69, 'A5'),
    (88, 'E7'),
    (108, 'C9'),
  )
  for (n, s) in tests:
    sx = midi2spn(n)
    if sx != s:
      print("failed midi2spn(%d) != %s (got %s)" % (n, s, sx))
    nx = spn2midi(s)
    if nx != n:
      print("failed spn2midi(%s) != %d (got %d)" % (s, n, nx))
    for i in range(128):
      s = midi2spn(i, flat=True)
      nx = spn2midi(s)
      assert i == nx, "%d -> %s -> %d" % (i, s, nx)
