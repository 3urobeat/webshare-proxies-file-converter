# webshare-proxies-file-converter

In steam-comment-service-bot v2.16 a `proxyFormat` setting was introduced, allowing users to specify a structure differing from the default.  
For webshare.io the format `http://ip:port:username:password` should be used. Please see the [official proxies documentation](https://github.com/3urobeat/steam-comment-service-bot/blob/beta-testing/docs/wiki/adding_proxies.md) to see if something changed.  

This project is therefore now obsolete and has been archived.

&nbsp;

**===================== Original README =====================**

&nbsp;

Quick and dirty lil py script to convert the https://webshare.io proxy file to something https://github.com/3urobeat/steam-comment-service-bot understands  

File must be in the same directory as this script and named "input.txt"  
The script will create and write to a file called "proxies.txt" so that you can instantly copy it to the folder of your steam-comment-service-bot installation.  

To run, open a terminal in this folder and run the script with python: `python proxyConverter.py`  
