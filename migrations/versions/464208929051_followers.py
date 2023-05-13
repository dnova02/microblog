"""followers

Revision ID: 464208929051
Revises: b4c80866cf90
Create Date: 2023-05-12 23:00:59.287662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '464208929051'
down_revision = 'b4c80866cf90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###