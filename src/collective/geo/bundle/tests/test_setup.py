# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.geo.bundle.testing import COLLECTIVE_GEO_BUNDLE_INTEGRATION_TESTING  # noqa
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import login
from plone.z3cform.interfaces import IFormWrapper
from zope.publisher.interfaces.browser import IBrowserPage
import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.geo.bundle is properly installed."""

    layer = COLLECTIVE_GEO_BUNDLE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.portal.acl_users.userFolderAddUser(
            SITE_OWNER_NAME, SITE_OWNER_PASSWORD, ['Manager'], [])
        login(self.portal, SITE_OWNER_NAME)
        self.portal.portal_workflow.setDefaultChain(
            "simple_publication_workflow")

    def test_create_document(self):
        # Adding content fails since traversing to the add-view
        # returns a collective.geo.mapwidget.browser.widget.MapWidget object.
        add_view = self.portal.restrictedTraverse('++add++Document')
        self.assertTrue(IBrowserPage.providedBy(add_view))
        self.assertTrue(IFormWrapper.providedBy(add_view))
