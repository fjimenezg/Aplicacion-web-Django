from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from global_.manager_connection import ManagerConnection

def check_user(username, password):
    conn = ManagerConnection('postgresql',"mario",'123',"5432","localhost",dbname="estudiantes")
    data = conn.managerSQL("select * from estudiante where nombre='"+username+"' and codigo_e="+password)
    if len(data) > 0:
        return True
    return False

class CustomBackend(object):

    def authenticate(self, request=None, **kwargs):
        if request is None:
            return None
                
        try:
            username = kwargs[get_user_model().USERNAME_FIELD]
            password = kwargs['password'] 
            if check_user(username, password):
                user = User.objects.create_user(username=username, password=password)
                print("#########################")
                return user     
        except:
            return None
            
        return None


    def get_user(self, user_id):
        print("--------------------------------")
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
