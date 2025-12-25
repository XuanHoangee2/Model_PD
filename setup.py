import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"
REPO_NAME = "Model_PD"
AUTHOR_USER_NAME= "Hoangee2"
SRC_REPO = "Model_PD"
AUTHOR_EMAIL = "tranxuanhoang14062004@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Calculate the probability that a customer will default on their payment",
    long_description=long_description,
    url = f"https.github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https.github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

)