# APVisions Photo Downloader
This application allows you to download all digital photos of your kids from a photo session taken by APVisions (apvisions.com) at their schools.

To run this:
- clone the repo and run `uv sync` (if you don't have `uv` installed, run `pipx install uv`)
- log into APVisions with your kids' password
- on the photo download page, export the html file as `apvision-photo-download-page.php` and save it to the root folder of this repo.
- perform one download; capture that download url and modify the `url` variable in `main.py`
- run `main.py` and the script will download all 60 or so photos of your kids with all background options.
