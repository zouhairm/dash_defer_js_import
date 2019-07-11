import json
import os
from setuptools import setup


with open(os.path.join('dash_defer_js_import', 'package.json')) as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package['description'] if 'description' in package else package_name,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[]
)
