import factory
from faker import Faker
from pnk_server.users.test.factories import UserFactory


fake = Faker()
user1 = UserFactory.build()


class MissionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'missions.Mission'
        django_get_or_create = (
            'name', 'description', 'discordURL', 'videoURL', 'category', 'location', 'feature_image',
            'mission_date', 'mission_status', 'briefing', 'debriefing', 'created_at', 'updated_at', 'commander',
            'rsvp_users', 'attended_users',
        )

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f'testmissionname{n + 1}')
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    discordURL = fake.url(schemes=None)
    videoURL = fake.url(schemes=None)
    category = "EXP"
    location = "Yela"
    feature_image = fake.url(schemes=None)
    mission_date = "2019-09-13T04:57:03+0000"
    mission_status = "ACT"
    briefing = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    debriefing = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
    commander = user1
    created_at = "2019-09-13T04:57:03+0000"
    updated_at = "2019-09-13T04:57:03+0000"
