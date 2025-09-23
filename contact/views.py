# contact/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Email to Admin
            admin_subject = f"🌙 New Contact Request from {name}: {subject}"
            admin_message = (
                f"You've received a new message from your portfolio contact form.\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n\n"
                f"Message:\n{message}\n\n"
                "Please respond to the sender at your earliest convenience. 🌙"
            )
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],  # admin email
                fail_silently=False,
            )

            # Confirmation Email to Sender
            sender_subject = "🌙 Thank you for reaching out to Nila!"
            sender_message = (
                f"Hi {name},\n\n"
                "Thank you so much for getting in touch! I appreciate you taking the time to write.\n"
                "I have received your message and will get back to you as soon as possible.\n\n"
                "Here's a copy of your message:\n"
                f"\"{message}\"\n\n"
                "In the meantime, feel free to explore my portfolio and projects online.\n\n"
                "Warm regards,\n"
                "Nila Ramamoorthy 🌙"
            )
            send_mail(
                sender_subject,
                sender_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})


def contact_success(request):
    return render(request, "contact/success.html")
