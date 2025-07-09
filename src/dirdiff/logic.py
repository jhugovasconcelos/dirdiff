from dirdiff.rich_imports import log, console, table, equal, different
from dirdiff.directories import get_files_in_dir


def show_diff(base_directory:str, compare_directory:str):
  l1 = get_files_in_dir(base_directory)
  l2 = get_files_in_dir(compare_directory)
  
  common = sorted([u for u in l1 if u in l2])
  unique_l1 = sorted([u for u in l1 if u not in l2])
  unique_l2 = sorted([u for u in l2 if u not in l1])

  len_common = len(common)
  len_u1 = len(unique_l1)
  len_u2 = len(unique_l2)
  longest = max([len_common, len_u1, len_u2])

  if len_common == longest:
    unique_l1.extend([" " for _ in range(len_common-len_u1)])
    unique_l2.extend([" " for _ in range(len_common-len_u2)])
  elif len_u1 == longest:
    unique_l2.extend([" " for _ in range(len_u1-len_u2)])
    common.extend([" " for _ in range(len_u1-len_common)])
  elif len_u2 == longest:
    unique_l1.extend([" " for _ in range(len_u2-len_u1)])
    common.extend([" " for _ in range(len_u2-len_common)])

  _table = [files for files in zip(unique_l1, common, unique_l2)]
  if unique_l1 or unique_l2:
    # Creating Table columns
    table.add_column(header=f'Only in {base_directory}', header_style="red", justify="center", style=different)
    table.add_column(header=f'Common files', header_style="green", justify="center", style=equal)
    table.add_column(header=f'Only in {compare_directory}', header_style="red", justify="center", style=different)

    # Creating Table rows
    table_rows = _table
    for row in table_rows:
        file_base, file_common, file_comp = row
        table.add_row(file_base, file_common, file_comp)
  else:
    # Creating Table columns
    table.add_column(header=f'Directories are equivalent', header_style="green", justify="center", style=equal)
    # Creating Table rows
    table_rows = _table
    for row in table_rows:
        file_base, file_common, file_comp = row
        table.add_row(file_base, file_common, file_comp)
  
  console.print(table)
