Overview
========

collective.geo allows to geo-reference Plone content types and to display this information over a map.

The core of collective geo is composed by the following packages:

`collective.geo.geographer <http://plone.org/products/collective.geo.geographer>`_
    provides geo annotation for Plone. `(repository) <https://github.com/collective/collective.geo.geographer>`__

`collective.geo.openlayers <http://plone.org/products/collective.geo.openlayers>`_
    enables openlayers machinery into Plone. `(repository) <https://github.com/collective/collective.geo.openlayers>`__

`collective.geo.settings <http://plone.org/products/collective.geo.settings>`_
    provides some utilities where settings of collective.geo packages can be stored `(repository) <https://github.com/collective/collective.geo.settings>`__

`collective.geo.mapwidget <http://plone.org/products/collective.geo.mapwidget>`_
    provides some handy page macros and adapters to easily manage multiple maps on one page. `(repository) <https://github.com/collective/collective.geo.mapwidget>`__

`collective.z3cform.mapwidget <http://plone.org/products/collective.z3cform.mapwidget>`_
    provides a mapwidget for z3c.form framework. `(repository) <https://github.com/collective/collective.z3cform.mapwidget>`__

`collective.geo.contentlocations <http://plone.org/products/collective.geo.contentlocations>`_
    provides a GUI for collective.geo.geographer. It provides some simple forms to add geographical coordinates to Plone content types. `(repository) <https://github.com/collective/collective.geo.contentlocations>`__

`collective.geo.kml <http://plone.org/products/collective.geo.kml>`_
    provides KML views for georeferenced objects, allowing Plone content types to be visualized in Google Earth. `(repository) <https://github.com/collective/collective.geo.kml>`__


To display the maps, **collective.geo** takes advantage of `Openlayers <http://www.openlayers.org>`_, a JavaScript library for displaying map data in web browsers, with no server-side dependencies.

As a default map source we can select `OpenStreetMap <http://www.openstreetmap.org/>`_, `Google Maps <http://maps.google.com>`_ or `Bing Maps <http://www.bing.com/maps>`_.


.. image:: http://plone.org/products/collective.geo/screenshot
