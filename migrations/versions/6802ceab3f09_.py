"""empty message

Revision ID: 6802ceab3f09
Revises: 03f62c94f664
Create Date: 2022-12-03 11:35:10.864370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6802ceab3f09'
down_revision = '03f62c94f664'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.alter_column('author',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.alter_column('author',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
