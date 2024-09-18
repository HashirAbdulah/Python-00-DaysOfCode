# MultiProcessing is the cpu bound task in which cpu is used for completing the given tasks like heavu computations. In the given example the request modules get the url and download the files using multiprocess.... Multiprocessing is suitable for CPU-bound tasks, like computations or data processing.

import multiprocessing
import requests
import os
import shutil

def download_file(url,name):
    print(f"Download Started {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"


if __name__ == '__main__':
    if os.path.exists("files"):
        shutil.rmtree("files")
    else:
        os.makedirs("files")
        pros = []
        for i in range(20):
            p = multiprocessing.Process(target=download_file, args=(url,i))
            p.start()
            pros.append(p)
        for p in pros:
            p.join()
