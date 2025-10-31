import os
import hashlib


def generate_hash(path) -> str:
    with open(path, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
        return digest.hexdigest()

def scanner(scan) -> list:
  files = []
  for f in scan:
      file_dir = {}
      file_dir.update({"name":f.name})
      if f.is_dir():
          file_dir.update({"is_dir": True})
      elif f.is_file():
          file_dir.update({"is_file":True})
          hash = generate_hash(f.path)
          file_dir.update({"hash":hash})
      elif f.is_symlink():
          file_dir.update({"is_symlink":True})
      elif f.is_symlink():
          file_dir.update({"is_junction":True})
      files.append(file_dir)
  return files

def get_files_in_dir(dir) -> list[dict]:
    """
    Scans a directory and generates 
    a list of dictionaries of each object therein, 
    wether it's a file, directory, symlink or junction.
    """
    scan = os.scandir(dir)
    files:list = scanner(scan)
    return files
