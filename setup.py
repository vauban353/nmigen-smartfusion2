from setuptools import setup, find_packages


def scm_version():
    def local_scheme(version):
        return version.format_choice("+{node}", "+{node}.dirty")
    return {
        "relative_to": __file__,
        "version_scheme": "guess-next-dev",
        "local_scheme": local_scheme,
    }


setup(
    name="nmigen-smartfusion2",
    use_scm_version=scm_version(),
    author="vauban353",
    author_email="vauban353@gmail.com",
    description="SmartFusion2 configuration using nMigen",
    license="BSD",
    setup_requires=["wheel", "setuptools", "setuptools_scm"],
    install_requires=[
        "nmigen>=0.2,<0.4",
        "importlib_metadata; python_version<'3.8'",
    ],
    packages=find_packages(),
    project_urls={
        "Source Code": "https://github.com/vauban353/nmigen-smartfusion2",
        "Bug Tracker": "https://github.com/vauban353/nmigen-smartfusion2/issues",
    },
)
