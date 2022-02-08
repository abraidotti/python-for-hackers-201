from distutils.core import setup
import py2exe

setup(
    options={"py2exe": {"bundle_files": 1, "compressed": True}},
    console=[{"script": "py2exe_demo.py"}],
    zipfile=None,
)

# command:
# python demo_setup.py py2exe
