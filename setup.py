#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    use_scm_version={"write_to": "napari_svg/_version.py"},
    setup_requires=["setuptools_scm"],
)
