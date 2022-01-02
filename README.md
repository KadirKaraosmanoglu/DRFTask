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
Kullanıcı proje yönetici ise istediği kullanıcıyı filtreleyebilir.
Normal kullanıcılar sadece kendi projelerini listeleyebilir.

    get http://localhost:8000/projects?user=user5


Herhangi bir projeyi düzenleme işlemini sadece Projeyi oluşturan kullanıcı veya Proje Yöneticisi kullanıcısı düzenleyebilir.

    update http://localhost:8000/projects/1

Proje silme işlemini sadece Proje Yöneticisi kullanıcısı yapabilir.

    delete http://localhost:8000/projects/1
