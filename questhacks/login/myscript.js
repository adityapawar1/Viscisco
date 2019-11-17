const fs = require('fs-js');
function myEnter() {
    let name = document.getElementById("Name").value;
    let age = document.getElementById("age").value;
    let User = document.getElementById("User").value;
    let Pass = document.getElementById("Pass").value;
    let School = document.getElementById("School").value;
    let ZIP = document.getElementById("ZIP").value;
    document.write("Full Name: ")
    document.write(name);
    document.write("<br>");
    document.write("Age: ")
    document.write(age);
    document.write("<br>");
    document.write("Username: ")
    document.write(User);
    document.write("<br>");
    document.write("Password: ")
    document.write(Pass);
    document.write("<br>");
    document.write("School: ")
    document.write(School);
    document.write("<br>");
    document.write("ZIP: ")
    document.write(ZIP);

    let data = "Learning how to write in a file.";


    fs.writeFile('in.txt', data, (err) => {
        console.log("Hello");
        if (err) throw err;
    })
}


