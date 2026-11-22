from setuptools import find_packages, setup

package_name = "rov_path_planner"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Ahmed",
    maintainer_email="ahmed@example.com",
    description="ROV path planner package",
    license="MIT",
    entry_points={
        "console_scripts": [
            "planner_node = rov_path_planner.planner_node:main",
        ],
    },
)
