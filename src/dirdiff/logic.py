from dirdiff.rich_imports import log, console, table, equal, different
from dirdiff.directories import get_files_in_dir


def better_zip(l1:list, l2:list) -> list[tuple]:
  """
    This function takes two lists of different sizes and where some or all elements are different and equalizes them by 
    putting blank spaces in between them until both have the same size and all the elements that are equal are in the
    same index on both lists and the ones that are different are in the same index as blank spaces on the other list. 
    Then it returns a list with tuples containing all the elements in both lists, where equal elements are in the same 
    tuple and unique elements are grouped with blank spaces.

    Remember to pass the bigger list as l1 and the smaller list as l2. 
    Will fix that in the future
  """
  zipped = []
  l1 = sorted(l1)
  l2 = sorted(l2)

  # Main loop iterating over the lenght of the bigger list (that is decided outside the function call)
  for i in range(len(l1)):
    # First, check if the smaller list is exhausted
    if i < len(l2):
        # Are they the same? Done
        if l1[i] == l2[i]:
          pass
        else:
          # Is either of them blank? Done
          if l1[i] == " " or l2[i] == " ":
            pass
          # Here is the actual shift
          else:
            if l1[i] < l2[i]:
              if i == 0:
                l2 = [" "] + l2
              else:
                l2 = l2[:i] + [" "] + l2[i:]
            else:
              if i == 0:
                l1 = [" "] + l1
              else:
                l1 = l1[:i-1] + [" "] + l1[i:]
  
  # Zipping it all together
  for i in range(len(l1)):
    zipped.append((l1[i], l2[i]))
  
  return zipped

def compare_dirs(src:str, dst:str):
  log.debug(f"Source Directory: {src}")
  log.debug(f"Destination Directory: {dst}")

  src_files = get_files_in_dir(src) 
  dst_files = get_files_in_dir(dst)

  if src_files > dst_files:
    table_rows = better_zip(l1=src_files, l2=dst_files)
  else:
    table_rows = better_zip(l1=dst_files, l2=src_files)

  return table_rows

def show_diff(src:str, dst:str):
  log.debug("Calling functions")
   
  # Creating Table columns
  table.add_column(header=f'{src}', header_style="cyan", justify="center")
  table.add_column(header=f'{dst}', header_style="green", justify="center")
  
  # Creating Table rows
  table_rows = compare_dirs(src, dst)
  for row in table_rows:
      file_src, file_dst = row
      if file_src == " " or file_dst == " ":
        table.add_row(file_src, file_dst, style=different)
      else:
        table.add_row(file_src, file_dst, style=equal)

  console.print(table)
