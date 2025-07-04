import os

from dirdiff.rich_imports import log

def get_files_in_dir(dir:str) -> list[str]:
  try:
    log.info(f'Fetching files from directory {dir}')
    return os.listdir(dir)
  except FileNotFoundError:
    log.error(f"Directory {dir} could not be found")
    return [""]
  except NotADirectoryError:
    log.error(f"The path {dir} is not a directory")
    return [""]