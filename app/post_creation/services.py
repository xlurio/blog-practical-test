from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


def send_email_to_staff_members(author: AbstractUser):
    """Sends an e-mail to all staff member to notify a post was made"""

    members = get_user_model().objects.filter(is_staff=True)
    send_mail(
        subject=f"New Post from {author.full_name}",
        message="A new post was created",
        from_email="donotreply@someblog.com",
        recipient_list=[member.email for member in members],
    )
