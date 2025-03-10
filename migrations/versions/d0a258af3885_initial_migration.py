"""Initial migration

Revision ID: d0a258af3885
Revises: 
Create Date: 2025-02-26 10:32:05.829107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0a258af3885'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.drop_constraint('uq_notes_bugaga', type_='unique')
        batch_op.drop_column('bugaga')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bugaga', sa.VARCHAR(length=120), nullable=False))
        batch_op.create_unique_constraint('uq_notes_bugaga', ['bugaga'])

    # ### end Alembic commands ###
