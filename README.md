### UpTrade test task

1. git clone git@github.com:AnastasiaNB/test_task_UpTrade.git
2. python3 -m venv venv
3. source venv/bin/activate
4. cd test_task/
5. python3 manage.py migrate
6. python3 manage.py runserver

### Endpoints:
- http://127.0.0.1:8000/test_page/index/ (main page)
- http://127.0.0.1:8000/test_page/page-x/ (x = 1-5, pages for parent menu items)
- http://127.0.0.1:8000/test_page/page-x-y/ (x = 2-3, y = 1-3, pages for child menu items)
- http://127.0.0.1:8000/admin/ (admin panel of site, superuser: login - admin, password - admin12345)