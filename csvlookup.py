import csv
def csvlookuptable(lookupfield, csvfilename):
    output = {}
    with open(csvfilename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            output[row[lookupfield]] = row
    return output

def csvlookup(lookupvalue, lookupfield, csvfilename):
    return csvlookuptable(lookupfield, csvfilename)[lookupvalue]

def csvlookupvalue(lookupvalue, lookupfield, csvfilename, outputfield):
    return csvlookup(lookupvalue, lookupfield, csvfilename)[outputfield]

#USAGE
#print(csvlookuptable('Melakartha', 'raga.csv'))
#print(csvlookup('29', 'Melakartha', 'raga.csv'))
#print(csvlookupvalue('29', 'Melakartha', 'raga.csv', 'Raga'))

