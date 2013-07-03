import os
import sys
import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath('test.py')), '..'))
sys.path.append(ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'darkoob.settings'

from django.core.management import setup_environ
from django.contrib.auth.models import User
from django.core.files import File
from django.utils import timezone
from avatar.models import Avatar
from darkoob import settings
from darkoob.book.models import Author, Quote, Publisher, Book, Language
from darkoob.group.models import Group
from darkoob.post.models import Post


AVATARS_DIR = 'media/avatars'
BOOKS_DIR = 'media/books'

# Add users
try:
    first_user = User.objects.get(pk=1)
    first_user.first_name = "First"
    first_user.last_name = "Last"
except:
    pass

afshin_rodgar = User.objects.create(
    username='afshinrodgar',
    password='afshinrodgar',
    first_name='Afshin',
    last_name='Rodgar',
    email='afshinrodgar@mydarkoobemail.com',
)
sina_mahmoodi = User.objects.create(
    username='sinamahmoodi',
    password='sinamahmoodi',
    first_name='Sina',
    last_name='Mahmoodi',
    email='sinamahmoodi@mydarkoobemail.com',
)
vahid_kharazi = User.objects.create(
    username='vahidkharazi',
    password='vahidkharazi',
    first_name='Vahid',
    last_name='Kharazi',
    email='vahidkharazi@mydarkoobemail.com',
)
aryan_baghi = User.objects.create(
    username='aryanbaghi',
    password='aryanbaghi',
    first_name='Aryan',
    last_name='Baghi',
    email='aryanbaghi@mydarkoobemail.com',
)

# Add avatars
ad = os.path.dirname(AVATARS_DIR)
if not os.path.exists(ad):
    os.makedirs(ad)

# Add userprofiles

# Add authors
albert_einstein = Author.objects.create(name='Albert Einstein')
dr_seuss = Author.objects.create(name='Dr. Seuss')
jane_austen = Author.objects.create(name='Jane Austen')
paulo_coelho = Author.objects.create(name='Paulo Coelho')

# Add publishers
harpercollins = Publisher.objects.create(name='HarperCollins')
modern_library = Publisher.objects.create(name='Modern Library')

# Add languages
english = Language.objects.create(name='English')

# Add books
bd = os.path.dirname(BOOKS_DIR)
if not os.path.exists(bd):
    os.makedirs(bd)

the_alchemist = Book.objects.create(
    title='The Alchemist',
    publisher=harpercollins,
    language=english,
    thumb=bd + 'the_alchemist.jpg',
)
the_alchemist.authors.add(paulo_coelho)
the_alchemist.tags.add('Fantasy', 'Spirituality')

pride_and_prejudice = Book.objects.create(
    title='Pride and Prejudice',
    publisher=modern_library,
    language=english,
    thumb=bd + 'pride_and_prejudice.jpg',
)
pride_and_prejudice.authors.add(jane_austen)
pride_and_prejudice.tags.add('Classics', 'Romance')

# Add quotes
q1 = Quote.objects.create(
    author=albert_einstein,
    user=sina_mahmoodi,
    text="Two things are infinite: the universe and human stupidity; and I'm\
    not sure about the universe.",
)
q2 = Quote.objects.create(
    author=dr_seuss,
    user=User.objects.get(pk=1),
    text="Don't cry because it's over, smile because it happened.",
)

# Add groups
bookworms = Group.objects.create(name='Bookworms', admin=sina_mahmoodi, created_time=timezone.now())
bookworms.members.add(afshin_rodgar, vahid_kharazi, aryan_baghi)

# Add schedules

# Add deadlines

# Add posts
p1 = Post.objects.create(
    user=User.objects.get(pk=1),
    text="Anna Quindlen is the winner of the 1992 Pulitzer Prize for commentary\
    and the author of three bestselling novels, most recently Black and Blue, a\
    children's book, Happily Ever After, and an inspirational book, A Short\
    Guide to a Happy Life.",
    submitted_time=timezone.now(),
)


