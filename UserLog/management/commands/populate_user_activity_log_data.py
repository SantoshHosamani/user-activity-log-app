import datetime
from django.core.management.base import BaseCommand, CommandError
from UserLog.models import User, ActivityPeriods
from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = "Save randomly generated user record values."

    def get_date(self):
        return datetime.datetime.now()

    def add_arguments(self, parser):
        parser.add_argument('total', type=int,
                            help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):

        total = ''
        if 'total' in kwargs:
            # convert to int in case user provide string or float
            try:
                total = int(kwargs['total'])
            except ValueError:
                self.stdout.write(
                    'Please provide valid integer argumate with populate_user_activity_log_data command')
        else:
            total = 10

        for _ in range(total):
            fake_id = fake.ssn()
            fake_name = fake.name()
            fake_tz = 'Asia/Kolkata'
            start_time = self.get_date()

            # Add one hour to start time to generate stop time
            hours = 1
            hours_added = datetime.timedelta(hours=hours)
            stop_time = hours_added

            try:
                User(user_id=fake_id, real_name=fake_name, tz=fake_tz, activity_periods=ActivityPeriods(
                    start_time=start_time,
                    stop_time=stop_time
                )).save()

            except User.DoesNotExist:
                raise CommandError(
                    'Error while writing data to user collection')
                continue

        self.stdout.write(self.style.SUCCESS(
            'User records saved successfully.'))
