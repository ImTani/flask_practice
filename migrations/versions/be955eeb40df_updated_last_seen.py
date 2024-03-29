"""updated last_seen

Revision ID: be955eeb40df
Revises: 08b65956b503
Create Date: 2024-01-30 15:22:15.775440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be955eeb40df'
down_revision = '08b65956b503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('last_seen',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('last_seen',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
