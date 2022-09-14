from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

install_requires = [
    'nbformat'
]

setup_requires = [
    'setuptools >= 30'
]

tests_require = [
    'pytest',
    'flake8',
    'pytest-flake8',
    'pytest-cram == 0.2.2',
]

setup(name='nbstripout',
      version='0.6.0',

      author='Florian Rathgeber',
      author_email='florian.rathgeber@gmail.com',
      url='https://github.com/kynan/nbstripout',

      license="License :: OSI Approved :: MIT License",

      description='Strips outputs from Jupyter and IPython notebooks',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      packages=find_packages(),
      provides=['nbstripout'],
      entry_points={
          'console_scripts': [
              'nbstripout = nbstripout._nbstripout:main'
          ],
      },

      install_requires=install_requires,
      setup_requires=setup_requires,
      tests_require=tests_require,
      python_requires='>=3.6',

      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Other Environment",
          "Framework :: IPython",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Topic :: Software Development :: Version Control",
      ])
