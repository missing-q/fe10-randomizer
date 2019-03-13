def gen(index):
    #create html file
    message = "<table><tr><th>Character</th><th>Class</th><th>Weapon</th></tr>"

    for i in index:
        message += "<tr><td>" + i[0] + "</td><td>" + i[1] + "</td><td>" + i[2] + "</td></tr>"

    message += "</table>"

    with open('output.html', 'w') as f:
        f.write("<!DOCTYPE html><html><body>" + message + "</body></html>")
