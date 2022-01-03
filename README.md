# DRFTask

Virtualenv kurulumu

    python -m venv env
    env\Scripts\activate
Daha sonra bağımlılıkların yüklenmesi için

    pip install -r requirements.txt
Uygulamada manage.py nin bulunduğu dizinde aşağıdaki komut ile uygulama ayağa kaldırılabilir.

    python manage.py runserver localhost:8000

Projede ekli bulunan kullanıcılar


Proje Yöneticisi kullanıcısı

    Username : manager
    Password : manager123

Normal kullanıcılar

    Username : user1,user2,user3,user4,user5
    Password : user1234


Yeni kullanıcı eklemek için

    http://localhost:8000/users/register
    {
        "username": "",
        "password": "",
        "password2": "",
        "isProjectManager": false
    }

JWT Token oluşturmak için

    http://localhost:8000/token/
    {
        "username": "",
        "password": ""
    }
    http://localhost:8000/token/refresh/
    {
        "refresh": ""
    }

Proje eklemek için

    post http://localhost:8000/projects
    {
 	    "name": "Project 10",
	    "description": "Project 10 sadadasdasdxxxxx",
	    "start_date": "2022-01-01T06:05:01Z",
	    "deadline": "2022-01-29T06:05:04Z"
    }

Kullanıcı proje yönetici ise istediği tüm projeleri listeleyebilir ve kullanıcı filtreleyebilir.
Normal kullanıcılar ise sadece kendi projelerini listeleyebilirler.

    get http://localhost:8000/projects?user=user5


Herhangi bir projeyi düzenleme işlemini sadece Projeyi oluşturan kullanıcı veya Proje Yöneticisi kullanıcısı düzenleyebilir.

    update http://localhost:8000/projects/1

Proje silme işlemini sadece Proje Yöneticisi kullanıcısı yapabilir.

    delete http://localhost:8000/projects/1
