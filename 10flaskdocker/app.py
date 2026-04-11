from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def table():
    rows = ""
    number = ""

    if request.method == "POST":
        number = request.form.get("number")
        if number:
            num = int(number)
            rows = "".join(
                f"<tr><td>{num}</td><td>×</td><td>{i}</td><td>=</td><td>{num*i}</td></tr>"
                for i in range(1, 11)
            )

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Multiplication Table</title>
        <style>
            * {{
                box-sizing: border-box;
            }}
            body {{
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
                font-family: 'Segoe UI', sans-serif;
            }}
            .card {{
                background: #fff;
                width: 90%;
                max-width: 380px;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 15px 30px rgba(0,0,0,0.2);
                text-align: center;
                animation: fadeIn 0.6s ease-in-out;
            }}
            h2 {{
                margin-bottom: 15px;
                color: #333;
            }}
            input {{
                width: 100%;
                padding: 12px;
                font-size: 16px;
                border-radius: 8px;
                border: 1px solid #ccc;
                outline: none;
                margin-bottom: 12px;
            }}
            input:focus {{
                border-color: #667eea;
            }}
            button {{
                width: 100%;
                padding: 12px;
                font-size: 16px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.3s;
            }}
            button:hover {{
                background: #5a67d8;
            }}
            table {{
                width: 100%;
                margin-top: 18px;
                border-collapse: collapse;
            }}
            td {{
                padding: 8px;
                font-size: 16px;
                border-bottom: 1px solid #eee;
            }}
            tr:last-child td {{
                border-bottom: none;
            }}
            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                    transform: translateY(10px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            @media (max-width: 400px) {{
                .card {{
                    padding: 18px;
                }}
                td {{
                    font-size: 14px;
                }}
            }}
        </style>
    </head>
    <body>

        <div class="card">
            <h2>Multiplication Table</h2>

            <form method="POST">
                <input type="number" name="number" placeholder="Enter a number" required value="{number}">
                <button type="submit">Generate Table</button>
            </form>

            <table>
                {rows}
            </table>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
