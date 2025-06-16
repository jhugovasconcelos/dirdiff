from dirdiff.rich_imports import log, console, table
from dirdiff.directories import get_files_in_dir


def compare_dirs(src:str, dst:str):
  log.debug(f"Source Directory: {src}")
  log.debug(f"Destination Directory: {dst}")

  src_files = get_files_in_dir(src) 
  dst_files = get_files_in_dir(dst)

  only_in_src = [f for f in src_files + dst_files if f not in dst_files]
  only_in_dst = [f for f in src_files + dst_files if f not in src_files]

  return only_in_src, only_in_dst

def show_diff(src:str, dst:str):
  log.debug("Calling functions")
  only_in_src, only_in_dst= compare_dirs(src, dst)
  
  # Creating Table columns
  table.add_column(header=f'Only in {src}', header_style="cyan", justify="center")
  table.add_column(header=f'Only in {dst}', header_style="green", justify="center")
  
  # Adjusting extra white spaces
  if len(only_in_src) > len(only_in_dst):
    for _ in range(len(only_in_src) - len(only_in_dst)):
      only_in_dst.append(" ")
  else:
      for _ in range(len(only_in_dst) - len(only_in_src)):
        only_in_src.append(" ")

  # Creating Table rows
  table_rows = zip(only_in_src, only_in_dst)
  for row in table_rows:
      file_src, file_dst = row
      table.add_row(file_src, file_dst)

  console.print(table)
