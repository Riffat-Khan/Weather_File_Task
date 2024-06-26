import csv

def export_to_csv(file, resDict):
  with open(file, mode='w') as avgDataFile:
    fieldnames = resDict.keys()
    writing = csv.DictWriter(avgDataFile, fieldnames)
    writing.writeheader()
    writing.writerow(resDict)
    
def read_result_file(file):
  with open(file, mode='r') as resultFile:
    resultFile = csv.DictReader(resultFile)
    resultFileData = list(resultFile)
  return resultFileData[-1]