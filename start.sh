python3.8 -m venv venv
cd venv
. bin/activate
cd ..
pip install -y wheel
pip install -r requirements.txt -U
#pip install naver-0.0.1-py3-none-any.whl
cd react
yarn install
cd ..
mkdir logs
cd django
./manage.py makemigrations  && ./manage.py migrate
# ./manage.py collectstatic
./manage.py runserver