from db import db


class ItemTags(db.Model):
    # THIS TABLE GOING TO BE USED FOR THE MANY-TO-MANY RELATIONSHIP
    __tablename__ = "items_tags"

    id = db.Column(db.Integer, primary_key=True)

    # THESE TWO COLUMNS DEFINING THE RELATIONSHIP BETWEEN THE ITEMS AND THE TAGS
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
