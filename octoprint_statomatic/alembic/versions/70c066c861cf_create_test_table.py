"""create test table

Revision ID: 70c066c861cf
Revises:
Create Date: 2019-07-25 05:52:12.301019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70c066c861cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	op.create_table(
		'account',
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('name', sa.String(50), nullable=False),
		sa.Column('description', sa.Unicode(200)),
	)


def downgrade():
	op.drop_table('account')
