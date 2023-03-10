# DjangoRestRegis

Installation : 

1. Install Python 3.11.2 from https://www.python.org/downloads/release/python-3112/.
2. After installation navigate to `DjangoRestRegis` folder in your terminal/cmd and run the following command to create a virtual env :
`python3.11 -m venv env`
3. Next run `source env/bin/activate  # On Windows use env\Scripts\activate` to activate the virtual env.
4. Run `pip install -r requirements.txt` to install the required python packages.
5. Now run `python manage.py migrate` to create the DB tables.
6. Then run `python manage.py runserver <port-number>` (default port is 8000) to start the djangorest server.

APIs :

1. POST `register`:
    curl command - `curl --location 'http://127.0.0.1:8000/register' \
--header 'Accept: application/json; indent=4' \
--header 'Cookie: csrftoken=PdtntmrYgb7vJHwNVEMSM1rgp2Cv32w0' \
--form 'username="Tom"' \
--form 'name="Tom Mathew"' \
--form 'password="tommy12345"' \
--form 'confirm_password="tommy12345"' \
--form 'email="tommy@email.com"' \
--form 'mobile="+918123456789"' \
--form 'country="India"' \
--form 'nationality="India"' \
--form 'role="student"'`
    Request body fields - username, name, password, confirm_password, email, mobile, country, nationality, role(student/admin/editor/staff).
    
2. POST `login/`
    curl command - `curl --location 'http://127.0.0.1:8000/login/' \
--header 'Cookie: csrftoken=PdtntmrYgb7vJHwNVEMSM1rgp2Cv32w0' \
--form 'username="Tom"' \
--form 'password="tommy12345"'`
    Request body fields - username, password

3. GET `mainapp/student/`
    Authentication - Bearer token(use the access token from `login/`).
    Access limited to student users.
4. GET `mainapp/admin/`
    Authentication - Bearer token(use the access token from `login/`).
    Access limited to admin users.
5. GET `mainapp/editor/`
    Authentication - Bearer token(use the access token from `login/`).
    Access limited to editor users.
6. GET `mainapp/staff/`
    Authentication - Bearer token(use the access token from `login/`).
    Access limited to staff users.
