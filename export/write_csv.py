import csv

def export_to_csv(file_path, resDict):
  fieldnames = resDict.keys()
  with open(file_path, mode='w') as avgDataFile:
    writing = csv.DictWriter(avgDataFile, fieldnames)
    writing.writeheader()
    writing.writerow(resDict)
    
def read_result_file(file_path):
  with open(file_path, mode='r') as resultFile:
    resultFile = csv.DictReader(resultFile)
    resultFileData = list(resultFile)
    for eachRow in resultFileData:
      return eachRow