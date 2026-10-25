#BeautifulSoup modulu 


my_html="""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neon Dijital Saat</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #0f172a; /* Koyu lacivert arka plan */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .card {
            background: #1e293b;
            padding: 40px 60px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 
                        0 0 20px rgba(56, 189, 248, 0.2);
            border: 1px solid #334155;
        }

        .time {
            font-size: 5rem;
            font-weight: bold;
            color: #38bdf8; /* Neon mavi */
            text-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
            letter-spacing: 4px;
            margin-bottom: 10px;
            font-variant-numeric: tabular-nums;
        }

        .date {
            font-size: 1.2rem;
            color: #94a3b8;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
    </style>
</head>
<body>

    <div class="card">
        <div class="time" id="timeDisplay">00:00:0
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(my_html,'html.parser')

result=soup.prettify()

print(result.title)


print(soup.head.parent.name)