from setuptools import setup

PACKAGE = "micro.common"

DEV = []
with open("requirements-dev.txt") as reqs:
    DEV = [l.strip() for l in reqs]

setup(
    name=PACKAGE,
    version='1.0.0',
    packages=[PACKAGE],
    namespace_packages=["micro"],
    install_requires=[
        "requests",
    ],
    extras_require={"dev": DEV}
)

