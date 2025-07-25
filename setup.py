import sys
from cx_Freeze import setup, Executable

# Define build options with enhancements.
build_exe_options = {
    "packages": ["os", "sys"],
    "excludes": ["unittest", "pydoc", "tkinter"],    # exclude unused modules
    "include_files": [("./src/images", "images")],       # include additional files or folders
    "include_msvcr": True,                           # include MS Visual C++ runtime DLLs
    "optimize": 2,                                   # enable optimization
}

# Set the base for GUI applications.
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="neocasa",
    version="1.55",
    description="Image describer",
    author="Kefas James Lungu",
    author_email="jameskefaslungu@gmail.com",
    url="https://github.com/kefaslungu/neocasa",
    license="GPL2",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/neocasa.py", base=base, icon="src/images/neocasa_logo.ico")]
)
