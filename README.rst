Introduction
============
collective.geo allows to geo-reference Plone content types and to display this information over a map.

collective.geo bundle is composed by the following packages:

`collective.geo.geographer <http://plone.org/products/collective.geo.geographer>`_
    provides geo annotation for Plone. `(repository) <https://github.com/collective/collective.geo.geographer>`_

`collective.geo.openlayers <http://plone.org/products/collective.geo.openlayers>`_
    enables openlayers machinery into Plone. `(repository) <https://github.com/collective/collective.geo.openlayers>`_

`collective.geo.settings <http://plone.org/products/collective.geo.settings>`_
    provides some utility to store settings of collective.geo packages. `(repository) <https://github.com/collective/collective.geo.settings>`_

`collective.geo.mapwidget <http://plone.org/products/collective.geo.mapwidget>`_
    provides some handy page macros and adapters to easily manage multiple maps on one page. `(repository) <https://github.com/collective/collective.geo.mapwidget>`_

`collective.geo.contentlocations <http://plone.org/products/collective.geo.contentlocations>`_
    provides a GUI for collective.geo.geographer. It provides some simple forms to add geographical coordinates to Plone content types. `(repository) <https://github.com/collective/collective.geo.contentlocations>`_

`collective.geo.kml <http://plone.org/products/collective.geo.kml>`_
    provides KML views for georeferenced objects, allowing Plone content types to be visualized in Google Earth. `(repository) <https://github.com/collective/collective.geo.kml>`_


To display the maps, **collective.geo** takes advantage of `Openlayers <http://www.openlayers.org>`_, a JavaScript library for displaying map data in web browsers, with no server-side dependencies.

As a default map source we can select `OpenStreetMap <http://www.openstreetmap.org/>`_, `Google Maps <http://maps.google.com>`_,  or `Bing Maps <http://www.bing.com/maps>`_.


.. image:: http://plone.org/products/collective.geo/screenshot

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

and run the buildout. Start Zope, go to Site Setup -> Add-on Products in your Plone site and install the Plone Maps (collective.geo) product.

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

.. image:: https://www.ohloh.net/p/collective_geo/widgets/project_partner_badge.gif
    :target: https://www.ohloh.net/p/collective_geo
