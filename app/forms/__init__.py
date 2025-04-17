from .auth.register import RegisterForm
from .connect.add_connect import AddConnectForm
from .connect.create import ConnectCreateForm
from .document.create import DocumentCreateForm
from .email_register.register import EmailRegisterForm
from .forum.create import ForumCreateForm
from .profile.update import ProfileUpdateForm

__all__ = [
    "ProfileUpdateForm",
    "DocumentCreateForm",
    "AddConnectForm",
    "ConnectCreateForm",
    "RegisterForm",
    "ForumCreateForm",
    "EmailRegisterForm",
]
