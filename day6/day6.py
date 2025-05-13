import os
import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_links(url):
    try:
        print(f"Fetching page: {url}")
        res = requests.get(url)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f'Error fetching {url}: {e}')
        return []

    soup = BeautifulSoup(res.text, 'html.parser')
    links = set()

    for tag in soup.find_all('a', href=True):
        full_url = urljoin(url, tag['href'])
        links.add(full_url)

    return list(links)

async def save_links(session, url, folder="downloads"):
    try:
        async with session.get(url) as resp:
            if resp.status != 200:
                print(f"Skipped {url} (status code {resp.status})")
                return

            content = await resp.read()
            parsed = urlparse(url)
            filename = os.path.basename(parsed.path) or "index.html"
            if not filename.endswith('.html'):
                filename += '.html'

            os.makedirs(folder, exist_ok=True)
            filepath = os.path.join(folder, filename)

            with open(filepath, 'wb') as f:
                f.write(content)

            print(f'Saved: {url} -> {filepath}')
    except Exception as e:
        print(f"Failed to download {url}: {e}")

async def download_all(links):
    async with aiohttp.ClientSession() as session:
        tasks = [save_links(session, url) for url in links]
        await asyncio.gather(*tasks)

def Srt_download(start_url):
    links = extract_links(start_url)

    if not links:
        print('No links found. Exiting.')
        return

    print(f"Found {len(links)} links. Starting download...\n")
    asyncio.run(download_all(links))

if __name__ == "__main__":
    start_url = "https://notepadfromdas.pythonanywhere.com/pad/share"
    Srt_download(start_url)
