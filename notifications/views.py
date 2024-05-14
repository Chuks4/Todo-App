from django.shortcuts import render


# Create your views here.
def notifications(request):
    owner = request.user.profile
    notifications = owner.notification.filter(read=False).order_by("-created")
    context = {"notifications": notifications}
    return render(request, "notifications.html", context)


def read_notifications(request, pk):
    owner = request.user.profile
    read_notification = owner.notification.get(id=pk)
    if not read_notification.read:
        read_notification.read = True
        read_notification.delete()

    context = {"notifications": read_notification}
    return render(request, "read_notifications.html", context)