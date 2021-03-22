from setuptools import setup


VERSION = "0.0.144"

setup(
    name='yandex-parser',
    description="Parse html content of Yandex",
    version=VERSION,
    url='https://github.com/KokocGroup/yandex-parser',
    download_url='https://github.com/KokocGroup/yandex-parser/tarball/v{0}'.format(VERSION),
    packages=['yandex_parser'],
    install_requires=[
        'pyquery==1.2.9',
        'lxml==4.6.3',
    ],
)
