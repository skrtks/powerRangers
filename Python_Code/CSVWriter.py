import csv

def writeCSV(score):
    with open("../results.csv", "w", newline= "") as resultsFile:
        fieldnames = ["runs", "score", "battery0", "battery1", "battery2", "battery3", "battery4"]
        writer = csv.DictWriter(resultsFile, fieldnames = fieldnames)

        writer.writeheader()
        for item in score:
            writer.writerow(item)
