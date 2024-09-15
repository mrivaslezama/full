# Create python3-virtualenv
python3 -m venv .venv
# Activate python3-virtualenv
source .venv/bin/activate
# Actualizar pip
pip install --upgrade pip
pip install reflex
reflex init
reflex run
#reflex export --frontend-only
#rm -fr public
#unzip frontend.zip -d public
#rm -f frontend.zip
#deactivate
#git add .
#git commit -m "build1"
# git push

code .
#pip install -r requirements.txt
# You can checkout you virtualenv version
#virtualenv --version
# Check yuo python version on this virtualenv
#python --version
# Check yuo pip version on this virtualenv
#pip --version
# When you finish working, you can deacgtivate your virtualenv
# deavtivate