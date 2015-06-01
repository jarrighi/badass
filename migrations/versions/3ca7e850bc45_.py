"""empty message

Revision ID: 3ca7e850bc45
Revises: 23ffcb1ca4a1
Create Date: 2015-05-31 10:05:06.118819

"""

# revision identifiers, used by Alembic.
revision = '3ca7e850bc45'
down_revision = '23ffcb1ca4a1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('skills', sa.Column('description', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('skills', 'description')
    ### end Alembic commands ###
