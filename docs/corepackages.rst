Core Packages
=============

collective.geo.geographer
-------------------------

collective.geo.geographer has been documented on readthedocs.org: http://collectivegeo.readthedocs.org/projects/collectivegeogeographer/

collective.geo.openlayers
-------------------------

This package includes `OpenLayers`_ framework in Plone.

You can include an `Openlayers`_ map in a page using a `BrowserView <http://developer.plone.org/views/browserviews.html>`_
or a `Page template <http://docs.zope.org/zope2/zope2book/ZPT.html>`_.

There is a simple integration example:

.. code-block:: html

    <html xmlns="http://www.w3.org/1999/xhtml"
          xmlns:metal="http://xml.zope.org/namespaces/metal"
          xmlns:tal="http://xml.zope.org/namespaces/tal"
          metal:use-macro="here/main_template/macros/master">
      <head>
        <metal:block metal:fill-slot="style_slot">
            <style type="text/css">
              #map {
                  width: 100%;
                  height: 500px;
                  border: 1px solid black;
                  position: relative
              }
            </style>
        </metal:block>

        <metal:block metal:fill-slot="javascript_head_slot">
          <script type="text/javascript">
            <!--
              (function ($) {
                var map;
                jq(window).load(function() {
                  map = new OpenLayers.Map('map');
                  var wms = new OpenLayers.Layer.WMS(
                                  "OpenLayers WMS",
                                  "http://labs.metacarta.com/wms/vmap0",
                                  {layers: 'basic'}
                              );
                  map.addLayer(wms);
                  mousecontrol = new OpenLayers.Control.MousePosition(),
                  map.addControl(mousecontrol);

                  map.setCenter(new OpenLayers.LonLat(7, 45), 3);

                });
              }(jQuery));
            // -->
          </script>
        </metal:block>
      </head>
      <body>
        <metal:content fill-slot="content-core">
            <metal:content define-macro="content-core">
              <div id="map" class="olMap">
                <!-- openlayers map -->
              </div>
            </metal:content>
        </metal:content>
      </body>
    </html>


For more informations about `OpenLayers`_ see:

* `Openlayers examples <http://openlayers.org/dev/examples/>`_
* `Openlayers User documentation <http://trac.osgeo.org/openlayers/wiki/Documentation>`_
* `Openlayers API <http://dev.openlayers.org/releases/OpenLayers-2.12/doc/apidocs/files/OpenLayers-js.html>`_


collective.geo.settings
-----------------------

This package provides some utilities to store settings used in
collective.geo packages.

Settings are stored in Plone registry and they provide default values to map widgets.

They are split in two different interfaces:

* IGeoSettings for map settings, like default map layers, center, zoom  etc.
* IGeoFeatureStyle for map style like lines and polygon colors, marke image etc.

For more details see:
`collective.geo.settings.interfaces <https://github.com/collective/collective.geo.settings/blob/master/collective/geo/settings/interfaces.py>`_

You can retrieve settings by `plone.app.registry`_ API:

.. code-block:: python

    from zope.component import getUtility

    from plone.registry.interfaces import IRegistry
    from collective.geo.settings.interfaces import IGeoSettings
    registry = getUtility(IRegistry)
    settings = registry.forInterface(IGeoSettings)


    from collective.geo.settings.interfaces import IGeoFeatureStyle
    styles = registry.forInterface(IGeoSettings)

or using some utilities:

.. code-block:: python

    from collective.geo.settings.utils import geo_settings
    settings = geo_settings()

    from collective.geo.settings.utils import geo_styles
    styles = geo_settings()


Coordinate field
^^^^^^^^^^^^^^^^

collective.geo.settings defines a field type 'Coordinate'
useful to define a coordinate attribute in Zope Interface and use it in forms.

You can define an interface in this way:

.. code-block:: python

    import decimal
    from zope.interface import Interface
    from collective.geo.settings.schema import Coordinate

    class IGeoSettings(Interface):
        ...
        longitude = Coordinate(
            title=_(u'Longitude'),
            default=decimal.Decimal("0.0"),
            required=True
        )

collective.z3cform.mapwidget
----------------------------

Example:

.. code-block:: python

    from zope.interface import Interface
    from zope import schema

    from z3c.form import form, field
    from collective.z3cform.mapwidget.widget import MapFieldWidget


    class IMyForm(Interface):
        wkt = schema.Text(
            title=u"Shape in WKT format"
        )


    class GeoShapeForm(form.Form):
        fields = field.Fields(IMyManager)
        fields['wkt'].widgetFactory = MapFieldWidget

        ...

.. * collective.geo.mapwdget
.. * collective.geo.contentlocations
.. * collective.geo.kml
.. * collective.geo.behaviour

.. _OpenLayers: http://openlayers.org
.. _plone.app.registry: https://pypi.python.org/pypi/plone.app.registry
