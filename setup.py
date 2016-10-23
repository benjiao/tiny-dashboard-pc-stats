from setuptools import setup

setup(
    name="tiny-dashboard-pc-stats",
    version="0.1",
    author="Benjie Jiao",
    author_email="hi@benjie.me",
    description=("Send PC stats to an Arduino dashboard via "),
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'pc-stats=pc_stats.cli:cli'
        ]
    },
    install_requires=[
        'Click', 'pyserial', 'psutil'
    ],
)
