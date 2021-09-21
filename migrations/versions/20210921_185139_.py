"""empty message

Revision ID: f519e7b9fba5
Revises: ffdc0a98111c
Create Date: 2021-09-21 18:51:39.802485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f519e7b9fba5'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('subbed', sa.Integer(), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['subbed'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'subbed')
    )
    op.add_column('users', sa.Column('profileImgUrl', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profileImgUrl')
    op.drop_table('subscribers')
    # ### end Alembic commands ###
