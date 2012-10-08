.. Collective geo documentation master file, created by
   sphinx-quickstart on Sun May  6 00:44:04 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Collective geo's documentation!
==========================================

Contents:

.. toctree::
   :maxdepth: 2

   howto.rst

Packages:

.. toctree::
   :maxdepth: 1

   package_geographer.rst


Overview
========
Collective geo allows to geo-reference Plone content types and to display this information over a map. The core of collective geo is composed by the following packages:

collective.geo.geographer
    provides geo annotation for Plone

collective.geo.openlayers
    enables openlayers machinery into Plone

collective.geo.settings
    provides some utilities where settings of collective.geo packages can be stored

collective.geo.mapwidget
    provides some handy page macros and adapters to easily manage multiple maps on one page

collective.geo.contentlocations
    provides a GUI for collective.geo.geographer. It provides some simple forms to add geographical coordinates to Plone content types.

collective.geo.kml
    provides KML views for georeferenced objects, allowing Plone content types to be visualized in Google Earth.

To display the maps, collective.geo takes advantage of Openlayers, a JavaScript
library for displaying map data in web browsers with no server-side
dependencies.

As a default map source collective geo uses: OpenStreetMap, Google Maps or Bing Maps


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
