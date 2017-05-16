import json

filenames = ['industrial.json', 'stone.json']
techTreeDir = "../resources/technologies/"

jsonString = "";

dictionary = {}
clusters = {}

for fname in filenames:
    print "Processing..." + fname
    path = techTreeDir + fname
    with open(path) as infile:
        ldict = json.load(infile);
    dictionary.update(ldict)
    clusters[fname.replace(".json", "")] = ldict.values()

graphvisString = "\n\ndigraph G { rankdir=\"LR\" \n node[shape=rect]\n\n"

for c in clusters:
    k = c;
    graphvisString += "subgraph %s{\n label=\"%s\"\n node[color=\"black\"]\n" % (k, k)
    c = clusters[c];
    for i in c:
        graphvisString += "\"%s\"\n" % i["name"]
    graphvisString += "}\n\n"

for d in dictionary:
    d = dictionary[d]

    if "requires" not in d:
        continue

    for r in d["requires"]:
        src = dictionary[r]["name"]
        dest = d["name"]
        graphvisString += "\"%s\" -> \"%s\"\n" % (src, dest)

graphvisString += "}\n"
print graphvisString
