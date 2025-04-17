from .category import CategoryAdmin
from .comment import Comment
from .connect import ConnectAdmin
from .connect_ticket import ConnectTicketAdmin
from .document import DocumentAdmin
from .email_register import EmailRegisterAdmin
from .extracurricular_activity import ExtracurricularActivityAdmin
from .forum import ForumAdmin
from .slider import SliderAdmin
from .student import StudentAdmin
from .subject import SubjectAdmin
from .tag import TagAdmin

__all__ = [
    "DocumentAdmin",
    "StudentAdmin",
    "SubjectAdmin",
    "CategoryAdmin",
    "ExtracurricularActivityAdmin",
    "TagAdmin",
    "SliderAdmin",
    "EmailRegisterAdmin",
    "Comment",
    "ForumAdmin",
    "ConnectAdmin",
    "ConnectTicketAdmin",
]
