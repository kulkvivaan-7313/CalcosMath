How to run CalcosMath:

1. Clone this Respiratory: git clone https://github.com/kulkvivaan-7313/CalcosMath.git
2. Open in VS Code or any main complier
3. Open the Terminal
4. Install Flask via "pip install flask"
5. Enter python app.py to start the app
6. Go to http://127.0.0.1:5000

File Breakdown:

app.py - Flask web server and routes

main.py - Core math logic and calculations

templates/index.html - Web user interface

How it runs:

templates/index.html: Hey JavaScript, the user wants to do addition and the 2 numbers are 2 and 4. Please return me the sum
JavaScript: I don't know how to do math! Let me ask app.py to tell main.py since I don't have access to main.py!!
*Calls app.py
JavaScript: Hello app.py, templates/index.html wants me to solve 2 + 2 for the user, but idk how to do that. Can you make main.py?
app.py: no 🤪 Just kidding! I will
app.py: Hey, main.py, please solve 2 + 4. 
main.py: Ahh let me see my functions, oh yes! the addition(a,b) function. BET! The answer is 6!
app.py: JavaScript, its 6
JavaScript: templates/index.html, its 6
templates/index.html: The answer is 6!!!!

This is how the files communicate with each other. It is super quick it only takes a fraction of a second. Meanwhile, it is doing all this calculation!
