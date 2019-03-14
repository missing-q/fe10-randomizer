def gen(index):
    #create html file
    message = ""

    for i in index:
        message += "<table><tr><th>Character</th><th>Class</th><th>Weapon</th></tr>"
        message += "<tr><td>" + i[0] + "</td><td>" + i[1] + "</td><td>" + i[2] + "</td></tr>"
        message += "<tr><th>Growths</th><th>HP</th><th>Str</th><th>Mag</th><th>Skl</th><th>Spd</th><th>Lck</th><th>Def</th><th>Res</th></tr>"
        message += "<tr><td></td><td>" + i[3][0] + "</td></tr>"
        message += "</table>"

    with open('output.html', 'w') as f:
        f.write("<!DOCTYPE html><html><body>" + message + "</body></html>")
