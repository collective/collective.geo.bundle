from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.geo.bundle',
      version=version,
      description="Plone Maps (collective.geo)",
      long_description=open("README.rst").read() + "\n" +
                       open("HISTORY.rst").read(),
      classifiers=[
        "Framework :: Plone",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: GIS",
        "Programming Language :: Python",
        ],
      keywords='Zope Plone GIS KML Google Maps Bing Yahoo OpenLayers',
      author='Giorgio Borelli',
      author_email='giorgio@giorgioborelli.it',
      url='http://plone.org/products/collective.geo',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.geo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'BeautifulSoup',
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
