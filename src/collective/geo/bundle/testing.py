# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import login
from plone.testing import z2

import collective.geo.bundle


class CollectiveGeoBundleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.geo.bundle)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.geo.bundle:default')
        portal.acl_users.userFolderAddUser('admin', 'secret', ['Manager'], [])
        login(portal, 'admin')


COLLECTIVE_GEO_BUNDLE_FIXTURE = CollectiveGeoBundleLayer()


COLLECTIVE_GEO_BUNDLE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_GEO_BUNDLE_FIXTURE,),
    name='CollectiveGeoBundleLayer:IntegrationTesting'
)


COLLECTIVE_GEO_BUNDLE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_GEO_BUNDLE_FIXTURE,),
    name='CollectiveGeoBundleLayer:FunctionalTesting'
)


COLLECTIVE_GEO_BUNDLE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_GEO_BUNDLE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveGeoBundleLayer:AcceptanceTesting'
)
