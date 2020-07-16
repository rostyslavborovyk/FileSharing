"""files table

Revision ID: df80bad534df
Revises: 
Create Date: 2020-07-17 00:07:30.939668

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'df80bad534df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('file', sa.BLOB(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='cp1251',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
