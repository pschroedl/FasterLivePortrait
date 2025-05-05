from setuptools import setup, find_packages

setup(
    name="faster-live-portrait",
    version="0.0.1",
    description="Real-time AI portrait reenactment pipeline",
    author="",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    zip_safe=False,
)