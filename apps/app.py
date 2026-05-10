from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Taiwo DevOps Challenge</title>

        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family: Arial, sans-serif;
            }

            body{
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
            }

            .container{
                text-align:center;
                background: rgba(255,255,255,0.08);
                padding:50px;
                border-radius:20px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.4);
                width: 80%;
                max-width:700px;
            }

            h1{
                font-size:42px;
                margin-bottom:20px;
                color:#38bdf8;
            }

            p{
                font-size:20px;
                margin-bottom:15px;
                line-height:1.6;
            }

            .status{
                display:inline-block;
                margin-top:20px;
                padding:12px 25px;
                background:#22c55e;
                color:white;
                border-radius:30px;
                font-weight:bold;
                font-size:18px;
            }

            footer{
                margin-top:30px;
                font-size:14px;
                color:#cbd5e1;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1> DevOps Deployment Successful</h1>

            <p>
                Welcome to <strong>Taiwo Peter Olatunji's</strong>
                Production-Ready DevOps Challenge Project.
            </p>

            <p>
                This application is fully containerized using Docker,
                deployed on AWS ECS Fargate,
                automated with GitHub Actions CI/CD,
                and monitored using AWS CloudWatch.
            </p>

            <div class="status">
                ✅ Application Running Successfully
            </div>

            <footer>
                DevOps Engineer Practical Challenge | AWS • Docker • ECS • Terraform • CI/CD
            </footer>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Taiwo DevOps Challenge App Running Successfully!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)