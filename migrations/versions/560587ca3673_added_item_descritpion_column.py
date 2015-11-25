"""Added Item descritpion column

Revision ID: 560587ca3673
Revises: 1bf715ee31d4
Create Date: 2015-11-21 17:06:08.919585

"""

# revision identifiers, used by Alembic.
revision = '560587ca3673'
down_revision = '1bf715ee31d4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('description', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'description')
    ### end Alembic commands ###