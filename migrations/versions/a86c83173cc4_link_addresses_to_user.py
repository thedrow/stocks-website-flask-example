"""link_addresses_to_user

Revision ID: a86c83173cc4
Revises: c5f7e838f9fc
Create Date: 2019-12-11 10:47:09.687199

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a86c83173cc4'
down_revision = 'c5f7e838f9fc'
branch_labels = None
depends_on = ['ea4921658ce2']


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('user_id', postgresql.UUID(), nullable=True))
    op.create_foreign_key(None, 'address', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'address', type_='foreignkey')
    op.drop_column('address', 'user_id')
    # ### end Alembic commands ###
