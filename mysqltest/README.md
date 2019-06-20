# MySQL DB Django create

### Configuration
Django v2.1  
MySQL v5.7  
MySQL user authority all and DBname

| item           |  content       |
| :------------- | :------------- |
| DBname         | dbtest         |
| username       | testuser       |
| password       | testpassword   |
| host           | 127.0.0.1      |
| port           | 3306           |

### pymysql install
pip install pymysql

## Django project add

### manage.py code add
```
import pymysql

pymysql.install_as_MySQLdb()

```

### settings.py code change

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbtest',
        'USER': 'testuser',
        'PASSWORD': 'testpassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
