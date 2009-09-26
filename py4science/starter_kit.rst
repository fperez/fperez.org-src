================================================
 Python for scientific computing: a Starter Kit
================================================

This document is meant to gather resources for the scientist interested in
starting to use Python for scientific computing.  Most of the information here
should be of general use, though a few pointers are specific to resources at UC
Berkeley.  Please `email me <Fernando.Perez@berkeley.edu>`_ with feedback,
corrections or suggestions.

The landscape of Python tools for scientific computing is varied and rapidly
growing.  The Python language wasn't originally designed as a numerical
computing tool but instead as a general purpose, high level language.  For this
reason, as a scientist you will need to install a set of tools on top of the
basic language download to provide support for numerics, array manipulations,
numerical algorithms and data visualization.  All of the tools mentioned here
are free and developed as open source software in a collaborative manner by
other scientists; I encourage you to not only use these tools but to get
involved with the groups that develop them.  You will find not only help with
questions and problems, but likely also the opportunity to shape the
development of the major tools in a way that improves them for your own
research.


What to download
================

If you think of Python as a 'Matlab/IDL replacement', you probably want at the
very least (before you download any of these individually, continue reading
below):

- A basic interactive environment: IPython_ (disclosure: I'm biased since this
  is a project I started years ago, but many people seem to like it).

- Multidimensional array support: NumPy_ is the core library that most other
  scientific Python projects depend on and which allows it to efficiently
  manipulate large amounts of homogeneous numerical data in a manner similar to
  Matlab, IDL or any other array language.

- Linear algebra and other numerical libraries: SciPy_ is a set of libraries
  that add to NumPy access to all of LAPACK, FFTs, numerical integration,
  optimization, special functions, and much more.  This is a large combination
  of old and well known codes in C and FORTRAN (many from netlib_) with lots of
  new Python code both to expose those libraries and to provide new
  functionality.

- Data visualization: Matplotlib_ is my tool of choice for high quality 2d
  plotting (it recently also has developed basic 3d support), while Mayavi_ is
  a powerful system that builds on top of the VTK_ toolkit to provide
  sophisticated 3d visualization.

These are probably the raw basics, and a `community maintained page`_ at the
SciPy site lists a vast array of other tools you may find useful in your
specific problem domain, all of them free.

In terms of actually downloading and installing tools, there are a few
alternatives, partly depending on your operating system of choice:

- Linux: On most modern Linux distributions, the above tools (and many more)
  are one click or command away, though you might not get by default the very
  latest versions.  As a starting point you will probably be fine.

- The `Enthought Python Distribution`_ (EPD) is a self-contained installer with
  the above and many other tools.  EPD is a very easy solution that is
  particularly appealing for Windows and Mac OSX, and it also exists for
  several Linux distributions and Solaris.

- `Python(x,y)`_ provides a single-click installer for Windows of a similar set
  of libraries to EPD (though not exactly the same), as well as Ubuntu
  repositories.

As an alternative approach, the Sage_ project also ships most of these tools,
and then adds others (like GMP and Pari) to provide a new numerical foundation,
as well as its own original libraries for many tasks.  It also extends the
Python language syntax and modifies its core numerical type system with one
based on more structured mathematical abstractions (all integer arithmetic is
performed over the rationals, floating point numbers can always be arbitrary
precision ones, etc).  Sage provides a web-based interactive notebook
environment (as well as a customized IPython command-line one) but does not by
default build the graphical user interface components for Matplotlib and
Mayavi.  It's worth noting that since Sage has its own numerical type system
and matrix classes, by default most normal numpy/scipy examples will not work
in exactly the same way in Sage.  Depending on your needs, you can either use
the Sage notebook in 'pure python mode' where it will not load Sage's native
types, or use 'Sage mode' where its objects provide mathematical computing
capabilities not available in Python or NumPy.

