"""update UploadDataModelwithModel

Revision ID: 559390991c39
Revises: 8a0cb12876b4
Create Date: 2022-06-15 15:26:45.752345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '559390991c39'
down_revision = '8a0cb12876b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('track_data', sa.Column('patient', sa.String(length=200), nullable=False))
    op.add_column('track_data', sa.Column('gender', sa.String(length=100), nullable=True))
    op.add_column('track_data', sa.Column('age', sa.String(length=100), nullable=True))
    op.add_column('track_data', sa.Column('place', sa.String(length=600), nullable=True))
    op.add_column('track_data', sa.Column('city', sa.String(length=200), nullable=True))
    op.add_column('track_data', sa.Column('province', sa.String(length=200), nullable=True))
    op.add_column('track_data', sa.Column('town', sa.String(length=200), nullable=True))
    op.add_column('track_data', sa.Column('county', sa.String(length=200), nullable=True))
    op.add_column('track_data', sa.Column('district', sa.String(length=200), nullable=True))
    op.add_column('track_data', sa.Column('relation', sa.String(length=500), nullable=True))
    op.add_column('track_data', sa.Column('rel_pat', sa.String(length=500), nullable=True))
    op.add_column('track_data', sa.Column('onset_time', sa.String(length=200), nullable=True))
    op.add_column('track_data', sa.Column('symptoms', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('track_data', 'symptoms')
    op.drop_column('track_data', 'onset_time')
    op.drop_column('track_data', 'rel_pat')
    op.drop_column('track_data', 'relation')
    op.drop_column('track_data', 'district')
    op.drop_column('track_data', 'county')
    op.drop_column('track_data', 'town')
    op.drop_column('track_data', 'province')
    op.drop_column('track_data', 'city')
    op.drop_column('track_data', 'place')
    op.drop_column('track_data', 'age')
    op.drop_column('track_data', 'gender')
    op.drop_column('track_data', 'patient')
    # ### end Alembic commands ###
