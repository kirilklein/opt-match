from setuptools import setup


setup(
    name='opmatch',
    version='1.0.0',
    author="Kiril Klein",
    author_email="kikl@di.ku.dk",
    description="A leightweight package to perform optimal case-control matching.",
    url="https://github.com/kirilklein/opmatch",
    license='MIT',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Medical Researchers, Epidemiologists, Statisticians",
        "Topic :: Statistics :: Epidemiology",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="""matching, statistics, epidemiology, causal inference, propensity score,
    optimal matching, case-control matching, matching algorithms, matching methods, pharmacoepidemiology""", 
    #package_dir={"": "opmatch"},
    packages=["opmatch"],
    python_requires=">=3.7, <4", 
)