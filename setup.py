from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.geo.bundle',
      version=version,
      description="Plone Maps (collective.geo)",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: GIS",
        "Programming Language :: Python",
        "Natural Language :: English",
        "Natural Language :: Italian",
        "Natural Language :: Dutch",
        ],
      keywords='Zope Plone GIS KML Google Maps Bing Yahoo OpenLayers',
      author='Giorgio Borelli',
      author_email='giorgio@giorgioborelli.it',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.geo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.geo.contentlocations',
          'collective.geo.kml',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
