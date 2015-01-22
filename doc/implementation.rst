Implementation
##############

Philosophy
----------

This particular implementation identifies three key groups:

* Persons who have previously never heard of EESTEC
* Persons who have some interest in EESTEC
* Persons who are associated with the association.

In particular this implementation does not strive to be any of the following:

* A recruitment portal for Commitments
* A place to reaffirm company and university representatives

It aims to provide useful content for these three groups, in particular a flashy homepage,
in depth information for interested parties, and a changed user interface to make it easier
for registered members to get to the content they are looking for.

Technical
---------

The system is implemented as a dynamic web service, or in laymen's terms a website. It
can be reached via a HTTP request and returns meaningful data in a HTTP_ response. The
content of the HTTP_ response depends on what was requested, and can be HTML_ , stylesheets_,
scripts_ or binary files like images.

Hosting
~~~~~~~

The web service is implemented as a Python_ program running on a Python_ webserver. The content that
users see is almost static over time ( this is not facebook ) and caching the HTTP_ responses yields
excellent performance even though in theory every request invokes the Python_ interpreter.

Processing of web requests is facilitated by the Django_ web framework

Static content (like this documentation) is served through an nginx_ webserver which serves the locations /static/,
/media/, and /doc/.


Security
~~~~~~~~

Connection
++++++++++

Our webserver is configured to run connections to https://eestec.net/ with an SSL_ encryption layer.
The particular security used for a particular connection depends on the capabilities of the user's browser.

Password storage
++++++++++++++++

By default, Django_ uses the PBKDF2_ algorithm with a SHA256_ hash, a password stretching mechanism recommended by NIST. This should be sufficient for most users: it’s quite secure, requiring massive amounts of computing time to break.
We do 12000 rounds and store our passwords with salt.

SQL injection protection
++++++++++++++++++++++++

By using Django_ querysets, the resulting SQL will be properly escaped by the underlying database driver. It is therefore impossible to launch an injection attack.

Cross site request forgery (CSRF) protection
++++++++++++++++++++++++++++++++++++++++++++

Django has built-in protection against most types of CSRF attacks and we use it.

Standards
~~~~~~~~~

The project tries to adhere to HTML5, CSS3 and Python PEP 8 standards.




.. _PBKDF2: http://en.wikipedia.org/wiki/PBKDF2
.. _SHA256: http://en.wikipedia.org/wiki/SHA-2
.. _Python: http://www.python.org
.. _HTTP: http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
.. _HTML: http://en.wikipedia.org/wiki/HTML
.. _nginx: http://www.nginx.org
.. _stylesheets: http://en.wikipedia.org/wiki/Cascading_Style_Sheets
.. _scripts: http://en.wikipedia.org/wiki/JavaScript
.. _Django: http://www.djangoproject.com
