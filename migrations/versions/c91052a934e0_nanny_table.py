"""Nanny table

Revision ID: c91052a934e0
Revises: b2207c4539f1
Create Date: 2023-11-08 22:11:57.842250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c91052a934e0'
down_revision = 'b2207c4539f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nanny',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nanny_selection',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('nanny_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['nanny_id'], ['nanny.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'nanny_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nanny_selection')
    op.drop_table('nanny')
    # ### end Alembic commands ###
