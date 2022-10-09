"""reviews table

Revision ID: 822a168a8dc3
Revises: 13316e9313bb
Create Date: 2022-10-04 21:57:05.697756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '822a168a8dc3'
down_revision = '13316e9313bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_entry_description', table_name='entry')
    op.drop_index('ix_entry_title', table_name='entry')
    op.drop_table('entry')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entry',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=64), nullable=False),
    sa.Column('description', sa.VARCHAR(length=120), nullable=False),
    sa.Column('status', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_entry_title', 'entry', ['title'], unique=False)
    op.create_index('ix_entry_description', 'entry', ['description'], unique=False)
    # ### end Alembic commands ###
