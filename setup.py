import timer_tool,sys,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

doc=timer_tool.__doc__.splitlines()
desc=''.join(doc[:3]) #取文档字符串的前3行

try:
    with open("README.rst",encoding="utf-8") as f:
        long_desc=f.read()
except OSError:
    long_desc=None

setup(
    name='timer-tool',
    version=timer_tool.__version__,
    description=desc,
    long_description=long_desc,
    author=timer_tool.__author__,
    author_email=timer_tool.__email__,
    url="https://github.com/qfcy/python-timer-tool",
    py_modules=['timer_tool'],
    keywords=["timer","performance","analysis","计时器","性能"],
    classifiers=[
        'Programming Language :: Python',
        "Natural Language :: Chinese (Simplified)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Utilities"
    ],
)
