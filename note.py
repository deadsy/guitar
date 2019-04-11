
import math

class note(object):

  def __init__(self, n):
    pass

  def from_midi(self, n):
    """create a note from an MIDI note"""
    self.midi = n

  def from_spn(self, n):
    """create a note from an SPN name"""
		n = n.upper()
		x = list(n)
		if len(x) == 2:
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
		self.midi = midi

  def spn(self):
    """return a string for the SPN name"""
    return ''

  def freq(self):
    """return the frequency of the note"""
    return 440.0 * math.pow(2.0, float(self.midi - 69) / 12.0)

  def __str__(self):
    return '%s(%d)' % (self.spn(), self.midi)

