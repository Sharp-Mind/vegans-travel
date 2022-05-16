from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Posts
import json


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     # Positional arguments
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    #     # Named (optional) arguments
    #     parser.add_argument(
    #         '--delete',
    #         action='store_true',
    #         help='Delete poll instead of closing it',
    #     )

    def handle(self, *args, **options):

        
        def jread ():
            with open('static/texts.json') as f:
                file_content = f.read()
                post_list = json.loads(file_content)

                for num, post in enumerate(post_list):
                    # print(post_list[num]['name'])               

                    post, created = Posts.objects.get_or_create(
                        name=post_list[num]['name'],
                        text=post_list[num]['text'],
                        picture=post_list[num]['picture']
                    )

                    print(created)
                # print(post_list[0]['name'])


        def jwrite():            
            t = "У нас были огромные планы на этот сезон! \n 😣 Но после того как случилась война, и мир безвозвратно изменился, мы поняли, что сейчас не время для рисков, потому что мы очень хотим сохранить наш проект, наши общие ценности и всё то, чего мы достигли за эти годы! \n Но несмотря на страшные события прямо у нас под боком, мы не должны забывать о себе. В такие времена обязательно нужно беречь себя, заботиться о себе и находить способы получать положительные эмоции, чтоб не тронуться и пережить всё это, ведь нам ещё вместе строить светлое будущее. \n Мы хотим напомнить вам о тех мероприятиях, которые у нас планируются этим летом: \n 🛣РОАДТРИП по Алтаю с 6 по 13 июля (возьмём ещё двух человек) \n 🏕ПОХОД на Алтае к подножию Белухи 18-31 июля (возьмём ещё пару человек в команду) \n 🏔ПОХОД на Кавказ. 11-21 августа Нагорье Лагонаки. Маршрут через горы к морю (ещё много свободных мест Больше многодневных мероприятий пока не будет. \n Летом мы проведём лишь несколько походов и выездов выходного дня, поэтому если вы давно хотели сходить с нами в горы, стать частью нашей семьи - это тот самый шанс! Ещё не знаем, что будет осенью, поедем ли мы куда-то и позовём ли вас. \n Заграничные походы и выезды пока отменены из-за нестабильной ситуации с рейсами, курсом валюты и прохождением границ. \n 🤍 Поход это отличная возможность для того, чтоб отвлечься от всех угнетающих новостей, наполнить себя новыми эмоциями, собрать в копилку тысячи счастливых моментов, перезагрузиться, заглянуть внутрь себя, найти новых друзей и прожить новый опыт, вспомнить, как много красивого и хорошего есть в нашем мире, несмотря ни на что! \n Обнимаем вас, поддерживаем в эти нелегкие времена и ждём в наших походах. ✍️По подробностям любых мероприятий пишите @mariewoohoo"
            t2 = " Уже на этих выходных! 7-8 мая \n Сплав по Москве реке + скалолазание! \n 7000 за всё! \n Давай откроем сезон приключений вместе? \n Пиши за подробностями в личку @mariewoohoo и прыгай к нам на борт!"

            post_list = (
                {'name': 'Сплав Москва','text': t, 'picture': 'photo_2022-04-28_20-54-22'},
                {'name': 'Новости', 'text': t2, 'picture': 'photo_2022-05-12_17-59-19'}
            )

            with open('static/texts.json', 'w') as f:
                to_write = json.dumps(post_list)
                f.write(to_write)

        # jwrite()
        jread()


        
