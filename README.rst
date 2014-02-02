Requirements
------------

* BeautifulSoup (geopy)
* geopy >=0.96.2
* Plone >= 4.1
* plone.app.z3cform
* `collective.z3cform.colorpicker <http://plone.org/products/collective.z3cform.colorpicker>`_ >= 1.1


Installation
------------

This addon can be installed has any other addons, please follow official
documentation_.

.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to


Upgrade
-------

To upgrade collective.geo go to in the Plone Site Setup > Addon.

When an upgrade is available a button will appear
next to Plone Maps (collective.geo) product.
Click the button to upgrade.


Dexterity
---------

`Dexterity <http://plone.org/products/dexterity>`_ support on collective.geo is provided by collective.geo.behaviour.

To include collective.geo.behaviour package when you install collective.geo, enable the "dexterity" extra::

    [buildout]
    ...
    eggs =
        collective.geo.bundle [dexterity]
    ...


Documentation
-------------

The package is documented at `collectivegeo.readthedocs.org <http://collectivegeo.readthedocs.org/>`_.
The sourcecode for this documentation resides in the docs folder of this
package, please contribute.


Contributors
------------

* Giorgio Borelli - gborelli
* Silvio Tomatis - silviot
* Gerhard Weis - gweis
* David Beitey - davidjb
* Adam Tang - adam139
* Christian Ledermann - cleder


Metrics
--------

.. image:: https://secure.travis-ci.org/collective/collective.geo.bundle.png
    :target: http://travis-ci.org/collective/collective.geo.bundle

.. image:: https://saucelabs.com/buildstatus/collectivegeo
    :target: https://saucelabs.com/u/collectivegeo

.. image:: https://www.ohloh.net/p/collective_geo/widgets/project_thin_badge.gif
    :target: https://www.ohloh.net/p/collective_geo
