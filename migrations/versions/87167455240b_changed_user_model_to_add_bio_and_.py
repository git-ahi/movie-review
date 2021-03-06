"""Changed user model to add bio and profile pic

Revision ID: 87167455240b
Revises: 58fdc3409291
Create Date: 2021-09-18 20:33:37.585857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87167455240b'
down_revision = '58fdc3409291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
