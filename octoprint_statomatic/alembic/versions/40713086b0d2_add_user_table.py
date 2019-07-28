"""add user table

Revision ID: 40713086b0d2
Revises: 70c066c861cf
Create Date: 2019-07-27 01:48:10.156806

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "40713086b0d2"
down_revision = "70c066c861cf"
branch_labels = None
depends_on = None


def upgrade():
	op.create_table(
		"users",
		sa.Column(
			"id", sa.Integer, primary_key=True
		),
		sa.Column(
			"name", sa.String(50), nullable=False
		)
	)


def downgrade():
	op.drop_table(
		"users"
	)
