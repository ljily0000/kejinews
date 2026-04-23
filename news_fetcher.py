import requests
import datetime
import os

def fetch_top_news(api_key, total=20):
    url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize={total}&category=general"
    headers = {"Authorization": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    articles = data.get('articles', [])
    return articles[:total]

def generate_html(articles):
    html = """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; }
            h2 { color: #2c3e50; }
            ul { padding-left: 18px; }
            li { margin-bottom: 12px; }
            .source { color: #888; font-size: 13px; }
        </style>
    </head>
    <body>
        <h2>🌎 今日全球重要新闻日报</h2>
        <ul>
    """
    for a in articles:
        title = a['title']
        url_ = a['url']
        source = a['source']['name']
        html += f'<li><a href="{url_}">{title}</a> <span class="source">({source})</span></li>'
    html += """
        </ul>
        <p style="font-size:12px;color:#bbb;">自动整理，来源于 NewsAPI</p>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    api_key = os.getenv("NEWSAPI_KEY")
    news = fetch_top_news(api_key)
    html = generate_html(news)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f"daily_news_{today}.html", "w", encoding="utf-8") as f:
        f.write(html)