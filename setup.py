from setuptools import setup

setup(
    name='MillisecondClock',
    version='1.0',
    packages=[''],
    install_requires=[
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'millisecond_clock = millisecond_clock:main',
        ],
    },
)
