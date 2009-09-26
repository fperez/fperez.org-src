=============================================================
 Python for scientific computing: a personal list of "warts"
=============================================================

While I don't hide the fact that I love Python for scientific computing work,
obviously no tool is perfect.  I happen to think that Python is, *today*, the
best *compromise* we have available that combines the following features:

- Open source, cross-platform and functional on a wide number of platforms,
  including supercomputers and other HPC environments.

- A high-level, very expressive language with readable syntax, a clean object
  model and useful built-in data types (strings, lists, dictionaries,
  sets, ...).

- A rich general-purpose library with support for common non-numerical tasks:
  networking, regular expressions and other text processing, database access,
  process management, operating system level tasks (file and directory
  manipulations), etc.

- A sophisticated array object for manipulating homogeneous collections of
  numerical data in a Fortran-like manner.

- A well-defined foreign function interface, and machinery to easily call
  existing codes in C, C++ and Fortran.

- A good body of bindings to common tools needed in scientific work: 2d and 3d
  plotting, numerical libraries, etc.

- Support for interactive work, including execution, visualization and
  debugging.

- Tools for documentation of code and automatic testing.

On any one of the above it's probably easy to find a better tool than Python,
but on the combination, I don't think that today we have any better option.
Perhaps in 10 years things will be different.

In the meantime, I'll focus on making Python as good of a tool as possible for
my own research, and one important aspect of working with a tool you've become
used to, is not forgetting about its problems and limitations.  We often get so
accustomed to the little (or big) problems in the tools we use that we simply
integrate workarounds into our mental workflows, and stop being critical.  This
is the start of the fossilization of a project, and I hope that doesn't happen
to us on the scientific python front.  So I'm trying to ask myself often about
what significant problems we still have in using Python efficiently every day
for scientific work, and occasionally third-parties also ask me this.

After a recent such discussion took place over email, I decided to make this
little page to track this question.  This is meant to serve both as a reminder
to myself of these problems, and hopefully also as a list of ideas for new
contributors to jump in and help in areas that genuinely require improvement.
Please  `email me <Fernando.Perez@berkeley.edu>`_ with corrections, ideas for
working on any of this, or your own favorite problem.

Off the top of my head, here are a few of Python's "warts" for scientific work
that annoy me regularly:

- For purely linear-algebra based problems, matlab's syntax can be cleaner than
  numpy's (multiplication, \ operator, array creation, etc).

- Numpy's core object is the n-dimensional array, which is far more powerful
  than matlab's arrays, but can be more complex to master.

- Being a general language, it has multiple container types (sets, tuples,
  lists, n-dimensional arrays).  This flexibility can be daunting for the
  beginner and intermediate user who sometimes misuses them, though it is a
  huge benefit for more advanced algorithmic development.

- The machinery for distributing python packages is brittle, buggy and
  generally a major pain to use and extend.  There is currently (summer 2009)
  active work to address this; the core ideas are listed in Python's `PEP 376`_
  and Tarek Ziadé (the person leading much of this effort) recently put up a
  `post on his blog`_ about it all.
  
- The automated testing systems for python are currently a bit fragmented.
  Python ships with two (unittest_ and doctest_) but these lack critical
  functionality and ease of use, which has led to third-party systems like
  nose_, which isn't well integrated in the core.  It would be great to see a
  merge of the good ideas of nose into the core in a robust and stable way.
  
- The transition to Python 3 will cause some pain for a while, as the new
  version is not backwards compatible.

- There is no single-point-of-entry set of tools with unified documentation and
  help system for Python.  The remarkable Sage project (http://sagemath.org)
  does offer something like this and is an extremely valuable piece of this
  puzzle (I use it myself). Sage is a viable solution to this problem, though
  it actually goes beyond the pure python language by extending its syntax and
  modifying Python's core numerical type hierarchy.  But in pure python, there
  is nothing that currently integrates execution, development, debugging and
  documentation with the polish of Mathematica or Matlab.

- The main python implementation in C has a global lock that prevents
  multithreaded code from modifying python data structures.  So while python
  does support threads, they can only be used effectively for i/o bound tasks,
  not for cpu-bound ones.  Google's `Unladen Swallow`_ project aims to correct
  this, but we'll have to wait a few more months to see if it succeeds.  In the
  meantime, all parallel python code must use multiple processes, which can be
  a pain for certain valid use cases.
  
- There is currently no seamless way to get fast execution for numerical code
  that manually loops over arrays and does indexing operations on individual
  elements.  In recent years, Matlab has developed JIT technology to support
  this, and currently no seamless equivalent exists for Python.  Cython helps
  quite a bit on this front, but it's not yet 100% integrated into the system
  machinery (though rapid progress is being made).



.. _PEP 376: http://www.python.org/dev/peps/pep-0376/
.. _post on his blog: http://tarekziade.wordpress.com/2009/07/24/words-on-distribute-distutils-pep-376-pep-386-pep-345/
.. _unittest: http://docs.python.org/library/unittest.html#module-unittest
.. _doctest: http://docs.python.org/library/doctest.html#module-doctest
.. _nose: http://somethingaboutorange.com/mrl/projects/nose
.. _Unladen Swallow: http://code.google.com/p/unladen-swallow
