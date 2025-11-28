# tests/conftest.py
import sys
from pathlib import Path

# Add the project root (one level up from tests/) to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Optional: Print confirmation when tests start
print(f"\nAdded to Python path: {project_root}")
print("src imports should now work!\n")