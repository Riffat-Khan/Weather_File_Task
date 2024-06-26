import csv

def export_to_csv(file, res_dict):
  with open(file, mode='w') as avg_data_file:
    fieldnames = res_dict.keys()
    writing = csv.DictWriter(avg_data_file, fieldnames)
    writing.writeheader()
    writing.writerow(res_dict)
    
def read_result_file(file):
  with open(file, mode='r') as result_file:
    result_file = csv.DictReader(result_file)
    res_file_data = list(result_file)
  return res_file_data[-1]