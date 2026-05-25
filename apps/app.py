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
        <title>Taiwo DevOps Portfolio</title>

        <style>

            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family: Arial, sans-serif;
            }

            body{
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color:white;
            }

            /* NAVBAR */

            nav{
                width:100%;
                background:#020617;
                padding:20px 50px;
                display:flex;
                justify-content:space-between;
                align-items:center;
                position:fixed;
                top:0;
                z-index:1000;
                box-shadow:0 4px 10px rgba(0,0,0,0.4);
            }

            nav h2{
                color:#38bdf8;
            }

            nav ul{
                display:flex;
                list-style:none;
                gap:20px;
            }

            nav ul li a{
                text-decoration:none;
                color:white;
                font-weight:bold;
                transition:0.3s;
            }

            nav ul li a:hover{
                color:#38bdf8;
            }

            /* HERO SECTION */

            .hero{
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                text-align:center;
                padding:20px;
            }

            .container{
                background: rgba(255,255,255,0.08);
                padding:60px;
                border-radius:20px;
                width:90%;
                max-width:850px;
                box-shadow:0 8px 25px rgba(0,0,0,0.5);
            }

            h1{
                font-size:50px;
                margin-bottom:20px;
                color:#38bdf8;
            }

            p{
                font-size:20px;
                line-height:1.7;
                margin-bottom:20px;
            }

            .status{
                display:inline-block;
                padding:14px 30px;
                background:#22c55e;
                border-radius:30px;
                font-size:18px;
                font-weight:bold;
                margin-top:20px;
            }

            /* BUTTONS */

            .buttons{
                margin-top:40px;
                display:flex;
                justify-content:center;
                gap:20px;
                flex-wrap:wrap;
            }

            .btn{
                text-decoration:none;
                background:#38bdf8;
                color:#0f172a;
                padding:14px 28px;
                border-radius:30px;
                font-weight:bold;
                transition:0.3s;
            }

            .btn:hover{
                background:white;
                transform:scale(1.05);
            }

            footer{
                text-align:center;
                padding:30px;
                color:#cbd5e1;
                font-size:14px;
                background:#020617;
            }

        </style>
    </head>

    <body>

        <!-- NAVBAR -->

        <nav>

            <h2>DevOps Portfolio</h2>

            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Portfolio</a></li>
                <li><a href="#">Contact</a></li>
            </ul>

        </nav>

        <!-- HERO SECTION -->

        <section class="hero">

            <div class="container">

                <h1>🚀 DevOps Deployment Successful</h1>

                <p>
                    Welcome to <strong>Taiwo Peter Olatunji's</strong>
                    Production-Ready DevOps Portfolio Project.
                </p>

                <p>
                    This application was fully containerized using Docker,
                    deployed on AWS ECS Fargate,
                    automated using GitHub Actions CI/CD,
                    and monitored with AWS CloudWatch.
                </p>

                <div class="status">
                    ✅ Application Running Successfully
                </div>

                <!-- BUTTONS -->

                <div class="buttons">

                    <a href="#" class="btn">About</a>

                    <a href="https://github.com/Taiwo-Peter2023" target="_blank" class="btn">
                        Social Media
                    </a>

                </div>

            </div>

        </section>

        <!-- FOOTER -->

        <footer>
            DevOps Engineer Practical Challenge |
            AWS • Docker • ECS • Terraform • GitHub Actions
        </footer>

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



















# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Taiwo DevOps Challenge</title>

#         <style>
#             *{
#                 margin:0;
#                 padding:0;
#                 box-sizing:border-box;
#                 font-family: Arial, sans-serif;
#             }

#             body{
#                 background: linear-gradient(135deg, #0f172a, #1e293b);
#                 color: white;
#                 height:100vh;
#                 display:flex;
#                 justify-content:center;
#                 align-items:center;
#             }

#             .container{
#                 text-align:center;
#                 background: rgba(255,255,255,0.08);
#                 padding:50px;
#                 border-radius:20px;
#                 box-shadow: 0 8px 25px rgba(0,0,0,0.4);
#                 width: 80%;
#                 max-width:700px;
#             }

#             h1{
#                 font-size:42px;
#                 margin-bottom:20px;
#                 color:#38bdf8;
#             }

#             p{
#                 font-size:20px;
#                 margin-bottom:15px;
#                 line-height:1.6;
#             }

#             .status{
#                 display:inline-block;
#                 margin-top:20px;
#                 padding:12px 25px;
#                 background:#22c55e;
#                 color:white;
#                 border-radius:30px;
#                 font-weight:bold;
#                 font-size:18px;
#             }

#             footer{
#                 margin-top:30px;
#                 font-size:14px;
#                 color:#cbd5e1;
#             }
#         </style>
#     </head>

#     <body>

#         <div class="container">

#             <h1> DevOps Deployment Successful</h1>

#             <p>
#                 Welcome to <strong>Taiwo Peter Olatunji's</strong>
#                 Production-Ready DevOps Challenge Project.
#             </p>

#             <p>
#                 This application is fully containerized using Docker,
#                 deployed on AWS ECS Fargate,
#                 automated with GitHub Actions CI/CD,
#                 and monitored using AWS CloudWatch.
#             </p>

#             <div class="status">
#                 ✅ Application Running Successfully
#             </div>

#             <footer>
#                 DevOps Engineer Practical Challenge | AWS • Docker • ECS • Terraform • CI/CD
#             </footer>

#         </div>

#     </body>
#     </html>
#     """

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)