from setuptools import setup
from kapacitor.udf import VERSION

setup(name='kapacitor_udf',
    version=VERSION,
    packages=[
        'kapacitor',
        'kapacitor.udf',
    ],
    install_requires=[
        "protobuf==3.0.0",
    ],
    maintainer_email="support@influxdb.com",
    license="MIT",
    url="github.com/influxdata/kapacitor",
    description="Kapacitor UDF Agent library"
)
