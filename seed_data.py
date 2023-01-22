from app import db
from app.models.Articles import Articles, StatusType
from app.models.Authors import Authors
from app.models.Tags import Tags

db.create_all()


author1 = Authors('Jonas', 'Jonaitis')
author2 = Authors('Petras', 'Petraitis')

db.session.add_all([author1, author2])
db.session.commit()


tag1 = Tags('Naujas')
tag2 = Tags('Zombiai')
tag3 = Tags('Helovynas')

db.session.add_all([tag1, tag2, tag3])
db.session.commit()


article1 = Articles(author1.id, 'Apie nieką', 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.', StatusType.PUBLISHED)
article2 = Articles(author1.id, 'Apie zombius', 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.')
article3 = Articles(author2.id, 'Braiiins!', 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.', StatusType.PUBLISHED)


article1.tags.append(tag1)
article1.tags.append(tag2)

article2.tags.append(tag2)
article2.tags.append(tag3)

article3.tags.append(tag3)

db.session.add_all([article1, article2, article3])
db.session.commit()
