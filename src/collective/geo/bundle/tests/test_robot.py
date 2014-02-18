# -*- coding: utf-8 -*-
import os.path
import unittest

import robotsuite
from ..testing import CGEO_FUNCTIONAL_TESTING
from plone.testing import layered


def test_suite():
    suite = unittest.TestSuite()

    suite.addTests([
        layered(robotsuite.RobotTestSuite(
            os.path.join("robotests", "control_panel.robot")),
            layer=CGEO_FUNCTIONAL_TESTING),

        layered(robotsuite.RobotTestSuite(
            os.path.join("robotests", "geo_reference_page.robot")),
            layer=CGEO_FUNCTIONAL_TESTING),

        layered(robotsuite.RobotTestSuite(
            os.path.join("robotests", "dexterity.robot")),
            layer=CGEO_FUNCTIONAL_TESTING),
    ])

    return suite
