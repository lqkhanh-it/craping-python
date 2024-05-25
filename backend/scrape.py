import subprocess

def scrape_data(url):
    command = f"scrapy crawl google -a target_url={url}"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("Output: %s, Error: %s", output, error)
    scraped_data = process.communicate()[0].decode()
    return scraped_data