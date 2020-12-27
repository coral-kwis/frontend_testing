from src.commons import constants


class CredentialUtil(object):
    @staticmethod
    def get_admin_username():
        admin_user = constants.ADMIN_USER
        if not admin_user:
            raise Exception('The admin credentials "ADMIN_USER" should be in env variables')
        else:
            return admin_user

    @staticmethod
    def get_admin_password():
        admin_pwd = constants.ADMIN_PWD
        if not admin_pwd:
            raise Exception('The admin credentials "ADMIN_PASSWORD" should be in env variables')
        else:
            return admin_pwd

    @staticmethod
    def get_username(user):
        return user['users']

    @staticmethod
    def get_password(user):
        return user['password']
