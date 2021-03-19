import re

list = input("Name the file you'd like to search (preferably generated using Racoda's owner report) without the .tsv extension: ")
season = input("What season are you searching for? (I don't care if this was in the thing just follow along) ")
f = open(list + ".tsv", "r")
g = open(list + " formatted.tsv", "w")
g.write("[table]")
for line in f:
    line = line.replace("\t", "[/td][td]")
    line = line.replace("\n", "[/list][/td][/tr]\n[tr][td]")
    line = re.sub(r":\d,", "[/nation][*][nation]", line)
    line = re.sub(r":\d", "[/nation]", line)
    line = re.sub(r"\[\/td\]\[td\]\d*\[\/td\]\[td\]\d*\[\/td\]\[td\]\d*\[\/td\]\[td\]", f"/season={season}]Link to Card[/url][/td][td][list][*][nation]", line)
    line = re.sub(r"^", "[url=https://www.nationstates.net/page=deck/card=", line)
    line = re.sub(r"\[\*\]\[nation\]\[\/list\]", "[i]No owners... :([/i][/list]", line)
    line = line.replace("[url=https://www.nationstates.net/page=deck/card=ID[/td][td]SEASON[/td][td]NUMBER OF OWNERS[/td][td]NUMBER OF COPIES[/td][td]OWNERS:COPIES[/list][/td][/tr]\n[tr][td]", "[tr][td][b]CARD LINK[/b][/td][td][b]OWNERS[/b][/td][/tr]\n[tr][td]")
    g.write(line)
g.write("[/table]")

f.close()
g.close()
