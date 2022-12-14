"""update UploadDataModel

Revision ID: 8a0cb12876b4
Revises: 3446b66c86b7
Create Date: 2022-06-14 18:30:17.523144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a0cb12876b4'
down_revision = '3446b66c86b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('track_data', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('track_data', 'create_time')
    # ### end Alembic commands ###
