from backend.model.UserModel import User

class UserDAO():

    @staticmethod
    def createUser(nome,email,senha):
        try:
            User.objects.create(nome=nome,email=email,senha=senha)
        except:
            return None


    @staticmethod
    def getUserByEmailAndPassowrd(email, senha):
        try:
            return User.objects.get(email=email, senha=senha)
        except:
            return None

    @staticmethod
    def getUserByEmail(email):
        try:
            return User.objects.get(email=email)
        except:
            return None

    @staticmethod
    def getUserById(user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return None

    @staticmethod
    def updateUser(user_id, novo_nome=None, novo_email=None, nova_senha=None):
        user = User.getUserById(user_id)
        if user:
            if novo_nome:
                user.nome = novo_nome
            if novo_email:
                user.email = novo_email
            if nova_senha:
                user.senha = nova_senha
            user.save()
            return user
        return None

    @staticmethod
    def deleteUser(user_id):
        user = User.getUserById(user_id)
        if user:
            user.delete()
            return True
        return False