Whether you choose to use the integrated Sage environment or the individual
libraries is up to you [#]_; I personally do most of my development on top of
'bare' Python using only the libraries I need for each problem, but I always
keep an updated Sage installation available and use it as needed.  Sage is
available in source and binary form for many different Unix-like operating
systems, and can be used in Windows as a VMWare Linux image.

.. _Sage: http://sagemath.org
.. _BSD: http://en.wikipedia.org/wiki/BSD_licenses
.. _GPL: http://en.wikipedia.org/wiki/GNU_General_Public_License

.. _IPython: http://ipython.scipy.org
.. _NumPy: http://numpy.scipy.org
.. _SciPy: http://www.scipy.org
.. _Matplotlib: http://matplotlib.sourceforge.net
.. _Mayavi: http://code.enthought.com/projects/mayavi
.. _Enthought Python Distribution: http://www.enthought.com/products/epd.php
.. _netlib: http://netlib.org
.. _VTK: http://vtk.org
.. _community maintained page: http://www.scipy.org/Topical_Software
.. _Python(x,y): http://www.pythonxy.com/foreword.php


What to read and view
=====================

Online resources
----------------

As a starting point, I recommend that people at the very least *work through*
(not just read, but actually type in and execute) the basic `Python tutorial
<http://docs.python.org/tutorial>`_, as well as the `introductory NumPy
tutorial <http://mentat.za.net/numpy/intro/intro.html>`_.

Note: in all of these, the markers that you see as ``>>>`` are the prompts
generated by Python which you do not type.  Similarly, the `IPython`_ prompts
look like ``In [3]:``.

In addition to these two minimal requirements, the following links can also be
useful:

- The NumPy `User Guide`_ and `Reference Guide`_: these are works in progress
  but they contain much useful information.

- The `Matplotlib manual <http://matplotlib.sourceforge.net/contents.html>`_:
  this is the Matlab-like plotting library most of us use regularly.

- The `IPython documentation <http://ipython.scipy.org/moin/Documentation>`_:
  handy resources about making the most of your interactive environment.

- The `SciPy documentation page <http://www.scipy.org/Additional_Documentation>`_ contains
  links to many more documentation resources, especially for scientific work.

- `Interactive data analysis
  <http://www.scipy.org/wikis/topical_software/Tutorial>`_: a tutorial with an
  astronomy focus but very useful for anyone dealing with data.  This is an
  *excellent resource* which you can download for reading but also with
  examples you can execute.

Books
-----

In terms of books for scientists, I recommend the following:

- `Beginning Python Visualization`_ by Shai Vaingast: this is a great practical
  introduction to numerical data processing and visualization.

- `Python Scripting for Computational Science`_ by Hans Petter Langtangen: a
  longer and denser but very comprehensive discussion of using Python in
  scientific computing contexts, available online from the author (`Amazon
  link`_).

The following Python books are freely available to UC Berkeley via the O'Reilly
Safari system.  These are books I have personally found to be useful and can
recommend; they are general-purpose books without content specific to
scientific use.

- `Learning Python, 3rd Edition
  <http://proquest.safaribooksonline.com/9780596513986>`_ by Mark Lutz.

- `Python Pocket Reference, 2nd Edition
  <http://proquest.safaribooksonline.com/0596001894>`_ by Mark Lutz.

- `Python in a Nutshell, 2nd Edition
  <http://proquest.safaribooksonline.com/0596100469>`_ by Alex Martelli.

- `Python Cookbook, 2nd Edition
  <http://proquest.safaribooksonline.com/0596007973>`_ by Alex Martelli; Anna
  Martelli Ravenscroft; David Ascher.

Note to Berkeley users: to access Safari for free, you need to be either on
campus or browsing with the `Berkeley Library Proxy
<http://lib.berkeley.edu/Help/proxy.html>`_.

Videos and webinars
-------------------

In late 2008 I taught an intensive 2-day workshop introducing Python to
scientific users at UC Berkeley.  While this was a very hands-on course and
thus probably not the best thing to watch as a recording, a number of people
have still told me that they find the lectures useful, all the `video is
available`_.  They were kindly videotaped and put online by Jeff Teeters.

Enthought offers a `webinar series`_ that is open to the public, and recordings
of past ones are available as well.

.. _User Guide:      http://docs.scipy.org/doc/numpy/user
.. _Reference Guide: http://docs.scipy.org/doc/numpy/reference
.. _Beginning Python Visualization: http://www.apress.com/book/view/9781430218432
.. _Python Scripting for Computational Science: http://folk.uio.no/hpl/scripting
.. _Amazon link: http://www.amazon.com/Python-Scripting-Computational-Science-Engineering/dp/3540739157/ref=sr_1_1?ie=UTF8&s=books&qid=1248306847&sr=8-1
.. _video is available: http://www.archive.org/search.php?query=Fernando+Perez+scientific+python
.. _webinar series: http://www.enthought.com/training/webinars.php


Where to get more help and information
======================================

All of the projects linked above have mailing lists that are very welcoming; I
have personally learned much from the discussions on these lists.  You will
find that very knowledgeable people are surprisingly generous with their time,
if you ask questions carefully and provide sufficient information to clearly
delineate your problem.  Simply click on each project's main page and you will
typically find an up-to-date link to its mailing lists.

The `Planet SciPy`_ blog aggregator is a useful way to keep in touch with what
many projects are doing.

Another excellent way to get in touch with what the developers of all these
tools are doing is to attend the annual SciPy conference_, which combines
teaching tutorials, formal presentations and development sprints.

If you are a UC Berkeley (or other Bay Area person for whom coming to campus is
feasible), I encourage you to stop by any of the regular `Py4Science meetings
on campus <https://cirl.berkeley.edu/view/Py4Science>`_.  This informal group
meets to discuss tools, problems and solutions regarding the use of Python in
scientific research; we have a very low-traffic `mailing list
<https://calmail.berkeley.edu/manage/list/listinfo/py4science@lists.berkeley.edu>`_
for meeting announcements that anyone can subscribe to.

.. _Planet SciPy: http://planet.scipy.org
.. _conference: http://conference.scipy.org

Acknowledgments
===============

Thanks to Chris Burns from UC Berkeley for a useful set of links and resources,
and to Stefan van der Walt from U. Stellenbosch for notes on Sage and numerics.


--------------

.. [#] One point that may be of importance to you in making this decision,
       depending on your context, is licensing.  Most of the tools I link to
       here are licensed in a BSD_ or similar manner, except for Sage which is
       GPL_ licensed.  Since Sage builds on a large foundation of other code
       that includes a mix of BSD and GPL tools, the combined Sage entity is
       necessarily also a GPL'd project.
       
