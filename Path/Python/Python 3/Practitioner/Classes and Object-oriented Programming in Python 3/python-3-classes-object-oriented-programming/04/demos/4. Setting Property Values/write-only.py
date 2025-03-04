# Write-only property
# Raise an error inside of the 'getter' method

@property
def password(self):
    raise AttributeError("Password is write-only")


@password.setter
def password(self, password):
    # hash password here
    self._password = password
