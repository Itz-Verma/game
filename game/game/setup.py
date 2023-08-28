import cx_Freeze

executables = [cx_Freeze.Executable("abc.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["/Users/shivamkrishana/Desktop/game/background.png", "/Users/shivamkrishana/Desktop/game/virus.png", "/Users/shivamkrishana/Desktop/game/cell.png"]}},
    executables=executables
)
