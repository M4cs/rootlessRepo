# rootlessRepo
Basic local repository script for AltichaDev's rootlessJB installer.

# Requirements:

- Python3
- rootlessJBInstaller from @AltichaDev

# Instructions:

1. Run `python3 rootlessRepo.py`.

2. Place any **patched debs** you would like to install in the same directory as rootlessRepo.

3. In another terminal run `ipconfig` on Windows or `ifconfig` on Linux/MacOS. Find you Local IP for the current network adapter you are using and remember it.

4. Open up rootlessJBInstaller on your iDevice. 

5. In the deb URL enter `https://<local-ip>:8081/<name-of-deb-file>.deb` and press exploit.

6. Press install when done exploiting.

**Not sure how Insidious works yet but I will update this to work with it once it releases.**
