#!/usr/bin/env python3

import math
import note

GRAMS = 0.001
MM = 0.001
MM_PER_INCH = 25.4
INCHES = MM_PER_INCH * MM
GRAV = 9.807
LBS_PER_KG = 2.20462

class gstring(object):

  def __init__(self, name, gauge, weight, length):
    self.name = name
    self.gauge = gauge
    # linear density
    self.ldensity = float(weight) / float(length)
    # volume density
    d = (MM_PER_INCH * (gauge / 1000.0)) * MM
    r = 0.5 * d
    a = math.pi * r * r
    self.vdensity = float(weight) / (float(length) * a)

  def f_string(self, l, t):
    """return the frequency (Hz) of a plucked string"""
    # l = string length (m)
    # t = string tension (N)
    return math.sqrt(t / self.ldensity) / (2.0 * l)

  def t_string(self, l, f):
    """return the tension (N) of a plucked string"""
    # l = string length (m)
    # f = string frequency (Hz)
    return 4.0 * self.ldensity * l * l * f * f

  def __str__(self):
    return '%s (%d)' % (self.name, self.gauge)


def string_setup(s, l, n):
  f = note.freq(note.spn2midi(n))
  x = []
  x.append(str(s))
  x.append(n)
  x.append('%.2fHz' % f)
  x.append('%.2fN' % s.t_string(l, f))
  return ' '.join(x)

def main():

  s0 = gstring('EB1146', 46, (7.306 - 0.166) * GRAMS, 1.0) # E3
  s1 = gstring('EB1136', 36, (4.570 - 0.166) * GRAMS, 1.0) # A3
  s2 = gstring('EB1126', 26, (2.539 - 0.166) * GRAMS, 1.0) # D4
  s3 = gstring('EB1017', 17, (1.340 - 0.166) * GRAMS, 1.0) # G4
  s4 = gstring('EB1013', 13, (0.859 - 0.166) * GRAMS, 1.0) # B4
  s5 = gstring('EB1010', 10, (0.571 - 0.166) * GRAMS, 1.0) # E5

  d = 25.0 * INCHES

  print('standard 6-string tuning')
  print(string_setup(s0, d, 'e3'))
  print(string_setup(s1, d, 'a3'))
  print(string_setup(s2, d, 'd4'))
  print(string_setup(s3, d, 'g4'))
  print(string_setup(s4, d, 'b4'))
  print(string_setup(s5, d, 'e5'))


  print('open G 3-string options')
  print(string_setup(s1, d, 'g3'))
  print(string_setup(s3, d, 'g4'))
  print(string_setup(s5, d, 'g5'))
  print(string_setup(s2, d, 'd4'))
  print(string_setup(s5, d, 'd5'))


main()


