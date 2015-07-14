# gyazoCrawler

**gyazoCrawler is a python scrip to index and download Gyazo screenshots.**

Usage
--
Edit the ```main.py``` file variables with your cookies and files/folders. Run it with py2 and you will have 2 main options:
1. Download/Index database of gyazos - will fetch gyazo.com and create your database of links;
2. Calculate the size and download the all the images from the DB - will calculate the size from the database file, and then ask if you want them to be downloaded, if so they will go on the specified folder.

Disclaimer
--
I'm not affiliated with Gyazo in any way.

For the Gyazo team/company:
 - You guys are awesome;
 - I could not find anything that explicitly said, that this practice of recovering and downloading old *gyazos* was against your policy.
 - I completely understand that you may not like this, if you want to stop it you should  remove 
```"url"```,```"permalink_url"``` and ```"permalink_path"``` 
from the JSON response
 - If you wish the removal of this repo just tweet me [@tofran_] and I’ll do it as soon as possible.

License
--
MIT
[@tofran_]:https://twitter.com/tofran_