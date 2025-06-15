import os
import sys
import importlib
python = sys.executable
file_directory = os.path.dirname(os.path.abspath(__file__))
WEB_DIRECTORY = file_directory + "/js"
def print_cyberpunk_logo():
    logo = [
        "\033[38;5;201m ██████╗\033[38;5;165m██╗   ██╗\033[38;5;129m██████╗ \033[38;5;93m███████╗\033[38;5;57m██████╗ \033[38;5;21m██████╗ \033[38;5;27m██╗   ██╗\033[38;5;33m███╗   ██╗\033[38;5;39m██╗  ██╗\033[0m",
        "\033[38;5;201m██╔════╝\033[38;5;165m╚██╗ ██╔╝\033[38;5;129m██╔══██╗\033[38;5;93m██╔════╝\033[38;5;57m██╔══██╗\033[38;5;21m██╔══██╗\033[38;5;27m██║   ██║\033[38;5;33m████╗  ██║\033[38;5;39m██║ ██╔╝\033[0m",
        "\033[38;5;201m██║     \033[38;5;165m ╚████╔╝ \033[38;5;129m██████╔╝\033[38;5;93m█████╗  \033[38;5;57m██████╔╝\033[38;5;21m██████╔╝\033[38;5;27m██║   ██║\033[38;5;33m██╔██╗ ██║\033[38;5;39m█████╔╝ \033[0m",
        "\033[38;5;201m██║     \033[38;5;165m  ╚██╔╝  \033[38;5;129m██╔══██╗\033[38;5;93m██╔══╝  \033[38;5;57m██╔═══╝ \033[38;5;21m██╔═══╝ \033[38;5;27m██║   ██║\033[38;5;33m██║╚██╗██║\033[38;5;39m██╔═██╗ \033[0m",
        "\033[38;5;201m╚██████╗\033[38;5;165m   ██║   \033[38;5;129m██████╔╝\033[38;5;93m███████╗\033[38;5;57m██║     \033[38;5;21m██║     \033[38;5;27m╚██████╔╝\033[38;5;33m██║ ╚████║\033[38;5;39m██║  ██╗\033[0m",
        "\033[38;5;201m ╚═════╝\033[38;5;165m   ╚═╝   \033[38;5;129m╚═════╝ \033[38;5;93m╚══════╝\033[38;5;57m╚═╝     \033[38;5;21m╚═╝     \033[38;5;27m ╚═════╝ \033[38;5;33m╚═╝  ╚═══╝\033[38;5;39m╚═╝  ╚═╝\033[0m"
    ]
    print()
    for line in logo:
        print(line)
    print()
    print("\033[38;5;51m🚀 CYBERPUNK-STYLE-DIY Custom Nodes Loaded! 🚀\033[0m")
    print()
print_cyberpunk_logo()
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
def load_nodes():
    py_dir = os.path.join(file_directory, "py")
    if os.path.exists(py_dir):
        if py_dir not in sys.path:
            sys.path.insert(0, py_dir)
        for filename in os.listdir(py_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, "NODE_CLASS_MAPPINGS"):
                        NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
                    if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS"):
                        NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
                except:
                    pass
load_nodes()
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]