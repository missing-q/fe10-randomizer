def gen(index):
    #create html file
    message = ""

    for i in index:
        message += "<table style = 'border: 1px solid; margin-bottom: 20px'><tr><th>Character</th><th>Class</th><th>Weapon</th></tr>"
        message += "<tr><td>" + i[0] + "</td><td>" + i[1] + "</td><td>" + i[2] + "</td></tr>"

        message += "<tr><th>Growths</th><th>HP</th><th>Str</th><th>Mag</th><th>Skl</th><th>Spd</th><th>Lck</th><th>Def</th><th>Res</th></tr>"
        message += "<tr><td></td><td>" + str(i[3][0]) + "</td><td>" + str(i[3][1]) + "</td><td>" + str(i[3][2]) + "</td><td>" + str(i[3][3]) + "</td><td>" + str(i[3][4]) + "</td><td>" + str(i[3][5]) + "</td><td>" + str(i[3][6]) + "</td><td>" + str(i[3][7]) + "</td></tr>"

        message += "<tr><th>Stats</th><th>HP</th><th>Str</th><th>Mag</th><th>Skl</th><th>Spd</th><th>Lck</th><th>Def</th><th>Res</th></tr>"
        message += "<tr><td></td><td>" + str(i[4][0]) + "</td><td>" + str(i[4][1]) + "</td><td>" + str(i[4][2]) + "</td><td>" + str(i[4][3]) + "</td><td>" + str(i[4][4]) + "</td><td>" + str(i[4][5]) + "</td><td>" + str(i[4][6]) + "</td><td>" + str(i[4][7]) + "</td></tr>"

        message += "</table>"

    with open('output.html', 'w') as f:
        f.write("<!DOCTYPE html><html><body>" + message + "</body></html>")
