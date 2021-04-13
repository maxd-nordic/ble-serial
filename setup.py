import setuptools, platform

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ble-serial",
    version="1.3.0",
    author="Jake",
    author_email="ble-serial-pypi@ja-ke.tech",
    description="A package to connect BLE serial adapters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jakeler/ble-serial",
    packages=[
        "ble_serial",
        "ble_serial.ports",
        "ble_serial.setup_com0com"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'bleak >= 0.11.0',
        'pyserial >= 3.4.0 ;platform_system == "Windows"',
        'aioserial >= 1.3.0 ;platform_system == "Windows"',
    ],
    entry_points={
        'console_scripts': [
            'ble-scan=ble_serial.scan:main',
            'ble-serial=ble_serial.main:launch',
        ] + (
            ['ble-setup=ble_serial.setup_com0com:main'] if platform.system() == "Windows" else []
        )
    },
)
