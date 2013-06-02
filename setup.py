from setuptools import setup, find_packages

version = '2.0b1'

setup(
    name='collective.geo.bundle',
    version=version,
    description="Plone Maps (collective.geo)",
    long_description=(
        open("OVERVIEW.rst").read() + "\n" +
        open("README.rst").read() + "\n" +
        open("HISTORY.rst").read()
    ),
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
        'collective.geo.contentlocations > 2.5',
        'collective.geo.kml > 2.5',
        # -*- Extra requirements: -*-
    ],
    extras_require={
        'dexterity': [
            'plone.app.dexterity',
            'collective.geo.behaviour'
        ],
        "test": [
            "plone.app.testing",
            "plone.app.robotframework"
        ]
    },
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
