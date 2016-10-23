from setuptools import setup, find_packages

setup(
    name="tiny-dashboard-pc-stats",
    version="0.1",
    author="Benjie Jiao",
    author_email="hi@benjie.me",
    description=("Send PC stats to an Arduino dashboard via USB"),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'pyserial', 'psutil'
    ],
    entry_points={
        'console_scripts': [
            'pc-stats=pc_stats.pc_stats:cli'
        ]
    }
)
