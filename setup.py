import setuptools

with open ("README.md","r", encoding= "utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "AWS-MLops"
AUTHOR_USER_NAME = "Balaji"
SRC_REPO = 'AWS-MLops'
AUTHOR_EMAIL = "balaji3097@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= " a package for predicting person got transmited to other dimensions",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    
    
)