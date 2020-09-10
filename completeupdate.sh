su # Requests sudo permissions once at the beginning. I think.

pacman -Syu --noconfirm
pip3 install --find-links https://www.tortall.net/~robotpy/wheels/2020/linux_x86_64/ -r requirements.txt --upgrade
git pull
