"""add printers table

Revision ID: 27f733a958ce
Revises: 40713086b0d2
Create Date: 2019-07-28 07:29:42.286348

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "27f733a958ce"
down_revision = "40713086b0d2"
branch_labels = None
depends_on = None


def upgrade():
	op.create_table(
		"printers",
		sa.Column(
			"id", sa.Integer, primary_key=True, autoincrement=True
		),
		sa.Column(
			"identifier", sa.String(250), nullable=False, unique=True, index=True
		),
		sa.Column(
			"name", sa.String(250), nullable=False
		),
		sa.Column(
			"model", sa.String(250), nullable=False
		)
	)


def downgrade():
	op.drop_table(
		"printers"
	)
