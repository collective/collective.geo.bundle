from plone.testing import z2
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import FunctionalTesting
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import collective.geo.bundle


CGEO = PloneWithPackageLayer(
    zcml_package=collective.geo.bundle,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.geo.bundle:testing',
    name="CGEO")


CGEO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(AUTOLOGIN_LIBRARY_FIXTURE, CGEO, z2.ZSERVER),
    name="collective.geo.bundle:Robot")
