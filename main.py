import re

import httpx
from lxml import html

# read from the html file exported from APVision photo download page
with open("apvision-photo-download-page.php", "r", encoding="utf-8") as file:
    content = file.read()

# parse the html file locally to obtain the 59 or so photo ids
tree = html.fromstring(content)
photos = tree.xpath("//div[@id='selectgsbg']/a/@onclick")
photo_ids = [re.search(r"'([a-z0-9]{32})'", photo).group(1) for photo in photos]

# download each photo
counter = 1
for id in photo_ids:
    # replace this with the right url by doing a trial high res download from apvision (there are query params like "p", "fp", and "did" that we cannot determine automatically)
    url = f"https://www.apvisions.com/_app/sy-inc/store/freedownload.php?p=b7aadaa9a2a5f866214d62616a49c72e&fp=1c383cd30b7c298ab50293adfecb7b18&did=aebf428799f36456510413c389b740f9&dem=org&gsbgphoto={id}"
    with httpx.stream("GET", url) as response:
        response.raise_for_status()
        file_path = f"eleanor-chan-{'0' + str(counter) if counter < 10 else counter}.jpg"
        with open(file_path, "wb") as file:
            for chunk in response.iter_bytes():
                file.write(chunk)
    print(f"file downloaded successfully: {file_path}")
    counter += 1
