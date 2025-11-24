import sys
import os

# Ensure project src is importable when tests are run directly against the workspace folder
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
