import csv

def run():
    results = []
    with open('67triangle.txt', newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(int(row))
        return (results)

if __name__ == "__main__":
    print(run())