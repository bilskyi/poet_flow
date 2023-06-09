from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username=None, email=None, phone=None, password=None, **kwargs):
        '''
        Creates and saves a User with the given email and password
        '''
        if not username:
            if not email and not phone:
                raise ValueError('The given email/phone must be set')
        
        if email:
            email = self.normalize_email(email)

            if not username:
                username = email
            
            user = self.model(
                email=email,
                username=username,
                **kwargs
            )
        
        if phone:
            if not username:
                username = phone
            
            user = self.model(
                username=username,
                phone=phone,
                **kwargs
            )

        if kwargs.get('is_superuser'):
            user = self.model(
                username=username,
                **kwargs
            )
            
        user.set_password(password)
        user.save(using=self._db)
        return user  # Return the created user instance

    def create_user(self, username, email, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(username=username, email=email, password=password, **kwargs)
    
    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_superuser') is not True:  # Corrected the condition
            raise ValueError('Super user must have is_superuser=True')
        
        return self._create_user(
            username=username,
            password=password,
            **kwargs
        )
