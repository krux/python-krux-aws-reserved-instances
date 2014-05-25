# -*- coding: utf-8 -*-
#
# © 2014 Krux Digital, Inc.
#
"""
Package setup for krux-aws-reserved-instances
"""
######################
# Standard Libraries #
######################
from __future__ import absolute_import
from setuptools import setup, find_packages

import os

# We use the version to construct the DOWNLOAD_URL.
VERSION      = '0.0.1'

# URL to the repository on Github.
REPO_URL     = 'https://github.com/krux/krux-aws-reserved-instances'
# Github will generate a tarball as long as you tag your releases, so don't
# forget to tag!
DOWNLOAD_URL = ''.join((REPO_URL, '/tarball/release/', VERSION))


setup(
    name             = 'krux-aws-reserved-instances',
    version          = VERSION,
    author           = 'Jos Boumans',
    author_email     = 'jos@krux.com',
    description      = 'Library for interacting with AWS reserved instances built on krux-stdlib',
    url              = REPO_URL,
    download_url     = DOWNLOAD_URL,
    license          = 'All Rights Reserved.',
    packages         = find_packages(),
    install_requires = [
        'krux-boto',
        'krux-stdlib',
    ],
    entry_points     = {
        'console_scripts': [
            'krux-aws-ri = krux_aws_reserved_instances:main',
        ],
    },
)
