from setuptools import setup

setup(name='lazylearn',
      version='0.0.1',
      description='Machine learning the lazy way.',
      url='http://github.com/linxichen/lazylearn',
      author='Linxi Chen',
      author_email='linxichen88@gmail.com',
      license='GPL v3',
      packages=['lazylearn'],
      install_requires=[
          'numpy',
          'pandas',
          'scikit-learn',
          'scipy',
      ],
      test_suite='tests',
      tests_require=['pytest'],
      include_package_data=True,
      zip_safe=False)