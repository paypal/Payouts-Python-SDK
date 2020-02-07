from setuptools import setup, find_packages

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="paypal-payouts-sdk",
    version="1.0.0",
    author="https://developer.paypal.com",
    author_email="dl-paypal-payouts-sdk@paypal.com",
    description="Python Rest SDK for PayPal Payouts",
    long_description="Python Rest SDK for PayPal Payouts",
    long_description_content_type="text/markdown",
    url="https://github.com/paypal/Payouts-Python-SDK/",
    packages=find_packages(exclude=["tests","sample"]),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["paypalhttp"],
)