import datetime
from operator import itemgetter
from copy import copy


class Scheduler:
    def __init__(self, config, logger, env_mode):

        self.env_mode = env_mode

        self.scheduler_config = config

        self.schedule_runs = []

        self.logger = logger

    def init_schedule_runs(self, now):
        schedule_runs = []

        for read_date in self.scheduler_config['dates']:
            read_schedule = {}

            year = now.year
            month = now.month

            if read_date['day'] == 'daily':
                day = now.day
            else:
                day = read_date['day']

            hour = read_date['hour']

            if now > datetime.datetime(year, month, day, hour, 0, 0):
                if read_date['day'] == 'daily':
                    year, month, day = self.get_next_day(now)
                else:
                    year, month = self.get_next_month(year, month)

            read_schedule['date'] = datetime.datetime(year, month, day, hour, 0, 0)

            schedule_runs.append(read_schedule)

        schedule_runs_sorted = sorted(schedule_runs, key=itemgetter('date'), reverse=False)

        return schedule_runs_sorted

    @staticmethod
    def get_next_month(source_year, source_month):
        month = source_month
        year = source_year + month // 12
        month = month % 12 + 1

        return year, month

    @staticmethod
    def get_next_day(now):
        next_day = now + datetime.timedelta(days=1)
        month = next_day.month
        year = next_day.year
        day = next_day.day

        return year, month, day

    def get_next_read(self, now):
        next_task = None

        if self.env_mode in ['Development']:
            next_task = {'date': datetime.datetime.now()}

            return next_task

        self.schedule_runs = self.init_schedule_runs(now=now)

        for task in self.schedule_runs:
            if task['date'] > now:
                next_task = copy(task)

                break

        self.logger.info('Scheduler - next read - {}'.format(next_task))

        return next_task
