from pathlib import Path

module_path = Path(__file__)
module_dir = module_path.parent

print(f"path: {module_path},\ndir: {module_dir}")