Installation
============

Dependencies
------------
Collective geo and collective.geo.contentlocation in particular,
depend on Shapely, a library for the manipulation of planar geometric
objects and Shapely itself depends on libgeos_c > 3.1

Before installing collective.geo you have to install libgeos_c library on your machine.

Debian/Ubuntu
^^^^^^^^^^^^^
On Linux systems based on Debian, you have to install the following packages:

* libgeos-c1
* libgeos-dev

Mac OS X
^^^^^^^^^
To install libgeos on Mac OS X system you can use macports and install this pachage:

* geos

Buildout
--------

The best way to install collective geo is using zc.buildout and adding the collective.geo.bundle package.

This package contains all core packages of c.geo that are suitable for common use.

Below an example of configuration::

    [buildout]
    ...
    eggs =
        ...
        collective.geo.bundle
    ...

You can also use each package separately to better suit your needs.

For instance, you can use only c.geo.geographer if you need to annotate geographical information on Plone content types or you can use only c.geo.openlayers to integrate OpenLayers javascript in Plone. See above for package details.

After running the buildout and started zope you have to install the product Plone Maps (collective.geo) from Addons Control Panel.

For development pourpose you can use the buildout configuration included in collective.geo.bundle.

In this package you'll find two different configurations:

* buildout.cfg: a generic buildout configuration that includes collective.geo.bundle and its dependencies
* devel.cfg a specific development configuration that includes all c.geo source packages from github
