Introduction
============
collective.geo allows to geo-reference Plone content types and to display this information over a map.

collective.geo bundle is composed by the following packages:

`collective.geo.geographer <http://plone.org/products/collective.geo.geographer>`_
    provides geo annotation for Plone.

`collective.geo.openlayers <http://plone.org/products/collective.geo.openlayers>`_
    enables openlayers machinery into Plone.

`collective.geo.settings <http://plone.org/products/collective.geo.settings>`_
    provides some utility to store settings of collective.geo packages.

`collective.geo.mapwidget <http://plone.org/products/collective.geo.mapwidget>`_
    provides some handy page macros and adapters to easily manage multiple maps on one page.

`collective.geo.contentlocations <http://plone.org/products/collective.geo.contentlocations>`_
    provides a GUI for collective.geo.geographer. It provides some simple forms to add geographical coordinates to Plone content types.

`collective.geo.kml <http://plone.org/products/collective.geo.kml>`_
    provides KML views for georeferenced objects, allowing Plone content types to be visualized in Google Earth.


To display the maps, **collective.geo** takes advantage of `Openlayers <http://www.openlayers.org>`_, a JavaScript library for displaying map data in web browsers, with no server-side dependencies.

As a default map source we can select `OpenStreetMap <http://www.openstreetmap.org/>`_, `Google Maps <http://maps.google.com>`_, `Yahoo Maps <http://maps.yahoo.com/>`_ or `Bing Maps <http://www.bing.com/maps>`_.


.. image:: http://plone.org/products/collective.geo/screenshot

Requirements
------------

* libgeos_c (2.2.3 or 3.0.0+)
* `Shapely <http://trac.gispython.org/lab/wiki/Shapely>`_
* BeautifulSoup (geopy)
* geopy
* Plone >= 4.0
* zope.schema = 3.6.0 (z3c.form requirement)
* plone.app.z3cform
* `collective.geo.colorpicker <http://plone.org/products/collective.z3cform.colorpicker>`_


Installation
------------

Add collective.geo.bundle to your buildout's list of eggs such as::

    [buildout]
    ...
    eggs = 
        collective.geo.bundle
    ...

and run the buildout. Start Zope, go to Site Setup -> Add-on Products in your Plone site and install the Plone Maps (collective.geo) product.

You can find `a buildout example here <http://svn.plone.org/svn/collective/collective.geo.bundle/buildout/>`_


Contributors
------------
 * Giorgio Borelli - gborelli
 * Silvio Tomatis - silviot
 * Gerhard Weis - gweis
 * David Breitkreutz - rockdj
