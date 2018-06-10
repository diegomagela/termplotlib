# -*- coding: utf-8 -*-
#
import numpy

import asciiplotlib as apl


def test_plot():
    x = numpy.linspace(0, 2 * numpy.pi, 10)
    y = numpy.sin(x)

    fig = apl.figure()
    fig.plot(x, y, title="data", width=50, height=15)
    string = fig.get_string()

    ref = """
    1 +---------------------------------------+
  0.8 |-+  **    +A*   +     +     +    +   +-|
  0.6 |-+ A         **           data ***A***-|
  0.4 |-**                                  +-|
  0.2 |*+             A*                    +-|
    0 |-+               **                  +-|
      |                                   A   |
 -0.2 |-+                 A*            **  +-|
 -0.4 |-+                   **         *    +-|
 -0.6 |-+                            *A     +-|
 -0.8 |-+   +    +     +     +A*** **   +   +-|
   -1 +---------------------------------------+
      0     1    2     3     4     5    6     7

"""

    assert string == ref
    return
