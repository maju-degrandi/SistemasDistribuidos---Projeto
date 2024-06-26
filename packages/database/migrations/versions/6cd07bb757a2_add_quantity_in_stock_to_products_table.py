"""'add_quantity_in_stock_to_products_table'

Revision ID: 6cd07bb757a2
Revises: 70ea070ea924
Create Date: 2024-06-20 17:39:10.883934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cd07bb757a2'
down_revision = '70ea070ea924'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity_in_stock', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('quantity_in_stock')

    # ### end Alembic commands ###
