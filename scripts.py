from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject, Commendation
import random


COMMENDATIONS = [
    "Молодец",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше чем я ожидал!",
    "Великолепно!",
    "Прекрасно",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается все лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится"
    ] 


def check_name(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.MultipleObjectsReturned:
        return "Введено неуникальное имя, уточните Ф.И.О"
    except Schoolkid.DoesNotExist:
        return "Пользоваеля с таким именем не существует. Проверьте правильность введенного Ф.И.О"


def check_subject(subject):
    try:
        return Subject.objects.get(title__contains=subject)
    except Subject.DoesNotExist:
        return "Введено некорректное имя предмета"


def fix_marks(schoolkid):
    marks_bad = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks_bad:
        mark.points = 5
        mark.save()


def remove_chastiments(schoolkid):
    chastiments = Chastisement.objects.filter(schoolkid=schoolkid)
    chastiments.delete()


def create_commendation(schoolkid, subject):
    commendation = random.choice(COMMENDATIONS)

    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid)
    
    lesson_last = Lesson.objects.filter(
        subject__title=subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
        ).order_by("-date").first()
    
    Commendation.objects.create(
        text=commendation,
        created=lesson_last.date,
        schoolkid=schoolkid,
        subject=lesson_last.subject,
        teacher=lesson_last.teacher
        )
