# python
sudo yum update -y
sudo yum install python3 python3-pip git -y
sudo amazon-linux-extras install nginx1 -y

Application Setup
mkdir ~/myapp && cd ~/myapp

Create virtual environment
source ~/myapp/venv/bin/activate

Update pip and setuptools
pip install --upgrade pip setuptools

Install dependencies
pip install -r requirements.txt

Test Application Locally
python ~/myapp/app.py

Test API (in a new terminal or after stopping the app with Ctrl+C)
curl http://localhost:5000/api/data

Production Setup with Gunicorn
Test Gunicorn:
gunicorn --config ~/myapp/gunicorn_config.py app:app

--------------------------------------------------------------------------
