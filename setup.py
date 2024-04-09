from setuptools import setup

setup(name='tetryonai',
      version='0.1',
      description='Rapid Prototyping for Machine Learning Applications.',
      url='https://github.com/sean-mcclure/tetryon_ai',
      author='Sean McClure',
      author_email='tetryonai@kedion.ai',
      license='MIT',
      packages=['tetryonai'],
      install_requires=[
            'numpy',
            'pandas',
            'requests',
            'bs4',
            'opencv-python',
            'scikit-learn'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
