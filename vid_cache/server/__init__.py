import os
import sys

# This is absolutely disgusting. But we modify path so we can find the
# protocol module in the parent directory.

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
print(f"[vid_cache] adding '{parent_dir}' to path")

sys.path.append(parent_dir)

