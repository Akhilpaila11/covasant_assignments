import requests, os
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def download(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        print(f"Success with {url}")
        return url, r.text
    except:
        print(f"Failed to load {url}")
        return url, None

def make_absolute(base, link):
    if link.startswith('http'):
        return link
    elif link.startswith('/'):
        parts = base.split('/')
        return parts[0] + '//' + parts[2] + link
    else:
        return base.rstrip('/') + '/' + link

def extract_links(html, base):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        abs_link = make_absolute(base, a['href'])
        if abs_link.startswith('http'):
            links.append(abs_link)
    return links

def save(url, html, folder='pages'):
    if html:
        os.makedirs(folder, exist_ok=True)
        name = url.replace('http://', '').replace('https://', '').replace('/', '_')
        with open(f'{folder}/{name}.html', 'w') as f:
            f.write(html)

def main(start_url):
    url, html = download(start_url)
    if not html: return
    links = extract_links(html, start_url)
    print(f"Found {len(links)} links.")
    with ThreadPoolExecutor(10) as ex:
        for fut in ex.map(download, links):
            save(*fut)

if __name__ == "__main__":
    main("https://notepadfromdas.pythonanywhere.com/pad/share")
