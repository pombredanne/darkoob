import os
import sys
import datetime
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath('test.py')), '..'))
sys.path.append(ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = 'darkoob.settings'

from django.core.management import setup_environ
from django.contrib.auth.models import User
from django.core.files import File
from django.utils import timezone
from avatar.models import Avatar
from darkoob import settings
from darkoob.social.models import UserNode
from darkoob.book.models import Author, Quote, Publisher, Book, Language
from darkoob.group.models import Group, Schedule, Deadline
from darkoob.post.models import Post


AVATARS_DIR = 'avatars'
BOOKS_DIR = 'books'

# Add users
first_user = None
try:
    first_user = User.objects.get(pk=1)
    first_user.first_name = "First"
    first_user.last_name = "Last"
    first_user.save()
except Exception, e:
    print e

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

if not first_user:
    first_user = User.objects.get(pk=1)

# Add avatars
ad = os.path.join('media', AVATARS_DIR)
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
bd = os.path.join('media', BOOKS_DIR)
if not os.path.exists(bd):
    os.makedirs(bd)
book_thumbs = {
    'the_alchemist': 'the_alchemist.jpg',
    'pride_and_prejudice': 'pride_and_prejudice.jpg',
}
for k in book_thumbs:
    shutil.copy(
        os.path.join('test', BOOKS_DIR, book_thumbs[k]),
        os.path.join('media', BOOKS_DIR)
    )
    book_thumbs[k] = os.path.join(BOOKS_DIR, book_thumbs[k])

the_alchemist = Book.objects.create(
    title='The Alchemist',
    publisher=harpercollins,
    language=english,
    thumb=os.path.join(BOOKS_DIR, 'the_alchemist.jpg'),
)
the_alchemist.authors.add(paulo_coelho)
the_alchemist.tags.add('Fantasy', 'Spirituality')

pride_and_prejudice = Book.objects.create(
    title='Pride and Prejudice',
    publisher=modern_library,
    language=english,
    thumb=os.path.join(BOOKS_DIR, 'pride_and_prejudice.jpg'),
)
pride_and_prejudice.authors.add(jane_austen)
pride_and_prejudice.tags.add('Classics', 'Romance')

# Favorite books
first_user.userprofile.favorite_books.add(pride_and_prejudice, the_alchemist)

# Add quotes
q1 = Quote.objects.create(
    author=albert_einstein,
    user=sina_mahmoodi,
    text="Two things are infinite: the universe and human stupidity; and I'm\
    not sure about the universe.",
)
q2 = Quote.objects.create(
    author=dr_seuss,
    user=first_user,
    text="Don't cry because it's over, smile because it happened.",
)

# Add groups
bookworms = Group.objects.create(name='Bookworms', admin=first_user, created_time=timezone.now())
bookworms.members.add(afshin_rodgar, vahid_kharazi, aryan_baghi, sina_mahmoodi)

# Add schedules
the_alchemist_schedule = Schedule.objects.create(
    group=bookworms,
    book=the_alchemist,
)

# Add deadlines
tas_deadline_1 = Deadline.objects.create(
    schedule=the_alchemist_schedule,
    from_page=1,
    to_page=45,
    start_time=timezone.now(),
    end_time=timezone.now() + datetime.timedelta(days=5),
    submitted_time=timezone.now(),
)

# Add posts
p1 = Post.objects.create(
    user=first_user,
    text="Anna Quindlen is the winner of the 1992 Pulitzer Prize for commentary\
    and the author of three bestselling novels, most recently Black and Blue, a\
    children's book, Happily Ever After, and an inspirational book, A Short\
    Guide to a Happy Life.",
    submitted_time=timezone.now(),
)

p2 = Post.objects.create(
    user=first_user,
    text="Deep learning is based on the theory\
    that - \"human intelligence stems from a single algorithm\".\
    \
    It, basically, involves development of (artificial) neural networks that\
    can gather information and can understand what objects can look\
    like (not restricted to just what they look like).\
    So you provide the system with a huge amount of data so that the\
    system can itself learn from that data.",
    submitted_time=timezone.now() - datetime.timedelta(days=-2),
)

p3 = Post.objects.create(
    user=first_user,
    text="""Another area where i see a lot of potential is automation of legal\
    work helping the lawyers a lot. This is because there is a lot of legal\
    work that doesn't require a huge amount of skill (or finding loopholes)\
    but a lot of knowledge and can be automated.""",
    submitted_time=timezone.now() - datetime.timedelta(hours=-5),
)

p4 = Post.objects.create(
    user=vahid_kharazi,
    text="""I only dabble in learning, so I can't say much here. However,\
    as the difficulty of problems we are looking at is increasing rapidly\
    (from simple classification to predicting all kinds of structure) the\
    need for newer tools and better algorithms is constantly there. Of\
    late "deep learning" techniques have also burst into the scene,\
    and, at least in terms of computer vision, there are indications\
    these "off-beat" (in some sense; what in science is ever\
    mainstream?) algorithms may perhaps end up becoming\
    the method of choice.""",
    submitted_time=timezone.now(),
)


