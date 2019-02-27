# python_scripts
python scripts for system admins

To use Python 3 on CentOS 7. Installation methods are being shared.

sudo yum update

sudo yum -y install yum-utils

sudo yum -y groupinstall development

sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm

sudo yum -y install python36u

python3.6 -V

sudo yum -y install python36u-pip

sudo yum -y install python36u-devel


Once you have installed, you can make virtual environment so that you whatever you install can stay in your virtual env.

mkdir virtualenvs

cd virtualenvs

python3.6 -m venv *virtualenv_name*

source virtualenvs/*virtualenv_name*/bin/activate
