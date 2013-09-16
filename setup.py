from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-diachron',
	version=version,
	description="Dataset inventory for Diachron FP7 project",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Knud M\xc3\xb6ller',
	author_email='kmoeller@brox.de',
	url='',
	license='MIT License',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.diachron'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.diachron:PluginClass
	""",
)
