"""added about me, last seen to user.

Revision ID: 08b65956b503
Revises: e26c95daa513
Create Date: 2024-01-24 20:27:21.876881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08b65956b503'
down_revision = 'e26c95daa513'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=40), nullable=False))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
