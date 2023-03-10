"""empty message

Revision ID: d0feace473de
Revises: 6802ceab3f09
Create Date: 2022-12-03 11:48:59.411336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0feace473de'
down_revision = '6802ceab3f09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.alter_column('author',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.alter_column('author',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###
