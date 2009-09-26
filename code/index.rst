================
 Software Tools
================

This page contains a collection of miscellaneous little software tools that
don't fit into any larger project but could be useful for someone.  Unless
otherwise specified, they are all released under the terms of the BSD license.

These days, I keep most new public projects available at my github_ repository,
which makes for a convenient download system and lets you send me back all the
great improvements you'll undoubtedly make.

.. _github: http://github.com/fperez


Python tools for Mathematica and Fortran
========================================

With Sage_ and Sympy_, I have much less of a need for Mathematica, but I've
previously needed to easily transfer quantities between Mathematica and Python.
If you have similar needs, you may find these tools useful (please drop me a
line if you do).

* A Mathematica notebook, `math2python.nb`_, defining functions to produce a
  Python module (meaning, valid, importable Python syntax) that contains
  variables from Mathematica.  It will export all numbers as floats and (even
  nested) lists as numpy arrays.

* A Python module, `py2mathematica.py`_ that does the opposite: it saves a list
  of Python variables to a valid Mathematica ``.m`` file, which can be loaded
  in Mathematica with the ``<<fname`` syntax.  This module is fairly well
  documented.

I also have on occasion needed to produce static Fortran tables of quantities
computed elsewhere.  Not so much from Python, but from Mathematica, and it
turned out to be much easier to use the above tools to do the Mathematica ->
Python conversion, and then generate valid Fortran from Python, than to
convince Mathematica to do the job (its string manipulation API, at least back
in version 5.0, was hideous beyond redemption).  If you ever need to generate
Fortran (77) from data you have in Python, then `py2fortran.py`_ may come in
handy.
  
.. _Sage: http://sagemath.org
.. _Sympy: http://code.google.com/p/sympy
.. _math2python.nb: math2python.nb
.. _py2mathematica.py: py2mathematica.py
.. _py2fortran.py: py2fortran.py


X11 keyboard control
====================

I recently modified and extended this `great little script`_ to control a
keyboard under X11.  My use for it is to take advantage of the special keys in
my Microsoft Wireless keyboards under Linux, so I can control XMMS, call up
Mozilla, Konqueror, gthumb, etc.

It's a simple module which you can find here_, and I call it via this_ little
script which you can modify for your particular usage case. It should be very
easy to customize it for any keyboard and any behavior you want.

Note that you'll need the `Xlib python`_ module.

.. links:

.. _great little script: http://www.larsen-b.com/Article/184.html
.. _here: x11kbd.py
.. _this: mskbd
.. _Xlib python: http://python-xlib.sourceforge.net


The attic: lyxport
==================

Today, LyX has very robust PDF export (and probably also HTML).  But that
wasn't the case in 2001, so I wrote this little tool in Perl called lyxport_
which managed to reliably produce valid PDF and HTML out of lyx or tex sources
better than LyX itself.

Today this code is probably of no interest, this is kept here mainly as a
curiosity and for archival purporses.  But it was my first open source tool
that saw some widespread use, and I learned a lot writing it even if the code
looks awful today, even for the dubious standards of Perl code.

.. _lyxport: lyxport/index.html

.. toctree::
   :hidden:

   lyxport/index
   