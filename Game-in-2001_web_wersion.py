from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def game():
    if request.method == 'POST':
        ans = request.form['subject']
        min = int(request.form['min'])
        max = int(request.form['max'])
        if ans == "win":
            return "I win!"
        elif ans == "toobig":
            max = int(request.form['guess'])
        elif ans == "toosmall":
            min = int(request.form['guess'])
        if abs(max - min) <= 1:
            return "Don't cheat on me!"
        return options(min, max)
    else:
        return options()


def dice(code: str):
    guess = int((max - min) / 2) + min
    return f"""
    In this game you can roll the following types of dice: (3, 4, 6, 8, 10, 12, 20, 100)-sided.
       <br>
    <form action="/" method="POST">
                <input type="hidden" name="min" value="{min}">
                <input type="hidden" name="max" value="{max}">
                <input type="hidden" name="guess" value="{guess}">
            <button name="subject" type="submit" value="win">
                You win
            </button>
            <button name="subject" type="submit" value="toobig">
                Too big
            </button>
            <button name="subject" type="submit" value="toosmall">
                Too small
            </button>
    </form>
    """


if __name__ == '__main__':
    app.run(debug=True)


"""
szblon zabrany z aplikacji webowej ze zgadywania liczb.
na metodzie get pokaz tabele wynikow i popros o wpisanie wyboru kostek.
na metodzie post oblicz sumy punktow i przeprowad warunki po czym sprawdz
czy ktos wygral i przesli wynik do geta znowu.
jesli ktos wygral to w gecie wyswietl wynik, byc moze na innej podstronie. 
"""