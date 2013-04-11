# -*- coding: utf-8 -*-
import os.path
import unittest

import robotsuite
from ..testing import CGEO_BUNDLE_ROBOT
from plone.testing import layered


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite(
            os.path.join("robotests", "hello.robot")),
            layer=CGEO_BUNDLE_ROBOT),
    ])
    return suite
