from setuptools import setup, find_packages
setup(name="mtool", packages=find_packages())

setup(
    # ...,
    setup_requires=["pytest-runner", ...],
    tests_require=["pytest", ...],
    # ...,
)