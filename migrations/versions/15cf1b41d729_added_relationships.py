"""Added relationships

Revision ID: 15cf1b41d729
Revises: 2cc9fc958e70
Create Date: 2015-11-21 17:46:44.850717

"""

# revision identifiers, used by Alembic.
revision = '15cf1b41d729'
down_revision = '2cc9fc958e70'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('category')
    op.add_column('items', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'items', 'categories', ['category_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_column('items', 'category_id')
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'category_pkey'),
    sa.UniqueConstraint('name', name=u'category_name_key')
    )
    op.drop_table('categories')
    ### end Alembic commands ###