from setuptools import setup


setup(
    name='pl',
    version='0.1',
    py_modules=['pl'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pl=pl:cli
    ''',
)
