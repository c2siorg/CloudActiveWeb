import os
import sys
from multiprocessing import Pool

import pandas as pd
from tqdm import tqdm


def download_content(url):
    try:
        command = "wget --recursive --level 1 --no-clobber --page-requisites --html-extension --convert-links " \
                  "--reject '*.apk,*.zip,*.exe,*.ico,*.gif,*.svg,*.jpg,*.jpeg,*.png,*.mp3,*.mp4,*.pdf,*.tgz,*.flv,*.avi,*.mpeg,*.iso'" \
                  "--restrict-file-names=windows --domains {} --no-parent https://{}".format(
                      url, url)
        os.system(command)
        return 1
    except:
        return 0


VM = int(sys.argv[1])
THREAD = int(sys.argv[2])
SEED_LIST = pd.read_csv(
    'stp-5-wb-non-inset-200feed.csv').apex.tolist()

if __name__ == '__main__':
    with Pool(THREAD) as p:
        r = list(
            tqdm(p.imap(download_content, SEED_LIST[(15000 * VM):(15000 + (15000 * VM))])))
        if all(r):
            print("success")
        else:
            print("some errors has occurred")

# python3 active.py [0,1,2,3] 128
# eg - python3 active.py 3 128
