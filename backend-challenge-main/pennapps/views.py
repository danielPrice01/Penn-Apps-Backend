from django.contrib.auth import login as auth_login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from pennapps.models import Applicant
from pennapps.models import Application

# Create your views here.


def index(request):
    return render(request, 'pennapps/index.html')


def application(request):
    return render(request, 'pennapps/application.html')


def application_signup(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':

        if hasattr(request.user, 'application'):
            messages.error(request, 'You have already submitted an application.')
            return redirect('index')

        school = request.POST["school"]
        year = request.POST["year"]
        phone_number = request.POST["phone_number"]
        birthday = request.POST["birthday"]
        q1 = request.POST["q1"]
        q2 = request.POST["q2"]

        applicant = request.user
        team_member_1 = request.POST.get('team_member_1', '')
        team_member_2 = request.POST.get('team_member_2', '')
        team_member_3 = request.POST.get('team_member_3', '')

        team_members = [team_member_1, team_member_2, team_member_3]

        if school == ""\
                or year == "nth"\
                or phone_number == ""\
                or birthday == ""\
                or q1 == ""\
                or q2 == "":
            messages.error(request, 'Please Enter All Fields')
            return redirect('application')

        application = Application(
            school_attending=school,
            student_year=year,
            student_major=request.POST.get('major', ''),
            phone_number=phone_number,
            student_birthday=birthday,
            short_answer_1=q1,
            short_answer_2=q2,
            first_hackathon=request.POST.get('first_hackathon', False),
            team_member1=team_member_1,
            team_member2=team_member_2,
            team_member3=team_member_3,
            applicant=applicant
            )
        application.save()

        applicant.application = application
        applicant.save()

        for team_member in team_members:
            if team_member != '':
                try:
                    team_applicant = Applicant.objects.get(username=team_member)
                    team_applicant.application = applicant
                    team_applicant.save()
                except Applicant.DoesNotExist:
                    messages.error(request, f'team member {team_member} is not registered')

        return redirect('index')

    return render(request, 'pennapps/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        password = request.POST['password']

        new_user = Applicant.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name)

        if email.endswith("@upenn.edu"):
            new_user.is_penn_student = True

        new_user.save()
        return redirect('login')

    return render(request, 'pennapps/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            return redirect('login')

        try:
            applicant = Applicant.objects.get(username=username)
        except Applicant.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

        if not applicant.check_password(password):
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

        auth_login(request, applicant)
        return render(request, 'pennapps/index.html')

    return render(request, 'pennapps/login.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('index')
