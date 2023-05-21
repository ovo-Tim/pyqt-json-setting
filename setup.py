import setuptools

with open("./dist/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyqt-json-setting",
    version="0.1",
    author="ovo-tim",
    author_email="ovo-tim@qq.com",
    description="根据json schema生成设置界面",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ovo-Tim/pyqt-json-settingt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
)