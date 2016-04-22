from setuptools import setup, find_packages

version = '2.4.dev0'

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
        'collective.geo.kml >= 3.2',
        'collective.geo.behaviour >= 1.2'
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
