#!/usr/bin/python3
"""
Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from tqdm import tqdm
import argparse
import time


CHROME_PATH = '/usr/bin/chromium-browser'
CHROMEDRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
WINDOW_SIZE = "800,600"


def initialize_driver():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    return driver

def watch_jacek():
    driver = initialize_driver()
    URL = "https://www.youtube.com/watch?v=llmeDxk21dU"
    driver.get(URL)
    for _ in tqdm(range(343)):
        time.sleep(1)
    driver.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--iterations', '-i', required=True, help='How many times movie will be repeated')
    args = parser.parse_args()

    print("[LOG] Started watching...")
    for i in range(int(args.iterations)):
        print("[LOG]: Iteration: {0}/{1}".format(i+1, int(args.iterations)))
        watch_jacek()
    print("[LOG] Finished watching...")


if __name__ == "__main__":
    main()