Requirements
------------

* BeautifulSoup (geopy)
* geopy
* Plone >= 4.0
* zope.schema = 3.6.0 (z3c.form requirement)
* plone.app.z3cform
* `collective.z3cform.colorpicker <http://plone.org/products/collective.z3cform.colorpicker>`_


Installation
------------

Add collective.geo.bundle to your buildout's list of eggs such as::

    [buildout]
    ...
    eggs =
        collective.geo.bundle
    ...

and run the buildout.

Start Zope, go to Site Setup -> Add-on Products in your Plone site and install the Plone Maps (collective.geo) product.

Documentation
-------------

The package is documented at `collectivegeo.readthedocs.org <http://collectivegeo.readthedocs.org/>`_.
The sourcecode for this documentation resides in the docs folder of this
package, please contribute.


Bug Reports
-----------

* `<https://github.com/collective/collective.geo.bundle/issues/>`_


Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/collective.geo.bundle.png
    :target: http://travis-ci.org/collective/collective.geo.bundle


Contributors
------------

* Giorgio Borelli - gborelli
* Silvio Tomatis - silviot
* Gerhard Weis - gweis
* David Beitey - davidjb
* Adam Tang - adam139
* Christian Ledermann - cleder
