import random

def main():

    DATAFILE = "testdatav3.csv"

    columns = "MEF, incompleteness, criteria, scenario, score, date"
    
    mefs = [ {'name': 'M1', 'incompleteness': 50},
             {'name': 'M2', 'incompleteness': 30},
             {'name': 'M3', 'incompleteness': 25},
             {'name': 'M4', 'incompleteness': 18}
    ]

    criteria = []
    for n in range(1, 14):
        criteria.append(f"C{n}")
    
    scenarios = []
    for n in range(1, 53):
        scenarios.append(f"S{n}")

    with open(DATAFILE, 'w') as f:
        f.write(columns + "\n")
        for mef in mefs:
            for crit in criteria:
                for scenario in scenarios:
                    score = random.randrange(0, 100)
                    line = (f"{mef['name']}, {mef['incompleteness']}, " +
                            f"{crit}, {scenario}, {score}\n")
                    f.write(line)

        



if __name__ == '__main__':
    main()
    print("DONE\n")