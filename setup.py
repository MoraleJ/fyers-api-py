import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='fyers_api',  
     version='1.0.4',
     author="Fyers-Tech",
     author_email="support@fyers.in",
     description="Fyers data and trading APIs.",
     long_description="",
     long_description_content_type="text/markdown",
     url="https://github.com/FyersDev/fyers-api-py",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
