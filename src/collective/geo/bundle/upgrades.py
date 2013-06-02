from Products.CMFCore.utils import getToolByName

from collective.geo import settings
from collective.geo import openlayers
from collective.geo import mapwidget
from collective.geo import contentlocations
from collective.geo import kml


def upgrade_to_2(context):

    # - collective.geo.settings
    # upgrade plone.app.registry
    settings.setuphandlers.upgrade_registry(context)

    # - collective.geo.openlayers
    # upgrade jsregistry
    openlayers.upgrades.upgrade_to_30(context)

    # - collective.geo.mapwidget
    # upgrade jsregistry and controlpanel
    mapwidget.upgrades.upgrade_to_20(context)

    # install collective.z3cform.colorpicker
    qi = getToolByName(context, 'portal_quickinstaller')
    if not qi.isProductInstalled('collective.z3cform.colorpicker'):
        qi.installProduct('collective.z3cform.colorpicker')

    # - collective.geo.contentlocations
    # add browserlayer, upgrade actions and remove IGeoMarkerUtility
    contentlocations.upgrades.upgrade_to_30(context)

    # - collective.geo.kml
    # add views and configuraiton for new collections
    kml.setuphandlers.add_ng_collection(context)
