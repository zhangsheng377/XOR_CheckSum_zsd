from setuptools import setup

NAME = 'XOR_CheckSum_zsd'
VERSION = '1.0.2.dev1'
URL = 'https://github.com/zhangsheng377/XOR_CheckSum_zsd'
KEYWORDS = 'XOR checksum string zsd'
EMAIL = '435878393@qq.com'
DESCRIPTION = 'XOR_CheckSum tools'
LONG_DESCRIPTION = '''XOR_CheckSum tools'''
REQUIRES = []
PACKAGES = ['XOR_CheckSum']

setup(
    name=NAME,
    author='zhangsheng377',
    license='MIT',
    zip_safe=False,
    url=URL,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author_email=EMAIL,
    keywords=KEYWORDS,
    install_requires=REQUIRES,
    packages=PACKAGES,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
