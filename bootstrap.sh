# update packages
sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libsasl2-dev libldap2-dev libssl-dev libncurses5-dev  libncursesw5-dev xz-utils tk-dev unixodbc-dev

wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
tar xvf Python-3.6.3.tgz
cd Python-3.6.3
sudo chown -R vagrant:vagrant *
./configure
make -j8
sudo make altinstall

sudo apt-get -y install python3-pip

sudo python3.6 -m pip install --upgrade pip

# install all requirements.txt
find ~ -name 'requirements.txt' -exec sudo python3.6 -m pip install -r {} \;
